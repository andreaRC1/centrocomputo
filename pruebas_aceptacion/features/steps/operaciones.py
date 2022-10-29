from typing import ContextManager
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

def insertar_operacion(context):
    context.driver.get(context.url+"/operaciones/nuevo/")
    context.driver.find_element(By.ID, 'matricula').send_keys("")
    context.driver.find_element(By.ID, 'operacion').send_keys("Impresión")
    context.driver.find_element(By.ID, 'precio_unitario').send_keys(1)
    context.driver.find_element(By.ID, 'cantidad').send_keys(10)
    select = Select(context.driver.find_element(By.ID,'id_material'))
    select.select_by_visible_text("Hojas de impresión")
    context.driver.find_element(By.ID, "btn_aceptar").click()

@when(u'ingreso al apartado "{url}"')
def step_impl(context, url):
    context.driver.get(context.url+url)
    
@given(u'que ingreso al apartado "{url}"')
def step_impl(context, url):
    context.driver.get(context.url+url)
    
@when(u'que ingreso al apartado "{url}"')
def step_impl(context, url):
    context.driver.get(context.url+url)
    
@when(u'que ingreso las credenciales "{matricula}", "{nombre}", "{precio_u}", "{cantidad}" y "{material}"')
def step_impl(context, matricula, nombre, precio_u, cantidad, material):
    context.driver.find_element(By.ID, 'matricula').send_keys(matricula)
    context.driver.find_element(By.ID, 'operacion').send_keys(nombre)
    context.driver.find_element(By.ID, 'precio_unitario').send_keys(precio_u)
    context.driver.find_element(By.ID, 'cantidad').send_keys(cantidad)
    select = Select(context.driver.find_element(By.ID,'id_material'))
    select.select_by_visible_text(material)
    
@given(u'que ingreso las credenciales "", "Impresión", "1", "10" y "Hojas de impresión"')
def step_impl(context):
    context.driver.find_element(By.ID, 'matricula').send_keys("")
    context.driver.find_element(By.ID, 'operacion').send_keys("Impresión")
    context.driver.find_element(By.ID, 'precio_unitario').send_keys(1)
    context.driver.find_element(By.ID, 'cantidad').send_keys(10)
    select = Select(context.driver.find_element(By.ID,'id_material'))
    select.select_by_visible_text("Hojas de impresión")
        
@when(u'doy click en el botón {boton}')
def step_impl(context, boton):
    context.driver.find_element(By.ID, "btn_aceptar").click()


@then(u'puedo ver el mensaje de éxito "{mensaje}"')
def step_impl(context, mensaje):
    respuesta = context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]").text
    assert mensaje in respuesta, f'Esperado {mensaje}, obtenido {respuesta}' 

@given(u'reviso el saldo del usuario "{matricula}"')
def step_impl(context, matricula):
    context.saldo_actual = context.driver.find_element(By.XPATH, "//*[@id='tabla-usuarios']/table/tbody/tr[3]/td[3]").text
    
@then(u'puedo ver que el saldo es diferente.')
def step_impl(context):
    saldo_nuevo = context.driver.find_element(By.XPATH, "//*[@id='tabla-usuarios']/table/tbody/tr[3]/td[3]").text
    assert context.saldo_actual != saldo_nuevo, f'Saldo no cambió'
    
@then(u'puedo ver que el saldo no cambió.')
def step_impl(context):
    saldo_nuevo = context.driver.find_element(By.XPATH, "//*[@id='tabla-usuarios']/table/tbody/tr[3]/td[3]").text
    assert context.saldo_actual == saldo_nuevo, f'Saldo cambió'

@then(u'puedo ver el mensaje de error de operación "{mensaje}"')
def step_impl(context, mensaje):
    respuesta = context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]").text
    assert mensaje in respuesta, f'Esperado {mensaje}, obtenido {respuesta}' 
    

    
@when(u'ingreso al apartado de lista de operaciones')
def step_impl(context):
    context.driver.get(context.url + "/operaciones/lista")
    
@then(u'puedo ver la tabla de operaciones.')
def step_impl(context):
    flag = True
    try:
        context.driver.find_element(By.ID, 'tabla-operaciones')
    except:
        flag = False
    assert flag, f'No se encuentra la tabla de operaciones.'
    
@given(u'hay una operación insertada')
def step_impl(context):
    insertar_operacion(context)

@when(u'que doy click en el botón de ver última operación.')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="tabla-operaciones"]/table/tbody/tr/td[5]/div/a').click()

@then(u'puedo ver la tabla de {tabla}.')
def step_impl(context, tabla):
    resultado = context.driver.find_elements(By.XPATH, '/html/body/div/div/div/div/table/tbody/tr')
    assert len(resultado) == 1, f'Esperado 1, obtenido {len(resultado)})' 

@when(u'que doy click en el botón de eliminar última operación.')
def step_impl(context):
    context.num_operaciones = context.driver.find_elements(By.XPATH, '//*[@id="tabla-operacion"]/tbody/tr')
    context.driver.find_element(By.XPATH, '//*[@id="tabla-operaciones"]/table/tbody/tr/td[5]/div/button').click()
    
@when(u'que confirmo la eliminación')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="formEliminar"]/button').click()


@then(u'puedo ver que en la lista de operaciones que se eliminó la operación.')
def step_impl(context):
    actual = context.driver.find_elements(By.XPATH, '//*[@id="tabla-operacion"]/tbody/tr')
    assert len(actual) == len(context.num_operaciones)-1, f'Operaciones encontradas: {len(actual)}, esperadas {len(context.num_operaciones)-1}'


    