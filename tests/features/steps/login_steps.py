from behave import given, when, then

from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage


@given("que o usuário acessa a página de login")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.driver.get("https://www.saucedemo.com")


@when("ele realiza login com usuário válido")
def step_valid_login(context):
    context.login_page.login(
        "standard_user",
        "secret_sauce"
    )


@when("ele realiza login com senha inválida")
def step_invalid_password(context):
    context.login_page.login(
        "standard_user",
        "senha_incorreta"
    )


@when("ele realiza login com usuário bloqueado")
def step_locked_user(context):
    context.login_page.login(
        "locked_out_user",
        "secret_sauce"
    )


@then("ele deve ser redirecionado para a página de inventário")
def step_validate_inventory(context):
    assert "inventory" in context.driver.current_url


@then("uma mensagem de erro deve ser exibida")
def step_validate_invalid_password(context):

    error_message = context.driver.find_element(
        "css selector",
        "[data-test='error']"
    ).text

    assert "Username and password do not match" in error_message


@then("uma mensagem de bloqueio deve ser exibida")
def step_validate_locked_user(context):

    error_message = context.driver.find_element(
        "css selector",
        "[data-test='error']"
    ).text

    assert "Sorry, this user has been locked out" in error_message