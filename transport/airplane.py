# импорт класса Vehicle из модуля vehicle
from .vehicle import Vehicle
# определение класса Airplane, наследующего от класса Vehicle
class Airplane(Vehicle):
    # конструктор класса, инициализирует атрибуты capacity и max_altitude
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity)  # вызов конструктора родительского класса
        self.max_altitude = max_altitude  # максимальная высота полёта самолёта в метрах
    # мгический метод __str__, который возвращает строковое представление объекта Airplane
    def __str__(self):
        return f"Airplane(ID={self.vehicle_id}, Capacity={self.capacity} tons, Current Load={self.current_load} tons, Max Altitude={self.max_altitude} meters)"