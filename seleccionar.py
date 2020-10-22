from persona import Persona
from conexion import Conexion
from logger_base import logger

#Las clases proveen una forma de empaquetar datos y funcionalidad juntos. 
class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''
    __SELECCIONAR = 'SELECT * FROM public.dbcrud ORDER BY id_persona'
    
    @classmethod
    #Las funciones en Python son creadas mediante la sentencia def:
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)
        Conexion.cerrar()    
        return personas               
    
if __name__ == '__main__':

     #Aqui podemos seleccionar un registro
    personas = PersonaDao.seleccionar()  
    for persona in personas:
        logger.debug(persona)
        logger.debug(persona.get_id_persona())
    
   
