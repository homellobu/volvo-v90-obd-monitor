from __future__ import annotations

import asyncio
import contextlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class DTCRecord:
    code: str
    module: str
    status: str
    data: dict[str, Any]


@dataclass
class DiagnosticSnapshot:
    timestamp: str
    vehicle: dict[str, Any]
    modules: list[dict[str, Any]]
    dtc: list[DTCRecord]
    live: dict[str, Any]


class ReadOnlyDiagnosticBackend:
    """Base segura. Sin transporte ni borrado implementados todavía."""

    def __init__(self, config_path: str = "config/default.toml") -> None:
        self.config_path = Path(config_path)
        self.connected = False
        self.read_only = True
        self.snapshot = DiagnosticSnapshot(
            timestamp=datetime.now(timezone.utc).isoformat(),
            vehicle={"vin": None, "platform": "SPA"},
            modules=[],
            dtc=[],
            live={
                "coolant_temp_c": None,
                "rpm": None,
                "speed_kmh": None,
                "battery_v": None,
                "intake_temp_c": None,
                "intake_pressure_kpa": None,
                "dpf_soot_percent": None,
                "dpf_temperature_c": None,
                "dpf_regeneration_active": None,
            },
        )

    def status(self) -> dict[str, Any]:
        return {
            "connected": self.connected,
            "read_only": self.read_only,
            "timestamp": self.snapshot.timestamp,
        }

    async def discover(self) -> dict[str, Any]:
        """Placeholder: no envía paquetes al vehículo."""
        return {"status": "not_configured", "modules": []}

    async def get_vehicle(self) -> dict[str, Any]:
        return self.snapshot.vehicle

    async def get_modules(self) -> list[dict[str, Any]]:
        return self.snapshot.modules

    async def get_dtc(self) -> list[dict[str, Any]]:
        return [
            {"code": item.code, "module": item.module, "status": item.status, "data": item.data}
            for item in self.snapshot.dtc
        ]

    async def clear_dtc(self, confirmation: str) -> dict[str, Any]:
        if confirmation != "CONFIRM_BORRADO_DTC":
            return {"success": False, "reason": "confirmation_required"}
        return {
            "success": False,
            "reason": "disabled_safety",
            "message": "Borrado no implementado",
        }

    async def close(self) -> None:
        self.connected = False


async def main() -> None:
    backend = ReadOnlyDiagnosticBackend()
    print(backend.status())
    await backend.discover()
    await backend.close()


if __name__ == "__main__":
    asyncio.run(main())
