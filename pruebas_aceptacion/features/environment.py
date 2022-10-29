from selenium import webdriver
from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from unittest import TestCase


@fixture
def browser_chrome(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = Chrome(options=options)
    context.url = 'http://192.168.33.10:8000'
    yield context
    

def before_all(context):
    use_fixture(browser_chrome, context)
    # -- NOTE: CLEANUP-FIXTURE is cal