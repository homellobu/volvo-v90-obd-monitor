# Hardware seleccionado

## Adaptador

- Producto: FENNICA, ASIN B0F5W8QGSS
- Tipo anunciado: cable VOE OBD-II a Ethernet/RJ45
- Incluye adaptador USB–Ethernet según la descripción comercial
- Uso previsto: transporte Ethernet/DoIP entre el V90 SPA y un host

## Verificación pendiente

Esta selección se basa en la compatibilidad anunciada para Volvo SPA. Antes de usar el adaptador, validar:

- conector OBD-II completo y sin daños;
- adaptador USB–Ethernet reconocido por el sistema;
- dirección IP de la interfaz;
- puerto TCP/UDP utilizado por el vehículo;
- enlace con la batería estabilizada;
- comunicación real con el V90;
- ausencia de tráfico de escritura;
- versión y firmware del adaptador, si están disponibles.

## Vehículo

- Volvo V90 Cross Country
- Año: 2018
- Motor: D4 diésel
- Potencia: 190 CV
- Plataforma: SPA

## Condiciones de uso

- Desarrollo inicial exclusivamente en modo lectura.
- No borrar DTC hasta validar el backend y el módulo objetivo.
- No realizar codificación, reprogramación, adaptaciones ni pruebas actuadoras.
- Registrar y revisar los resultados antes de interpretar PIDs/DIDs.
- Mantener una alimentación estable mientras se conecte al puerto OBD-II.

## Identificación técnica

El producto no incluye una API ni debe considerarse software diagnóstico. Actúa como interfaz física entre el OBD-II y el host. La aplicación de este repositorio implementará el transporte y validará las respuestas recibidas.
