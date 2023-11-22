from dispositivo import Dispositivo


class Database:
    def __init__(self, database_template):
        self.database = []

        dispositivos = database_template.get("dispositivos")
        for dispositivo in dispositivos:
            self.database.append(Dispositivo(diccionario=dispositivo))

    def delete_by_id(self, id):
        to_delete = -1
        for position in range(len(self.database)):
            if self.database[position].id == id:
                to_delete = position
        if to_delete != -1:
            self.database.pop(to_delete)

    def add_dispositivo(self, dispositivo=None, diccionario=None):
        if dispositivo:
            self.database.append(dispositivo)
        elif diccionario:
            self.database.append(Dispositivo(diccionario=diccionario))











