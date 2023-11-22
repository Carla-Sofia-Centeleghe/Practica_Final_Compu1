class Persona:
    def __init__(self,nombre,apellido,edad):
        if edad < 18:
            raise MenorEdadException('La Persona sigue siendo menor de edad')
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class MenorEdadException(Exception):
    pass