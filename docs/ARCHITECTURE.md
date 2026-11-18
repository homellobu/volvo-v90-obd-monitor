# Arquitectura

```text
Puerto OBD-II
  -> adaptador VOE OBD-II a RJ45
  -> red Ethernet del host
  -> backend DoIP/UDS
  -> API REST/WebSocket
  -> ESP32/Wio Terminal y navegador móvil
```

## Componentes

### Adaptador VOE

Debe proporcionar transporte Ethernet/DoIP. Confirmar antes de integrar:

- protocolo DoIP o transporte alternativo;
- dirección IP o modo DHCP;
- puerto TCP/UDP;
- estabilidad al identificar módulos;
- documentación del fabricante.

### Host

Raspberry Pi o PC para la primera fase. El ESP32 no se recomienda como host completo para UDS/DoIP.

### Backend

Responsable de descubrir el adaptador, establecer sesión DoIP, direccionar ECU, ejecutar servicios UDS permitidos, validar respuestas y registrar el tráfico.

### Wio Terminal

Solo mostrará datos recibidos y no implementará transporte Volvo directo.

## API prevista

```text
GET  /api/status
GET  /api/vehicle
GET  /api/modules
GET  /api/dtc
GET  /api/live
POST /api/dtc/clear       # deshabilitado hasta confirmación segura
WS   /ws/live
```

No se implementará reprogramación, codificación, adaptaciones o actuadores en fases iniciales.
