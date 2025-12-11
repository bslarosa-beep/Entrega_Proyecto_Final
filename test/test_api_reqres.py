import requests
import pytest
import json
import time
from utils.logger import logger 

#obtener usuarios
@pytest.mark.get
def test_get_users(url_base,header_request):
    logger.info("Validando ID de usuario específico")
    response = requests.get(f"{url_base}/2", headers=header_request)

    logger.info(f"Response Body: {response.json()}")
    logger.info(f"Status Code: {response.status_code}")
    assert response.status_code == 200

    data = response.json()

    assert "data" in data, "La clave 'data' no está en la respuesta"
    assert len(data["data"]) > 0, "No se encontraron usuarios en la respuesta"

    print(json.dumps(data, indent=4))

#crear usuario
@pytest.mark.post
def test_create_user(url_base,header_request):
 payload = {
    "name": "Barbara La Rosa",
    "job": "QA"
    }

 response = requests.post(url_base, headers=header_request, json=payload)
 logger.info(f"Response Body: {response.json()}")
 logger.info(f"Status Code: {response.status_code}")
 assert response.status_code == 201
 data = response.json()

 logger.info(f"Response Data: {data}")
 assert data["name"] == payload["name"], "El nombre no coincide"
 assert data["job"] == payload["job"], "El trabajo no coincide"
 assert "id" in data, "No se generó un ID para el nuevo usuario"

#actualizar usuario
@pytest.mark.put
def test_update_user(url_base,header_request):
   
   payload = {
      "name": "Barbara La Rosa",
      "job": "QE"}   
   
   inicio = time.time()

   response = requests.get(f"{url_base}/2", headers=header_request)

   tiempo_diff = time.time() - inicio

 #Validación del status code
   assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

   body = response.json()
   #Validación 
   logger.info(f"Response Body: {body}")
    