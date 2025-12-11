import pytest
from utils.datos import leer_csv_login
from pages.login_page import LoginPage

from utils.logger import logger

@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_validation(driver, usuario, password, debe_funcionar):
    logger.info(f"Iniciando prueba de login con usuario: {usuario}, debe_funcionar: {debe_funcionar}")
    login_page = LoginPage(driver)
    login_page.abrir_pagina().login_completo(usuario, password)

    if debe_funcionar:
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        mensaje_error = login_page.obtener_error()
        assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando"