import logging

# Variable logger a utilizar
logger = logging

#El logging de Python es una herramienta útil para prevenir errores, controlar los ataques de piratas informáticos o, simplemente, llevar a cabo análisis.

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])

#Basicamente el logging de Python registra errores de código simples y genera un mensaje. ​
if __name__ == '__main__':
    logging.warning('mensaje a nivel warning')
    logging.info('mensaje a nivel info')
    logging.debug('mensaje a nivel debug')
    logging.error('Ocurrió un error en la base de datos')
    logging.debug('se realizó la conexión con exito')
