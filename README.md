# Volvo V90 OBD Monitor

Sistema independiente de monitorización y diagnóstico para **Volvo V90 Cross Country D4 2018 (plataforma SPA)**.

## Ruta seleccionada

**Ruta A: VOE Ethernet / DoIP**

La interfaz física será un adaptador OBD-II compatible con Ethernet/DoIP. El primer host será un PC o Raspberry Pi; el Wio Terminal y el ESP32 se incorporarán como capa de visualización y conectividad.

## Objetivos

- Monitorizar datos OBD-II estándar en tiempo real.
- Detectar y registrar DTC por módulo.
- Leer identificadores, VIN y datos de diagnóstico disponibles.
- Mostrar datos en un Wio Terminal y en un panel web móvil.
- Preparar integración UDS/DoIP configurable.
- Reservar datos Volvo específicos sin inventar PIDs.
- Mantener el borrado de DTC y las funciones sensibles deshabilitadas hasta confirmación explícita.

## Arquitectura inicial

```text
V90 OBD-II
    |
Adaptador VOE Ethernet/DoIP
    |
Raspberry Pi / PC
    |
Backend Python (DoIP + UDS)
    ├── REST API
    ├── WebSocket
    ├── MQTT opcional
    └── almacenamiento local
    |
Wio Terminal  <── WiFi ──>  Panel web móvil
```

## Estado de desarrollo

Se empieza por los servicios de lectura. El soporte DPF, mantenimiento avanzado, funciones de servicio y reprogramación quedará desactivado hasta confirmar el adaptador y los datos reales del vehículo.

## Reglas de seguridad

- Solo lectura durante el desarrollo inicial.
- Guardar los DTC antes de cualquier borrado.
- Borrado de DTC con confirmación doble.
- Sin reprogramación, codificación ni actuadores sin procedimiento validado.
- No interpretar respuestas desconocidas como datos reales de Volvo.

## Estructura

```text
backend/       Cliente DoIP/UDS, API y persistencia
wio_terminal/  Código Arduino para la pantalla
esp32_bridge/  Puente WiFi/MQTT opcional
web/           Panel web responsive
config/        Configuración de red y PIDs/DIDs
docs/          Arquitectura, seguridad y catálogo diagnóstico
```

## Hardware

- Vehículo: Volvo V90 Cross Country D4 2018, plataforma SPA
- Adaptador: confirmar modelo exacto OBD-II Ethernet/DoIP compatible con SPA
- Host inicial: Raspberry Pi o PC
- Pantalla: Seeed Wio Terminal
- Puente opcional: ESP32-C6

## Licencia

MIT
