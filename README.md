# report_ticket
Permite la impresión del ticket fiscal (impresora térmica ) desde la factura

Documentación Detallada
Pasos para Implementar el Módulo
Crear la Estructura del Módulo: Crea las carpetas y archivos como se muestra en la estructura anterior.

Definir Metadata del Módulo: En __manifest__.py, define la metadata y las dependencias del módulo.

Crear Plantillas de Cabecera y Pie: En report_header.xml y report_footer.xml, define el contenido de la cabecera y el pie del reporte.

Definir el Reporte Principal: En report_ticket.xml, define la estructura del reporte y haz referencia a la cabecera y el pie.

Configurar Acciones del Reporte: Asegúrate de que la acción del reporte está correctamente definida para que aparezca en las opciones de impresión.

Ajustar Dimensiones para Impresora Térmica: Usa estilos CSS para ajustar el ancho del reporte a las dimensiones de una impresora térmica.

Actualizar y Reiniciar Odoo: Actualiza el módulo y reinicia el servidor de Odoo para aplicar los cambios.

Notas
Personalización: Ajusta los contenidos y estilos de los archivos XML según las necesidades específicas de tu proyecto.

Reutilización: Puedes copiar esta estructura y ajustar los detalles específicos (nombres, IDs, contenidos) para otros proyectos.
