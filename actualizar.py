from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''
 
    __ACTUALIZAR = 'UPDATE public.dbcrud SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s' 
   
            
    @classmethod
    def actualizar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al actualizar persona:{e}') 
        finally:
            Conexion.cerrar()
            
    
if __name__ == '__main__':
  
    id_persona = input ("Para actualizar ingrese ID: " )  
    nombre = input ("Ingrese nombre: " )   
    apellido = input ("Ingrese apellido: " )  
    email = input ("Ingrese email: " )  
    persona = Persona (id_persona,nombre,apellido,email) 
    personas_actualizadas = PersonaDao.actualizar(persona)
    logger.debug(f'Personas actualizadas: {personas_actualizadas}')
 
