# Catálogo de PIDs y DIDs

## PIDs OBD-II previstos

| PID | Dato | Fórmula inicial |
|---|---|---|
| 0105 | Temperatura refrigerante | A - 40 °C |
| 010C | RPM | ((A × 256) + B) / 4 |
| 010D | Velocidad | A km/h |
| 010F | Temperatura admisión | A - 40 °C |
| 0111 | Apertura acelerador | 100 × A / 255 % |
| 0142 | Voltaje módulo | (256 × A + B) / 1000 V |

Los valores deben validarse con telemetría real.

## DPF

Los PIDs Volvo no deben asumirse como PIDs universales. Reservar datos configurables para hollín, temperatura DPF, presión diferencial, distancia de regeneración y estado activo.

## Regeneración

- temperatura DPF > 600 °C: evidencia primaria solo con DID verificado;
- disminución del hollín: evidencia auxiliar solo con dato comprobado;
- datos no validados se marcan como desconocidos.

## DTC

Distinguir DTC UDS, OBD-II P0/P2/P3 y códigos por módulo. No crear descripciones sin fuente verificable.
