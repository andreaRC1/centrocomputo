Característica: Como administrador deseo agregar un usuario
                para que así quede registrado en el sistema.

    ###### Realizar Operación ###########
    Escenario: Agregar usuario como administrador
        Dado que ingreso al sistema como "administrador"
        Y que ingreso al apartado "/usuarios/nuevo"
        Cuando coloco las credenciales de usuario "usuario_prueba", "12345678" y "15"
        Y doy click en el botón Agregar
        Entonces puedo ver que la lista de usuarios se incrementó.