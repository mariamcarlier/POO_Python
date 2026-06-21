
---
### Porque se separaron asi los archivos? 
  > las carpetas de models y services
  - Porque es una práctica estándar en arquitectura de software: 
    - los 📂models representan qué es algo (la entidad, sus datos, su comportamiento propio)
    - los 📂services representan qué hace el sistema con esas entidades (gestionarlas, guardarlas, listarlas). 
    ###### Es la misma separación de responsabilidades que ya identificamos cuando sacamos crear_usuario(), eliminar_usuario(), etc. fuera de UsuarioGaleria.
    
 - Cada carpeta lleva un archivo __init__.py vacío — es lo que le dice a Python "esta carpeta es un paquete, puedes importar cosas de aquí". Lo crearás vacío, no necesita contenido.