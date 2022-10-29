from django.contrib.auth.models import User
from django.test import TestCase
from equipos.forms import EquipoForm
from script_grupos import crear_grupos
from usuarios.models import Usuario
from equipos.models import Equipo
from materiales.models import Material, TipoMaterial
from operaciones.models import Operacion
from django.core.exceptions import ValidationError

class TestModels(TestCase):
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


    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)

    def test_return_object_usuario(self):
        self.usuario.full_clean()
        self.usuario.save()
        self.assertEqual(User.objects.first().username, self.usuario.__str__())

    def test_nombre_es_requerido(self):
        usuario = Usuario(
            username='isaacdiaz',
            password='Contra12345'
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()

  
    def test_nombre_usuario_no_acepta_espacios(self):
        self.usuario.username = 'isaac d'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

    def test_matricula_no_acepta_letras(self):
        self.usuario.full_clean()
        self.usuario.matricula = '3412rt67'
        self.assertRaises(ValidationError, self.usuario.full_clean())

    def test_matricula_no_acepta_espacios(self):
        #self.usuario.full_clean()
        self.usuario.matricula = '34 12 67'
        self.assertRaises(ValidationError, self.usuario.full_clean())

    def test_nombre_usuario_no_acepta_vacios(self):
        self.usuario.username = ''
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

    def test_matricula_usuario_no_acepta_vacios(self):
        self.usuario.matricula = ''
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass
            
        

    def test_saldo_no_acepta_letras(self):
        self.usuario.full_clean()
        self.usuario.saldo = '2rt6'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

    def test_saldo_no_acepta_espacios(self):
        #self.usuario.full_clean()
        self.usuario.saldo = '3 12'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

    def test_saldo_no_acepta_vacios(self):
        self.usuario.saldo = ''
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

    

    def test_pwd_no_acepta_espacios(self):
        self.usuario.full_clean()
        self.usuario.password = '3 12'
        self.usuario.full_clean()

    def test_pwd_no_acepta_vacios(self):
        self.usuario.full_clean()
        self.usuario.password = ''
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

  
    
def setUp(self, tipo='DeEscritorio', marca='lenovo',
              modelo='xp1800', disponibilidad='Dsiponible'):
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

def test_return_object_equipo(self):
        self.usuario.full_clean()
        self.usuario.save()
        self.assertEqual(Equipo.objects.first().tipo, self.Equipo.__str__())

def test_nombre_usuario_no_acepta_espacios(self):
        self.usuario.username = 'isaac d'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

def test_matricula_no_acepta_punto(self):
    self.usuario.full_clean()
    self.usuario.matricula = '3412.t67'
    self.assertRaises(ValidationError, self.usuario.full_clean())

def test_matricula_no_acepta_espacios(self):
    self.usuario.full_clean()
    self.usuario.matricula = '34 12 67'
    self.assertRaises(ValidationError, self.usuario.full_clean())

def test_nombre_equipo_no_acepta_espacios(self):
        self.usuario.username = 'isaac d'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()
        pass

def test_matricula_no_acepta_le(self):
    self.usuario.full_clean()
    self.usuario.matricula = '3412rt67'
    self.assertRaises(ValidationError, self.usuario.full_clean())

def test_matricula_no_acepta_espacios(self):
    self.usuario.full_clean()
    self.usuario.matricula = '34 12 67'
    self.assertRaises(ValidationError, self.usuario.full_clean())
 