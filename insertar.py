from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''

    __INSERTAR = 'INSERT INTO public.dbcrud(nombre, apellido, email) VALUES(%s,%s,%s)'
    
    
    @classmethod
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al insertar persona:{e}') 
        finally:
            Conexion.cerrar()
                     
    
if __name__ == '__main__':
    
    nombre = input ("Ingrese nombre: " )   
    apellido = input ("Ingrese apellido: " )  
    email = input ("Ingrese email: " )  
    persona = Persona ("",nombre,apellido,email) 
    personas_insertadas = PersonaDao.insertar(persona)
    logger.debug(f'Personas insertados: {personas_insertadas}')


