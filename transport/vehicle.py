# импортируем модуль uuid для генерации уникальных идентификаторов
import uuid
from transport.client import Client
# определение класса Vehicle для транспортного средства
class Vehicle:
    # конструктор класса, инициализирует атрибуты vehicle_id, capacity, current_load и clients_list
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4())  # уникальный идентификатор транспортного средства, генерируется случайно
        self.capacity = capacity  # грузоподъемность транспортного средства в тоннах
        self.current_load = 0  # текущая загрузка транспортного средства, изначально 0
        self.clients_list = []  # список клиентов, чьи грузы загружены
    # метод для загрузки груза от клиента в транспортное средство
    def load_cargo(self, client):
        # проверка, является ли client объектом класса Client
        if not isinstance(client, Client):
            raise ValueError("Неверные данные клиента")
        # проверка, превышает ли суммарная загрузка грузоподъемность транспортного средства
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Превышение грузоподъемности транспортного средства")
        # увеличение текущей загрузки на вес груза клиента
        self.current_load += client.cargo_weight
        # добавление клиента в список клиентов
        self.clients_list.append(client)
    # магический метод __str__, который возвращает строковое представление объекта Vehicle
    def __str__(self):
        return f"Vehicle(ID={self.vehicle_id}, Capacity={self.capacity} tons, Current Load={self.current_load} tons)"