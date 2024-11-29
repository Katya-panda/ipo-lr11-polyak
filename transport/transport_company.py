# импорт класса client из модуля client
from .client import Client
# импорт класса vehicle из модуля vehicle
from .vehicle import Vehicle
# импорт класса airplane из модуля airplane
from .airplane import Airplane
# импорт класса van из модуля van
from .van import Van
# определение класса transportcompany для транспортной компании
class TransportCompany:
    # конструктор класса, инициализирует атрибуты name, vehicles и clients
    def __init__(self, name):
        self.name = name            # название компании
        self.vehicles = []          # список транспортных средств компании
        self.clients = []           # список клиентов компании
    # метод для добавления транспортного средства
    def add_vehicle(self, vehicle):
        # проверка, является ли vehicle объектом класса vehicle
        if not isinstance(vehicle, Vehicle):
            raise ValueError("invalid vehicle data")  # генерация ошибки при неверных данных транспортного средства
        self.vehicles.append(vehicle)  # добавление транспортного средства в список vehicles
    # метод для получения списка всех транспортных средств
    def list_vehicles(self):
        return self.vehicles  # возвращает список транспортных средств
    # метод для добавления клиента
    def add_client(self, client):
        # проверка, является ли client объектом класса client
        if not isinstance(client, Client):
            raise ValueError("invalid client data")  # генерация ошибки при неверных данных клиента
        self.clients.append(client)  # добавление клиента в список clients
    # метод для оптимизации распределения грузов между транспортными средствами
    def optimize_cargo_distribution(self):
        # выделение vip-клиентов в отдельный список
        vip_clients = [client for client in self.clients if client.is_vip]
        # выделение обычных клиентов в отдельный список
        regular_clients = [client for client in self.clients if not client.is_vip]
        # объединение списков vip и обычных клиентов, vip-клиенты первыми
        clients = vip_clients + regular_clients
        # распределение грузов клиентов по транспортным средствам
        for client in clients:
            for vehicle in self.vehicles:
                try:
                    vehicle.load_cargo(client)  # попытка загрузить груз клиента в транспортное средство
                    break  # выход из внутреннего цикла при успешной загрузке
                except ValueError:
                    continue  # продолжение цикла при возникновении ошибки загрузки
    # магический метод __str__, который возвращает строковое представление объекта transportcompany
    def __str__(self):
        return f"transportcompany(name={self.name}, vehicles={len(self.vehicles)}, clients={len(self.clients)})"