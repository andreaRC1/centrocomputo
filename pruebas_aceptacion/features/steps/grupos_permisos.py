from typing import ContextManager
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

@given(u'que ingreso al sistema como "{tipo_usuario}"')
def step_impl(context, tipo_usuario):
    login(context, tipo_usuario)


@when(u'me dirijo al apartado "{url}"')
def step_impl(context, url):
    context.driver.get(context.url + url)


@when(u'doy click en un botón de grupos no asignado a alguno de los usuarios')
def step_impl(context):
    grupo = context.driver.find_element(By.XPATH, "//*[@id='tabla-usuarios']/table/tbody/tr[4]/td[4]/a[3]")
    context.grupo_clase = grupo.get_attribute("class")
    context.driver.find_element(By.XPATH,'//*[@id="tabla-usuarios"]/table/tbody/tr[4]/td[4]/a[3]').click()
    


@then(u'puedo ver en la lista de usuarios que el tipo de usuario se cambió.')
def step_impl(context):
    grupo = context.driver.find_element(By.XPATH, "//*[@id='tabla-usuarios']/table/tbody/tr[4]/td[4]/a[3]")
    cambio = grupo.get_attribute("class")
    assert cambio != context.grupo_clase, 'No se encontraron cambios {cambio}'



@when(u'utilizo la barra lateral de dashboard')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="sidepanel-toggler"]').click()
    lateral = context.driver.find_element(By.ID, 'app-nav-main')
    opciones = lateral.find_element(By.ID, 'menu-accordion')
    lista_opciones = []
    botones = opciones.find_elements(By.ID, "opciones")
    for boton in botones:
        desp = boton.find_element(By.ID, 'desplegable')
        lista_opciones.append(desp.find_element(By.CLASS_NAME, 'nav-link-text').text)
        
    try:    
        no_desplegables = opciones.find_elements(By.ID, 'no-desplegable')
        for item in no_desplegables:
            opcion = item.find_element(By.CLASS_NAME, 'nav-link')
            lista_opciones.append(opcion.find_element(By.CLASS_NAME, 'nav-link-text').text)
        context.lista_opciones = lista_opciones
    except:
        context.lista_opciones = lista_opciones



@then(u'puedo hacer click en cualquier opción de navegación.')
def step_impl(context):
    esperados = ['Operaciones', 'Usuarios', 'Materiales', 'Equipos', 'Graficos', 'Reportes']
    assert esperados == context.lista_opciones, f'No coinciden los elementos. Esperados {esperados}, obtenidos {context.lista_opciones}'
    
    

@then(u'puedo hacer click sobre las opciones de usuarios, equipos y operaciones.')
def step_impl(context):
    esperados = ['Operaciones', 'Usuarios', 'Equipos']
    assert esperados == context.lista_opciones, f'No coinciden los elementos. Esperados {esperados}, obtenidos {context.lista_opciones}'


@then(u'puedo hacer click en la opción de operaciones.')
def step_impl(context):
    esperados = ['Operaciones']
    assert esperados == context.lista_opciones, f'No coinciden los elementos. Esperados {esperados}, obtenidos {context.lista_opciones}'




@then(u'puedo ver el mensaje de error "{tipo_error}"')
def step_impl(context, tipo_error):
    error = context.driver.find_element(By.CLASS_NAME, 'io').text
    assert tipo_error in error, f'Mensaje no encontrado. Esperado {tipo_error}, obtenido {error}'



@then(u'puedo ver la lista de "{tipo_lista}".')
def step_impl(context, tipo_lista):
    tag = "tabla-" + tipo_lista
    flag = True
    try:
        context.driver.find_element(By.ID, tag)
    except:
        flag = False
    assert flag, f'No se encontró la lista.'


def login(context, tipo_usuario):
    context.driver.get(context.url)
    context.driver.find_element(By.ID, 'id_username').send_keys(tipo_usuario)
    context.driver.find_element(By.ID, 'id_password').send_keys(tipo_usuario)
    context.driver.find_element(By.ID, 'btn_ingresar').click()
    