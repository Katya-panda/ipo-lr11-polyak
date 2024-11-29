# определение класса Client для клиента компании
class Client:
    # конструктор класса, инициализирует атрибуты name, cargo_weight и is_vip
    def __init__(self, name, cargo_weight, is_vip=False):
        self.name = name                 # имя клиента
        self.cargo_weight = cargo_weight # вес груза клиента
        self.is_vip = is_vip             # флаг VIP-статуса клиента, по умолчанию False
    # магический метод __str__, который возвращает строковое представление объекта Client
    def __str__(self):
        return f"Client(name={self.name}, cargo_weight={self.cargo_weight}, is_vip={self.is_vip})"