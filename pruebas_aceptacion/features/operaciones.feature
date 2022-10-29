Característica: Como usuario deseo agregar una operación
                para que así quede registrada en el sistema.

    ###### Realizar Operación ###########
    Escenario: Ver mensaje de operación exitosa. 
        Dado que ingreso al sistema como "administrador"
        Y que ingreso al apartado "/operaciones/lista"
        Cuando ingreso al apartado "/operaciones/nuevo" 
        Y que ingreso las credenciales "34154287", "Impresión", "1", "10" y "Hojas de impresión"
        Y doy click en el botón aceptar
        Entonces puedo ver el mensaje de éxito "Operación realizada."
        
    Escenario: Comprobar operación exitosa. 
        Dado que ingreso al sistema como "administrador"
        Y que ingreso al apartado "/usuarios/lista"
        Y reviso el saldo del usuario "34154287"
        Cuando ingreso al apartado "/operaciones/nuevo" 
        Y que ingreso las credenciales "34154287", "Impresión", "1", "10" y "Hojas de impresión"
        Y doy click en el botón aceptar
        Y que ingreso al apartado "/usuarios/lista"
        Entonces puedo ver que el saldo es diferente.

    Escenario: Ver mensaje de error con matrícula inválida. 
        Dado que ingreso al sistema como "administrador"
        Y que ingreso al apartado "/operaciones/lista"
        Cuando ingreso al apartado "/operaciones/nuevo"  
        Y que ingreso las credenciales "1", "Impresión", "1", "10" y "Hojas de impresión"
        Y doy click en el botón aceptar
        Entonces puedo ver el mensaje de error de operación "Datos incorrectos."
        
    Escenario: Comprobar operación no realizada con matrícula inválida. 
        Dado que ingreso al sistema como "administrador"
        Y que ingreso al apartado "/usuarios/lista"
        Y reviso el saldo del usuario "34154287"
        Cuando ingreso al apartado "/operaciones/nuevo" 
        Y que ingreso las credenciales "1", "Impresión", "1", "10" y "Hojas de impresión"
        Y doy click en el botón aceptar
        Y que ingreso al apartado "/usuarios/lista"
        Entonces puedo ver que el saldo no cambió.

    
    Escenario: Realizar operación con usuario no matriculado. 
        Dado que ingreso al apartado "/operaciones/nuevo"
        Y que ingreso las credenciales "", "Impresión", "1", "10" y "Hojas de impresión"
        Cuando doy click en el botón aceptar
        Entonces puedo ver el mensaje de éxito "Operación realizada."


    #### Ver Lista Operaciones ####

    Escenario: Ver lista de operaciones.
        Dado que ingreso al sistema como "administrador"
        Cuando ingreso al apartado de lista de operaciones
        Entonces puedo ver la tabla de operaciones.

    ### Ver Operación #### 
    Escenario: Ver operación.
        Dado que ingreso al sistema como "administrador"
        Y hay una operación insertada
        Cuando ingreso al apartado de lista de operaciones
        Y que doy click en el botón de ver última operación.
        Entonces puedo ver la tabla de "Detalles de Operación".

    ### Eliminar operación ####
    Escenario: Eliminar operación.
        Dado que ingreso al sistema como "administrador"
        Y hay una operación insertada
        Cuando ingreso al apartado de lista de operaciones
        Y que doy click en el botón de eliminar última operación.
        Y que confirmo la eliminación
        Entonces puedo ver que en la lista de operaciones que se eliminó la operación.



    