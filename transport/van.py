# импорт класса Vehicle из модуля vehicle
from .vehicle import Vehicle
# определение класса Van, наследующего от класса Vehicle
class Van(Vehicle):
    # конструктор класса, инициализирует атрибуты capacity и is_refrigerated
    def __init__(self, capacity, is_refrigerated):
        super().__init__(capacity)  # вызов конструктора родительского класса
        self.is_refrigerated = is_refrigerated  # флаг, указывающий на наличие холодильника в фургоне
    # магический метод __str__, который возвращает строковое представление объекта Van
    def __str__(self):
        return f"Van(ID={self.vehicle_id}, Capacity={self.capacity} tons, Current Load={self.current_load} tons, Refrigerated={self.is_refrigerated})"