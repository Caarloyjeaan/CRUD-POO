from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad public.dbcrud
    '''
    __SELECCIONAR = 'SELECT * FROM public.dbcrud ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO public.dbcrud(nombre, apellido, email) VALUES(%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE public.dbcrud SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s' 
    __ELIMINAR = 'DELETE FROM public.dbcrud WHERE id_persona = %s'
    
    @classmethod
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
            
    @classmethod
    def eliminar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al eliminar persona:{e}') 
        finally:
            Conexion.cerrar()                
    
if __name__ == '__main__':
    personas = PersonaDao.seleccionar()    
    for persona in personas:
        logger.debug(persona)
        logger.debug(persona.get_id_persona())
    
    #Insertamos un nuevo registro
    #persona = Persona(nombre='Maria', apellido='Elena', email='nena.22@mail.com')
    #personas_insertadas = PersonaDao.insertar(persona)
    #logger.debug(f'Personas insertados: {personas_insertadas}')
    
    #Actualizar un registro existente
    #persona = Persona(10,'Carolina','Torres', 'Catatorres@mail.com')
    #personas_actualizadas = PersonaDao.actualizar(persona)
    #logger.debug(f'Personas actualizadas: {personas_actualizadas}')
    
    #eliminar un registro existente
    persona = Persona(id_persona=10)
    personas_eliminadas = PersonaDao.eliminar(persona)
    logger.debug(f'Personas eliminadas: {personas_eliminadas}')