from django.contrib.auth.models import User
from django.test import TestCase
from usuarios.models import Usuario 
from usuarios.forms import UsuarioFormLog, UsuarioForm
from equipos.models import Equipo
from equipos.forms import EquipoForm
from materiales.models import Material, TipoMaterial
from materiales.forms import TipoMaterialForm, MaterialForm
from operaciones.models import Operacion
from operaciones.forms import OperacionForm
from django.core.exceptions import ValidationError


class TestFormUsuario(TestCase):

    def setUp(self, nombre='isaacdiaz', matricula='34123456',
              password='Contra12345', saldo='100', password_re='Contra12345',
              nompreOp='imprimir', precio_unitario=5, cantidad=3, material = 'hojas oficio',
              nombreMaterial='hojas oficio', precio=100, descripcion= 'urgente', fecha='05/12/21',
              tipo='impresora', marca='epson', modelo='laserjet', disponibilidad='D', nombreTM="tinta"):
        
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

        self.tipomaterial= TipoMaterial(
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

    def test_usuario_form_valido(self):
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_valido_log(self):
        form = UsuarioFormLog(self.data_log)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UsuarioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_vacio_log(self):
        self.data['username'] = ''
        form = UsuarioFormLog(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_matricula_invalida_vacia(self):
        self.data['matricula'] = ''
        form = UsuarioForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['matricula'],
            ['This field is required.'])

    def test_usuario_form_matricula_invalida_vacia_log(self):
        self.data['matricula'] = ''
        form = UsuarioFormLog(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['matricula'],
            ['This field is required.'])

    def test_usuario_form_matricula_valida(self):
        self.data['matricula'] = '34123456'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_matricula_invalida(self):
        self.data['matricula'] = 'a34123456'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_saldo_invalida(self):
        self.data['saldo'] = 'no'
        form = UsuarioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_saldo_valida(self):
        self.data['saldo'] = '100'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_matricula_invalida_muy_chica_mod(self):
        self.data_log['matricula'] = '123'
        form = UsuarioFormLog(self.data_log)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_invalido(self):
        self.data['username'] = 'aana5678'
        form = UsuarioFormLog(self.data_log)
        self.assertTrue(form.is_valid())
        
    def test_usuario_form_nombre_invalida_numero_letra(self):
        self.data['username'] = '76423'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())
        

    def test_usuario_form_nombre_valida_log(self):   
        self.data_log['username'] = 'isaacdiaz'
        form = UsuarioFormLog(self.data_log)
        self.assertTrue(form.is_valid())
      
    def test_usuario_form_password_formato_invalido(self):
        self.data_log['password'] = 'co'
        form = UsuarioFormLog(self.data_log)
        self.assertTrue(form.is_valid())

    def test_usuario_form_password_formato_valido(self):
        self.data_log['password'] = 'Contra12345'
        form = UsuarioFormLog(self.data_log)
        self.assertTrue(form.is_valid())

    def test_usuario_form_password_vacia_invalida(self): 
        self.data_log['password'] = ''
        form = UsuarioFormLog(self.data_log)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_mas_caracteres(self): 
        self.data['username'] = 'isaacdiazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_password_mas_caracteres(self):  
        self.data_log['password'] = 'Contra12345'*15
        form = UsuarioFormLog(self.data_log)
        self.assertFalse(form.is_valid())

    def crear_usuario(self):
        User.objects.create_user(
            username='isaacdiaz',
            matricula='34153376',
            password='Contra12345',
        )
  
class TestFormOperaciones(TestCase):

    def setUp(self, nombre='imprimir', precio_unitario='2',
              cantidad='100', material='hoja oficio'):
        self.operacion = Operacion(
            nombre=nombre,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            material= TipoMaterial.objects.get_or_create(TipoMaterial = material[0])
        )

        self.data = {
            'nombre': nombre,
            'precio_unitario': precio_unitario,
            'cantidad': cantidad,
            'materiales.TipoMaterial': material
        }

class TestFormEquipos(TestCase):
    def setUp(self, tipo='DeEscritorio', marca='lenovo',
              modelo='xp1800', disponibilidad='D'):
        self.Equipo = Equipo(
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            disponibilidad=disponibilidad
        )

        self.data = {
            'tipo': tipo,
            'marca': marca,
            'modelo': modelo,
            'disponibilidad': disponibilidad
        }


    def test_equipo_form_valido(self):
        form = EquipoForm(self.data)
        self.assertTrue(form.is_valid())

    def test_equipo_form_tipo_vacio(self):
        self.data['tipo'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_equipo_form_modelo_invalido_vacia(self):
        self.data['tipo'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['tipo'],
            ['This field is required.'])

    def test_equipo_form_tipo_vacio(self):
        self.data['tipo'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_equipo_form_modelo_invalido_vacia_eq(self):
        self.data['tipo'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['tipo'],
            ['This field is required.'])

    def test_equipo_form_marca_vacio(self):
        self.data['marca'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_equipo_form_marca_invalido_vacia(self):
        self.data['marca'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['marca'],
            ['This field is required.'])

    def test_equipo_form_marca_vacio(self):
        self.data['marca'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_equipo_form_marca_invalido_vacia(self):
        self.data['marca'] = ''
        form = EquipoForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['marca'],
            ['This field is required.'])

    def test_equipo_form_marca_invalido_num(self):
        self.data['marca'] = '12'
        form = EquipoForm(self.data)
        self.assertTrue(form.is_valid())
        