from persona import Persona
from conexion import Conexion
from logger_base import logger

#Las clases proveen una forma de empaquetar datos y funcionalidad juntos. 
class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''
 
    __ACTUALIZAR = 'UPDATE public.dbcrud SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s' 
   
            
    @classmethod
    #Las funciones en Python son creadas mediante la sentencia def:
    def actualizar(cls, persona):
        #El try bloque le permite probar un bloque de código en busca de errores.
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        #El except bloque le permite manejar el error.
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al actualizar persona:{e}')
        #El finally bloque le permite ejecutar código, independientemente del resultado de los bloques try y except. 
        finally:
            Conexion.cerrar()
            

if __name__ == '__main__':
  
    #Aqui podemos actualizar un registro 
    id_persona = input ("Para actualizar ingrese ID: " )  
    nombre = input ("Ingrese nombre: " )   
    apellido = input ("Ingrese apellido: " )  
    email = input ("Ingrese email: " )  
    persona = Persona (id_persona,nombre,apellido,email) 
    personas_actualizadas = PersonaDao.actualizar(persona)
    logger.debug(f'Personas actualizadas: {personas_actualizadas}')
 
