from django.contrib.auth.models import User
from django.test import TestCase
from script_grupos import crear_grupos
from usuarios.models import Usuario
from equipos.models import Equipo
from materiales.models import Material, TipoMaterial
from operaciones.models import Operacion



class TestViews(TestCase):
    def setUp(self, nombre='administrador2', matricula='35154261',
              password='Administrador123', saldo='100', password_re='Contra12345',
              nompreOp='imprimir', precio_unitario=5, cantidad=3, material = 'hojas oficio',
              nombreMaterial='hojas oficio', precio=100, descripcion= 'urgente', fecha='05/12/21',
              tipo='impresora', marca='epson', modelo='laserjet', disponibilidad='D', nombreTM="tinta"):

        crear_grupos()
        
        self.usuario = Usuario(
            username=nombre,
            matricula=matricula,
            saldo=saldo,
            password=password
        )
        
        self.equipo = Equipo(
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            disponibilidad=disponibilidad
        )

        self.insertar= TipoMaterial(
            nombre=TipoMaterial
        )


        self.data = {
            'username': nombre,
            'matricula': matricula,
            'saldo': saldo
        }

        self.data_log = {
            'matricula': matricula,
            'username': nombre,
            'password': password
        }

        self.data_nuevo = {
            'username': nombre,
            'matricula': matricula,
            'saldo': saldo
        }

        self.data_tm = {
            'nombre': nombreTM,
        }

        self.data_equipo = {
            'tipo': tipo,
            'marca': marca,
            'modelo': modelo,
            'descripcion': descripcion
        }
        

    ###ADMINISTRADOR - USUARIOS

    ################## TEST DEL NOMBRE EN USUSRIO NUEVO admin
    def test_no_agrega_sin_nombre_usuario_nuevo_admin(self):
        self.login_admin()
        self.data_nuevo['username'] = ''
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)
    
    def test_no_agrega_invalido_usuario_admin(self):
        self.login_admin()
        self.data_nuevo['username'] = 'el'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_no_agrega_invalido_usuario_invalido_num_admin(self):
        self.login_admin()
        self.data_nuevo['username'] = 'el123'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    ################## TEST DEL NOMBRE EN USUSRIO NUEVO cajero
    def test_no_agrega_sin_nombre_usuario_nuevo_cajero(self):
        self.login_cajero()
        self.data_nuevo['username'] = ''
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)
    
    def test_agrega_invalido_usuario_cajero(self):
        self.login_cajero()
        self.data_nuevo['username'] = 'el'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario_invalido_num_cajero(self):
        self.login_cajero()
        self.data_nuevo['username'] = 'el123'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario_invalido_num_cajero(self):
        self.login_cajero()
        self.data_nuevo['username'] = 'cajero'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    ################## TEST DEL NOMBRE EN USUSRIO NUEVO alumno
    def test_agrega_sin_nombre_usuario_nuevo_alumno(self):
        self.login_alumno()
        self.data_nuevo['username'] = ''
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)
    
    def test_agrega_invalido_usuario_alumno(self):
        self.login_alumno()
        self.data_nuevo['username'] = 'el'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario_invalido_num_alumno(self):
        self.login_alumno()
        self.data_nuevo['username'] = 'el123'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_agrega_invalido_usuario_invalido_num_alumno(self):
        self.login_alumno()
        self.data_nuevo['username'] = 'cajero'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)


     ################## TEST DE LA MATRICULA EN USUARIO NUEVO
    def test_no_agrega_sin_matricula_usuario_nuevo(self):
        self.login_admin()
        self.data_nuevo['matricula'] = ''
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)
    
    def test_no_agrega_matricula_invalido_usuario(self):
        self.login_admin()
        self.data_nuevo['matricula'] = 'el'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)

    def test_no_agrega_invalido_matricula_usuario_invalido_num(self):
        self.login_admin()
        self.data_nuevo['matricula'] = 'el123'
        response =self.client.post('/usuarios/nuevo', self.data_nuevo)
        self.assertEqual(response.status_code, 301)


    def test_no_agrega_sin_saldo_usuario_nuevo(self):
        self.login_admin()
        self.data['saldo'] = ''
        response =self.client.post('/usuarios/nuevo', self.data)
        self.assertEqual(response.status_code, 301)
    
    def test_no_agrega_saldo_invalido_usuario(self):
        self.login_admin()
        self.data['saldo'] = 'el'
        response =self.client.post('/usuarios/nuevo', self.data)
        self.assertEqual(response.status_code, 301)

    def test_agrega_valido_saldo_usuario_num(self):
        self.login_admin()
        self.data['saldo'] = '1'
        response =self.client.post('/usuarios/nuevo', self.data)     
        self.assertEqual(response.status_code, 301)

    
    def test_no_agrega_sin_saldo_usuario_nuevo(self):
        self.login_admin()
        self.data_tm['saldo'] = ''
        response =self.client.post('/usuarios/nuevo', self.data)
        self.assertEqual(response.status_code, 301)
    
    def test_no_agrega_saldo_invalido_usuario(self):
        self.login_admin()
        self.data['saldo'] = 'el'
        response =self.client.post('/usuarios/nuevo', self.data)
        self.assertEqual(response.status_code, 301)

    def test_agrega_valido_saldo_usuario_num(self):
        self.login_admin()
        self.data['saldo'] = '1'
        response =self.client.post('/usuarios/nuevo', self.data)  
        self.assertEqual(response.status_code, 301)

    def test_no_agrega_contra_usuario_nuevo_log(self):
        self.data_log['password'] = ''
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301)
    
    def test_agrega_contra_invalido_usuario_log(self):
        self.login_admin()
        self.data_log['password'] = 'el'
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301)

    def test_no_agrega_contra_invalido_num_log(self):
        self.login_admin()
        self.data_log['password'] = '100'
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301)

    def test_agrega_contra_valido_log(self):
        self.login_admin()
        self.data_log['password'] = 'Administrador123'
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301) 
        
    def test_agrega_nombre_vacio_log_admin(self):
        self.login_admin()
        self.data_log['username'] = ''
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301)
    
    def test_agrega_nombre_invalido_usuario_log_admin(self):
        self.login_admin()
        self.data_log['username'] = 'el'
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301)

    def test_agrega_nombre_invalido_num_log_admin(self):
        self.login_admin()
        self.data_log['username'] = '100'
        response =self.client.post('/usuarios/login', self.data_log)
        self.assertEqual(response.status_code, 301)

    def test_agrega_nombre_valido_admin(self):
        self.login_admin()
        self.data_log['username'] = 'isaacdiaz'
        response =self.client.post('/usuarios/login', self.data_log)   
        self.assertEqual(response.status_code, 301)


    def test_admin_ingresa_lista_usuarios(self):
        self.login_admin()
        response = self.client.get('/usuarios/lista/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_nuevo_usuario(self):
        self.login_admin()
        response = self.client.get('/usuarios/nuevo/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_editar_usuario(self):
        self.login_admin()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_template_correcto_lista_usuario(self):
        self.login_admin()
        response = self.client.get('/usuarios/lista/')
        self.assertTemplateUsed(response, 'usuarios/usuario_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_editar_usuario(self):
        self.login_admin()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'editar_usuario.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_nuevo_usuario(self):
        self.login_admin()
        response = self.client.get('/usuarios/nuevo/')
        self.assertTemplateUsed(response, 'usuarios/usuario_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    ### Admin - Equipos

    def test_admin_ingresa_lista_equipos(self):
        self.login_admin()
        response = self.client.get('/equipos/lista/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_nuevo_equipo(self):
        self.login_admin()
        response = self.client.get('/equipos/nuevo/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_editar_equipo(self):
        self.insertar_equipo()
        self.login_admin()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_detalle_equipo(self):
        self.insertar_equipo()
        self.login_admin()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_template_correcto_lista_equipos(self):
        self.login_admin()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'equipos/equipo_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    ###ADMINISTRADOR - OPERACIONES

    def test_admin_ingresa_lista_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/lista/')
        self.assertEqual(response.status_code, 200)

    def test_admin_template_correcto_lista_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_nuevo_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_lista_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_nuevo_operacion(self):
        self.login_admin()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    ###ADMINISTRADOR - TIPOMATERIAL
    def test_admin_ingresa_url_tipoMaterial(self):
        self.insertar_tipoMaterial()
        self.login_admin()
        response = self.client.get('/tipomaterial/lista/')
        self.assertEqual(response.status_code, 200)

    ###ADMINISTRADOR - MATERIALES

    def test_admin_ingresa_lista_materiales(self):
        self.login_admin()
        response = self.client.get('/materiales/lista/')
        self.assertEqual(response.status_code, 200)

    ###CAJERO - USUARIOS

    def test_cajero_ingresa_lista_usuarios(self):
        self.login_cajero()
        response = self.client.get('/usuarios/lista/')
        self.assertEqual(response.status_code, 200)

    def test_cajero_ingresa_url_nuevo_usuario(self):
        self.login_cajero()
        response = self.client.get('/usuarios/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_ingresa_url_editar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_correcto_lista_usuario(self):
        self.login_cajero()
        response = self.client.get('/usuarios/lista/')
        self.assertTemplateUsed(response, 'usuarios/usuario_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_incorrecto_editar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_template_incorrecto_nuevo_usuario(self):
        self.login_cajero()
        response = self.client.get('/usuarios/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_ingresa_eliminar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/eliminar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_incorrecto_eliminar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/eliminar/' + str(last.id))
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_template_correcto_eliminar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/eliminar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')

    ###CAJERO - EQUIPO

    def test_cajero_ingresa_lista_equipos(self):
        self.login_cajero()
        response = self.client.get('/equipos/lista/')
        self.assertEqual(response.status_code, 200)

    def test_cajero_ingresa_url_nuevo_equipo(self):
        self.login_cajero()
        response = self.client.get('/equipos/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_ingresa_url_editar_equipo(self):
        self.insertar_equipo()
        self.login_cajero()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_cajero_ingresa_url_detalle_equipo(self):
        self.insertar_equipo()
        self.login_cajero()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_cajero_template_correcto_lista_equipos(self):
        self.login_cajero()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'equipos/equipo_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_correcto_lista_equipos(self):
        self.login_cajero()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'equipos/equipo_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_incorrecto_nuevo_equipo(self):
        self.login_cajero()
        response = self.client.get('/equipos/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_ingresa_lista_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/lista/')
        self.assertEqual(response.status_code, 200)

    def test_cajero_template_correcto_lista_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_correcto_nuevo_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_incorrecto_lista_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_ingresa_url_tipoMaterial(self):
        self.insertar_tipoMaterial()
        self.login_cajero()
        response = self.client.get('/tipomaterial/lista/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_incorrecto_tipomaterial_lista(self):
        self.login_cajero()
        response = self.client.get('/tipomaterial/lista/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_ingresa_lista_materiales(self):
        self.login_cajero()
        response = self.client.get('/materiales/lista/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_incorrecto_materiales_lista(self):
        self.login_cajero()
        response = self.client.get('/materiales/lista/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_ingresa_lista_usuarios(self):
        self.login_alumno()
        response = self.client.get('/usuarios/lista/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_nuevo_usuario(self):
        self.login_alumno()
        response = self.client.get('/usuarios/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_editar_usuario(self):
        self.login_alumno()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_alumno_template_incorrecto_usuario_lista(self):
        self.login_alumno()
        response = self.client.get('/usuarios/lista/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_incorrecto_usuario_nuevo(self):
        self.login_alumno()
        response = self.client.get('/usuarios/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_incorrecto_usuario_editar(self):
        self.login_alumno()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_ingresa_lista_equipos(self):
        self.login_alumno()
        response = self.client.get('/equipos/lista/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_nuevo_equipo(self):
        self.login_alumno()
        response = self.client.get('/equipos/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_editar_equipo(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_detalle_equipo(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_alumno_template_incorrecto_lista_equipo(self):
        self.login_alumno()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_correcto_lista_equipo(self):
        self.login_alumno()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_incorrecto_nuevo_equipos(self):
        self.login_alumno()
        response = self.client.get('/equipos/nuevo/')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_correcto_nuevo_equipos(self):
        self.login_alumno()
        response = self.client.get('/equipos/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_equipos_detaller(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_incorrecto_equipos_detaller(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_incorrecto_equipos_editar(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_correcto_equipos_editar(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_ingresa_lista_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/lista/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_template_correcto_lista_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_nuevo_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_lista_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateNotUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_nuevo_operacion(self):
        self.login_alumno()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_ingresa_url_tipoMaterial(self):
        self.insertar_tipoMaterial()
        self.login_alumno()
        response = self.client.get('/tipomaterial/lista/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_lista_materiales(self):
        self.login_alumno()
        response = self.client.get('/materiales/lista/')
        self.assertEqual(response.status_code, 403)

    def login_admin(self):
        self.client.login(username='administrador2', password='Administrador123')

    def login_cajero(self):
        self.client.login(username='cajero2', password='Cajero123')

    def login_alumno(self):
        self.client.login(username='alumne', password='Alumno123')
