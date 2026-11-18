# Estado del prototipo

El prototipo ofrece una API local de solo lectura y un panel web, pero **todavía no se comunica con el vehículo**. Los endpoints devuelven estado no disponible hasta validar la interfaz física y la configuración de red del adaptador `OBD2-RJ45-ENET-2M`.

No hay implementación de DoIP/UDS, lectura real de DTC, PID, escritura o borrado. El endpoint de borrado responde bloqueado deliberadamente.
