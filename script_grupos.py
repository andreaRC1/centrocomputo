from usuarios.models import Usuario
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group, User
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centrocomputo.settings')
django.setup()


def crear_grupos():
    administrador_grupo = Group.objects.create(name='admin_group')
    cajero_grupo = Group.objects.create(name='cajero_group')
    alumno_grupo = Group.objects.create(name='alumno_group')

    content_type = ContentType.objects.get_for_model(Usuario)
    content_type2 = ContentType.objects.get_for_model(User)

    cajero_permiso = Permission.objects.create(
        codename='cajero_permiso',
        name='Permiso requerido para cajeros',
        content_type=content_type
    )
    alumno_permiso = Permission.objects.create(
        codename='alumno_permiso',
        name='Permiso requerido para alumnos',
        content_type=content_type
    )

    administrador_permiso = Permission.objects.create(
        codename='administrador_permiso',
        name='Permiso requerido para administradores',
        content_type=content_type2
    )

    '''
    administrador_permiso = Permission.objects.get(codename='administrador_permiso')
    cajero_permiso = Permission.objects.get(codename='cajero_permiso')
    alumno_permiso = Permission.objects.get(codename='alumno_permiso')
    '''

    administrador_grupo.permissions.add(administrador_permiso)
    administrador_grupo.permissions.add(cajero_permiso)
    administrador_grupo.permissions.add(alumno_permiso)

    cajero_grupo.permissions.add(cajero_permiso)
    cajero_grupo.permissions.add(alumno_permiso)

    alumno_grupo.permissions.add(alumno_permiso)

    administrador = Usuario.objects.create(username='administrador',
                                           matricula=34154281,
                                           saldo=0)

    cajero = Usuario.objects.create(username='cajero',
                                    matricula=34154282,
                                    saldo=0)

    alumno = Usuario.objects.create(username='alumno',
                                    matricula=34154287,
                                    saldo=1000)

    administrador2 = Usuario.objects.create(username='administrador2',
                                           matricula=35154261,
                                           saldo=0)

    julia = Usuario.objects.create(username='julia',
                                           matricula=35555555,
                                           saldo=0)

    cajero2 = Usuario.objects.create(username='cajero2',
                                    matricula=35154271,
                                    saldo=0)

    alumne = Usuario.objects.create(username='alumne',
                                    matricula=35154281,
                                    saldo=1000)

    alumno2 = Usuario.objects.create(username='alumno2',
                                     matricula=34154267,
                                     saldo=0)
    
    anonimo = Usuario.objects.create(username='Anónimo',
                                     matricula=00000000,
                                     saldo=0)
    
    administrador.set_password('administrador')
    julia.set_password('Julia123')
    cajero.set_password('cajero')
    alumno.set_password('alumno')
    alumno2.set_password('alumno2')
    anonimo.set_password('anonimo')

    administrador2.set_password('Administrador123')
    cajero2.set_password('Cajero123')
    alumne.set_password('Alumno123')

    administrador.save()
    cajero.save()
    alumno.save()
    alumno2.save()
    anonimo.save()
    julia.save()

    administrador2.save()
    cajero2.save()
    alumne.save()

    administrador_grupo.user_set.add(administrador2)
    cajero_grupo.user_set.add(cajero2)
    alumno_grupo.user_set.add(alumne)

    administrador_grupo.user_set.add(administrador)
    administrador_grupo.user_set.add(julia)
    cajero_grupo.user_set.add(cajero)
    alumno_grupo.user_set.add(alumno)
    alumno_grupo.user_set.add(alumno2)
    alumno_grupo.user_set.add(anonimo)

    
crear_grupos()
