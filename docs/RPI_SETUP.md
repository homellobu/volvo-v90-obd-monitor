# Lista de instalación para Raspberry Pi OS

## Fase 1: instalación del sistema

1. Instalar Raspberry Pi OS de 64 bits.
2. Actualizar el sistema:

```bash
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y python3 python3-venv python3-pip git
```

3. Conectar el adaptador USB–Ethernet al Raspberry Pi.
4. Conectar el cable OBD-II-RJ45/ENET al adaptador Ethernet.
5. Encender el vehículo, pero mantener al principio el motor apagado si es posible.

## Fase 2: identificar la interfaz

```bash
ip link
ip -br address
nmcli device status
```

Registrar el nombre real de la interfaz, por ejemplo `eth0`, `eth1` o `enx...`.

Configurar una dirección adecuada en una de las interfaces físicas sin deshabilitar WiFi durante las pruebas:

```bash
nmcli connection show
nmcli device set <INTERFACE> managed yes
```

No modificar la dirección ni el gateway hasta haber confirmado el esquema de red usado por el vehículo. No usar valores por suposición.

## Fase 3: comprobar el enlace físico

```bash
ethtool <INTERFACE>
ip link set <INTERFACE> down
ip link set <INTERFACE> up
ip -br address
sudo tcpdump -ni <INTERFACE> -e
```

La comprobación inicial debe buscar únicamente tráfico de descubrimiento de capa 2/3. No enviar solicitudes UDS ni de borrado.

## Fase 4: entorno Python

```bash
cd /home/pi
python3 -m venv volvo-obd/.venv
source volvo-obd/.venv/bin/activate
python -m pip install --upgrade pip
```

Dependencias iniciales previstas:

```text
fastapi
uvicorn[standard]
websockets
python-can
udsoncan
```

Estas dependencias no garantizan soporte DoIP ni comunicación con módulos Volvo. DoIP requiere una implementación o biblioteca validada.

## Fase 5: pruebas seguras

1. Confirmar que la interfaz Ethernet cambia de estado.
2. Capturar tráfico disponible.
3. Determinar direcciones IPv4, MAC y puertos anunciados.
4. Detectar paquetes de descubrimiento DoIP si existen.
5. Registrar el enlace sin enviar escrituras.
6. Implementar el backend solo después de confirmar el transporte.

## Comprobaciones prohibidas

- escribir parámetros;
- borrar DTC;
- iniciar reprogramación;
- codificar módulos;
- ejecutar adaptaciones;
- probar actuadores;
- enviar paquetes arbitrarios a todos los módulos.

## Archivos previstos

```text
backend/
  doip_client.py
  uds_client.py
  api.py
  models.py
  vehicle.py
  logging.py
config/default.toml
logs/
```
