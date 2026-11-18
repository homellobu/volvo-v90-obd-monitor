# Continuación de configuración en Raspberry Pi 4

Se usará el cable `OBD2-RJ45-ENET-2M`. La Raspberry Pi 4 tiene Ethernet integrado: no hace falta USB–Ethernet salvo que quieras separar la LAN del vehículo y la red doméstica. La topología puede requerir una segunda interfaz para que teléfono/WiFi y vehículo estén disponibles simultáneamente.

## Primero: registrar interfaces, sin vehículo conectado

En la Raspberry Pi ejecuta:

```bash
ip -br address
ip link
```

Guarda la salida. La interfaz integrada suele llamarse `eth0`, pero hay que confirmarlo; no configures una IP ni cambies rutas todavía.

Con el cable/adaptador conectado al Pi, revisa de nuevo:

```bash
ip -br address
ip -s link
```

El cable OBD-RJ45 puede terminar directamente en Ethernet. Si el enchufe del Pi y el del cable son ambos RJ45, conéctalos directamente; no añadas un USB–Ethernet a menos que necesites una interfaz adicional.

## Instalar y arrancar la API local (sin vehículo)

```bash
sudo apt update
sudo apt install -y git python3-venv python3-pip
cd ~
git clone https://github.com/homellobu/volvo-v90-obd-monitor.git
cd volvo-v90-obd-monitor
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.api:app --host 0.0.0.0 --port 8000
```

Desde otro dispositivo en la misma red abre `http://<IP-DE-LA-RASPBERRY>:8000`. La página mostrará explícitamente datos no disponibles: es lo esperado mientras no se implemente y valide el transporte del adaptador.

API de prueba:

- `GET /api/status`
- `GET /api/vehicle`
- `GET /api/modules`
- `GET /api/dtc`
- `GET /api/live`
- `POST /api/dtc/clear` (bloqueado intencionadamente)

## Antes de conectar al coche

Comparte la salida de `ip -br address` y una foto o descripción de ambos extremos del cable. Después se identificará el enlace y la red sin enviar órdenes de diagnóstico. No se debe fijar `192.168.0.2` ni asumir puerto/protocolo: esos valores de la ficha inicial son parámetros de ejemplo y deben contrastarse con el adaptador.
