import logging
import pathlib

audit_dir = pathlib.Path('logs')
#Validación si el directorio existe, si no, se crea.
audit_dir.mkdir(exist_ok=True)

#crear el archivo del logger
log_file = audit_dir / 'suite.log'

#nombre del archivo de log
logger = logging.getLogger('test_logger')
#Que tipo de datos se van a guardar en el log
logger.setLevel(logging.INFO)

if not logger.handlers:
    #formato del log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    #crear el manejador de archivo
    file_handler = logging.FileHandler(log_file,mode='a',encoding='utf-8')
    file_handler.setFormatter(formatter)

    #agregar el manejador al logger
    logger.addHandler(file_handler)