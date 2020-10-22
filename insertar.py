from persona import Persona
from conexion import Conexion
from logger_base import logger

#Las clases proveen una forma de empaquetar datos y funcionalidad juntos. 
class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''

    __INSERTAR = 'INSERT INTO public.dbcrud(nombre, apellido, email) VALUES(%s,%s,%s)'
    
    
    @classmethod
    #Las funciones en Python son creadas mediante la sentencia def:
    def insertar(cls, persona):
        #El try bloque le permite probar un bloque de código en busca de errores.
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        #El except bloque le permite manejar el error.
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al insertar persona:{e}')
        #El finally bloque le permite ejecutar código, independientemente del resultado de los bloques try y except. 
        finally:
            Conexion.cerrar()
                     
    
if __name__ == '__main__':
    
     #Aqui podemos insertar un registro
    nombre = input ("Ingrese nombre: " )   
    apellido = input ("Ingrese apellido: " )  
    email = input ("Ingrese email: " )  
    persona = Persona ("",nombre,apellido,email) 
    personas_insertadas = PersonaDao.insertar(persona)
    logger.debug(f'Personas insertados: {personas_insertadas}')


