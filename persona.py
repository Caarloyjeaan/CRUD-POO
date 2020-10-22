from logger_base import logger

class Persona:

    #Las funciones en Python son creadas mediante la sentencia def:
    #Este método _init_ se llama cuando se crea un objeto a partir de una clase y permite que la clase inicialice los atributos de la clase.
    def __init__(self, id_persona='%s', nombre='%s', apellido='%s', email='%s'):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    # _str_ Devuelve una cadena de caracteres con lo que queremos mostrar.
    def __str__(self):
        return (
            f'Id Persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'Email: {self.__email}'
        )

    #Al usar la palabra clave "self" accedemos a los atributos y métodos de la clase.
    #Los métodos get y set, son simples métodos que usamos en las clases para mostrar (get) o modificar (set) el valor de un atributo.
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_id_persona(self):
        return self.__id_persona

    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona



if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'email')
    logger.debug(persona1)
    # simulando un objeto a insertar de tipo persona
    persona2 = Persona(nombre='Maria', apellido='Elena',
                       email='Mebolanos@mail.com')
    logger.debug(persona2)
    # simular el caso de eliminar un objeto de tipo persona
    persona3 = Persona(id_persona=10)
    logger.debug(persona3)
