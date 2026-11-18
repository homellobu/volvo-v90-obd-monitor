# Seguridad

Este proyecto trabaja con sistemas eléctricos reales del vehículo.

## Solo lectura

Las fases iniciales leen identificadores, estado de módulos, DTC, freeze frame y datos disponibles.

## Operaciones prohibidas inicialmente

- borrado de DTC;
- reprogramación;
- cambio de configuración;
- codificación;
- resets;
- adaptaciones;
- pruebas actuadoras;
- modificación persistente.

## Borrado futuro

Deberá exigir: persistencia previa de DTC, confirmación explícita, identificación del módulo, bloqueo de reintentos, registro y respuesta positiva comprobada.

## Alimentación

Mantener batería estable, no desconectar durante escritura y detener funciones sensibles ante caída de energía.
