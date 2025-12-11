import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "test/test_login.py",
    "test/test_cart.py",
    "test/test_cart_json.py",
    "test/test_api_reqres.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)
