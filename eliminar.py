from persona import Persona
from conexion import Conexion
from logger_base import logger

#Las clases proveen una forma de empaquetar datos y funcionalidad juntos. 
class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''

    __ELIMINAR = 'DELETE FROM public.dbcrud WHERE id_persona = %s'
  
            
    @classmethod
    #Las funciones en Python son creadas mediante la sentencia def:
    def eliminar(cls, persona):
        #El try bloque le permite probar un bloque de código en busca de errores.
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        #El except bloque le permite manejar el error.
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al eliminar persona:{e}') 
        #El finally bloque le permite ejecutar código, independientemente del resultado de los bloques try y except.
        finally:
            Conexion.cerrar()                
    
if __name__ == '__main__':
  
     #Aqui podemos eliminar un registro
    id_persona = input ("Ingrese ID: " )    
    persona = Persona (id_persona,)
    personas_eliminadas = PersonaDao.eliminar(persona)
    logger.debug(f'Personas eliminadas: {personas_eliminadas}')
