import pytest
from pages.login_page import LoginPage
from faker import Faker

faker = Faker()

@pytest.mark.parametrize("usuario,password,debe_funcionar", [
    (faker.user_name(), faker.password(length=8,special_chars=True,upper_case=True,lower_case=True,digits=True), False),  # Usuario y contraseña aleatorios (deben fallar)
    ("standard_user", faker.password(), False)])  # Usuario válido y contraseña aleatoria (debe fallar)
def test_login_validation(driver, usuario, password, debe_funcionar):
    login_page = LoginPage(driver)
    login_page.abrir_pagina().login_completo(usuario, password)

    if debe_funcionar:
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        mensaje_error = login_page.obtener_error()
        assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando"