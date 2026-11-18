from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.diagnostic_backend import ReadOnlyDiagnosticBackend

app = FastAPI(
    title="Volvo V90 OBD Monitor API",
    version="0.1.0",
    description="Read-only application scaffold; no vehicle commands are sent.",
)
backend = ReadOnlyDiagnosticBackend()
app.mount("/static", StaticFiles(directory="web"), name="static")


@app.get("/", include_in_schema=False)
async def dashboard() -> FileResponse:
    return FileResponse("web/index.html")


@app.get("/api/status")
async def status() -> dict[str, Any]:
    return {
        **backend.status(),
        "adapter": "OBD2-RJ45-ENET-2M",
        "transport": "unverified",
        "message": "Sin conexión al vehículo; el backend todavía no transmite por Ethernet/DoIP.",
    }


@app.get("/api/vehicle")
async def vehicle() -> dict[str, Any]:
    return await backend.get_vehicle()


@app.get("/api/modules")
async def modules() -> dict[str, Any]:
    return {"status": "unavailable", "modules": []}


@app.get("/api/dtc")
async def dtc() -> dict[str, Any]:
    return {"status": "unavailable", "read_only": True, "codes": await backend.get_dtc()}


@app.get("/api/live")
async def live() -> dict[str, Any]:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "unavailable",
        "values": backend.snapshot.live,
    }


@app.post("/api/dtc/clear", status_code=403)
async def clear_dtc() -> dict[str, Any]:
    # Deliberately unavailable: this app has no vehicle transport or write path.
    return {"success": False, "reason": "disabled_safety"}


@app.websocket("/ws/live")
async def live_websocket(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        while True:
            await websocket.send_json(await live())
            await websocket.receive_text()
    except WebSocketDisconnect:
        pass
