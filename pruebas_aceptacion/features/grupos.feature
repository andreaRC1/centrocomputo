Característica: Como administrador deseo cambiar los grupos a los que pertenece un usuario 
                para restringir los permisos sobre el sistema.

    Escenario: Cambiar usuario como administrador. 
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/usuarios/lista"
        Y doy click en un botón de grupos no asignado a alguno de los usuarios
        Entonces puedo ver en la lista de usuarios que el tipo de usuario se cambió.

    Escenario: Ver opciones de navegación como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando utilizo la barra lateral de dashboard
        Entonces puedo hacer click en cualquier opción de navegación.

    Escenario: Ver opciones de navegación como cajero.
        Dado que ingreso al sistema como "cajero" 
        Cuando utilizo la barra lateral de dashboard 
        Entonces puedo hacer click sobre las opciones de usuarios, equipos y operaciones.

    Escenario: Ver opciones de navegación como alumno.
        Dado que ingreso al sistema como "alumno" 
        Cuando utilizo la barra lateral de dashboard 
        Entonces puedo hacer click en la opción de operaciones.

    Escenario: Ingresar al apartado de materiales como cajero.
        Dado que ingreso al sistema como "cajero" 
        Cuando me dirijo al apartado "/materiales/lista"
        Entonces puedo ver el mensaje de error "403"

    Escenario: Ingresar al apartado de materiales como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/materiales/lista"
        Entonces puedo ver la lista de "materiales".

    Escenario: Ingresar al apartado de usuarios como alumno.
        Dado que ingreso al sistema como "alumno" 
        Cuando me dirijo al apartado "/usuarios/lista"
        Entonces puedo ver el mensaje de error "403"

    Escenario: Ingresar al apartado de materiales como alumno.
        Dado que ingreso al sistema como "alumno" 
        Cuando me dirijo al apartado "/materiales/lista"
        Entonces puedo ver el mensaje de error "403"

    Escenario: Ingresar al apartado de equipos como alumno.
        Dado que ingreso al sistema como "alumno" 
        Cuando me dirijo al apartado "/equipos/lista"
        Entonces puedo ver el mensaje de error "403"

    Escenario: Ingresar al apartado de operaciones como alumno.
        Dado que ingreso al sistema como "alumno" 
        Cuando me dirijo al apartado "/operaciones/lista"
        Entonces puedo ver el mensaje de error "403"

    Escenario: Ingresar al apartado de usuarios como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/usuarios/lista"
        Entonces puedo ver la lista de "usuarios".

    Escenario: Ingresar al apartado de materiales como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/materiales/lista"
        Entonces puedo ver la lista de "materiales".

    Escenario: Ingresar al apartado de operaciones como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/operaciones/lista"
        Entonces puedo ver la lista de "operaciones".

    Escenario: Ingresar al apartado de equipos como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/equipos/lista"
        Entonces puedo ver la lista de "equipos".

    Escenario: Ingresar al apartado de usuarios como administrador.
        Dado que ingreso al sistema como "administrador" 
        Cuando me dirijo al apartado "/usuarios/lista"
        Entonces puedo ver la lista de "usuarios".

    Escenario: Ingresar al apartado de usuarios como cajero.
        Dado que ingreso al sistema como "cajero" 
        Cuando me dirijo al apartado "/usuarios/lista"
        Entonces puedo ver la lista de "usuarios".
