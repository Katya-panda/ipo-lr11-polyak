import json # импортируем модуль json для работы с файлами в формате JSON
from transport.client import Client # импортируем класс Client из модуля client
from transport.vehicle import Vehicle # импортируем класс Vehicle из модуля vehicle
from transport.airplane import Airplane # импортируем класс Airplane из модуля airplane
from transport.van import Van # импортируем класс Van из модуля van
from transport.transport_company import TransportCompany # импортируем класс TransportCompany из модуля transport_company
# функция для вывода меню
def display_menu(): 
    print("\nМеню:") # выводим меню
    print("1. Вывести все записи") # пункт меню для вывода всех записей
    print("2. Вывести запись по полю") # пункт меню для вывода записи по полю
    print("3. Добавить запись") # пункт меню для добавления записи
    print("4. Удалить запись по полю") # пункт меню для удаления записи по полю
    print("5. Оптимизировать распределение грузов") # пункт меню для оптимизации распределения грузов
    print("6. Выйти из программы") # пункт меню для выхода из программы
# загрузка данных из JSON файла
def load_data(): 
    try:
        with open('data.json', 'r') as file: # пытаемся открыть файл на чтение
            data = json.load(file) # загружаем данные из файла в переменную data
    except FileNotFoundError: # если файл не найден
        data = {'clients': [], 'vehicles': []} # создаем пустой словарь для данных
    return data # возвращаем загруженные данные
# сохранение данных в JSON файл
def save_data(data):
    with open('data.json', 'w') as file: # открываем файл на запись
        json.dump(data, file, indent=4) # со# выводим заголовок для списка транспортных средствхраняем данные в файл с отступами для удобства чтения
# вывод всех записей клиентов и транспортных средств
def display_all_entries(company): 
    print("\nКлиенты:") # выводим заголовок для списка клиентов
    for client in company.clients: # проходим по всем клиентам в компании
        print(client) # выводим информацию о каждом клиенте
    print("\nТранспортные средства:") # выводим заголовок для списка транспортных средств
    for vehicle in company.vehicles: # проходим по всем транспортным средствам в компании
        print(vehicle) # выводим информацию о каждом транспортном средстве
# вывод записи по полю (например, id)
def display_entry_by_id(company, entry_type, entry_id):
    if entry_type == 'client': # если тип записи - клиент
        for idx, client in enumerate(company.clients): # проходим по всем клиентам с их индексами
            if client.name == entry_id: # если имя клиента совпадает с искомым id
                print(f"Клиент с именем {entry_id}: {client}") # выводим информацию о клиенте
                print(f"Позиция в списке: {idx}") # выводим позицию клиента в списке
                return # выходим из функции
    elif entry_type == 'vehicle': # если тип записи - транспортное средство
        for idx, vehicle in enumerate(company.vehicles): # проходим по всем транспортным средствам с их индексами
            if vehicle.vehicle_id == entry_id: # если ID транспортного средства совпадает с искомым id
                print(f"Транспортное средство с ID {entry_id}: {vehicle}") # выводим информацию о транспортном средстве
                print(f"Позиция в списке: {idx}") # выводим позицию транспортного средства в списке
                return # выходим из функции
    print("Запись не найдена") # если запись не найдена, выводим сообщение
# добавление нового клиента или транспортного средства
def add_entry(company, entry_type):
    if entry_type == 'client': # если тип записи - клиент
        name = input("Введите имя клиента: ") # запрашиваем имя клиента 
        cargo_weight = float(input("Введите вес груза: ")) # запрашиваем вес груза
        is_vip = input("VIP клиент? (да/нет): ").lower() == 'да' # запрашиваем, является ли клиент VIP
        client = Client(name, cargo_weight, is_vip) # создаем объект Client
        company.add_client(client) # добавляем клиента в компанию
    elif entry_type == 'vehicle': # если тип записи - транспортное средство
        vehicle_type = input("Тип транспортного средства (airplane/van): ").lower() # запрашиваем тип транспортного средства
        capacity = float(input("Грузоподъемность: ")) # запрашиваем грузоподъемность
        if vehicle_type == 'airplane': # запрашиваем грузоподъемность
            max_altitude = float(input("Максимальная высота полета: ")) # запрашиваем максимальную высоту полета
            vehicle = Airplane(capacity, max_altitude) # создаем объект Airplane
        elif vehicle_type == 'van': # если тип транспортного средства - фургон
            is_refrigerated = input("Наличие холодильника (да/нет): ").lower() == 'да' # запрашиваем наличие холодильника
            vehicle = Van(capacity, is_refrigerated) # создаем объект Van
        company.add_vehicle(vehicle) # добавляем транспортное средство в компанию
    save_data({'clients': [client.__dict__ for client in company.clients], # сохраняем данные клиентов в JSON
               'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]}) # сохраняем данные транспортных средств в JSON
    print(f"{entry_type.capitalize()} добавлен(а) успешно.") # выводим сообщение об успешном добавлении записи
# удаление записи по полю (например, id)
def delete_entry_by_id(company, entry_type, entry_id):
    if entry_type == 'client': # если тип записи - клиент
        for client in company.clients: # проходим по всем клиентам
            if client.name == entry_id: # если имя клиента совпадает с искомым id
                company.clients.remove(client) # удаляем клиента из списка клиентов
                save_data({'clients': [client.__dict__ for client in company.clients], # сохраняем обновленные данные клиентов в JSON
                           'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]}) # сохраняем данные транспортных средств в JSON
                print(f"Клиент с именем {entry_id} удалён.") # выводим сообщение об успешном удалении клиента
                return # выходим из функции
    elif entry_type == 'vehicle': # если тип записи - транспортное средство
        for vehicle in company.vehicles: # проходим по всем транспортным средствам
            if vehicle.vehicle_id == entry_id: # если ID транспортного средства совпадает с искомым id
                company.vehicles.remove(vehicle) # удаляем транспортное средство из списка транспортных средств
                save_data({'clients': [client.__dict__ for client in company.clients], # сохраняем данные клиентов в JSON
                           'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]}) # сохраняем обновленные данные транспортных средств в JSON
                print(f"Транспортное средство с ID {entry_id} удалено.") # выводим сообщение об успешном удалении транспортного средства
                return # выходим из функции
    print("Запись не найдена") # если запись не найдена, выводим сообщение
# основная часть программы
def main():
    data = load_data() # загружаем данные из файла JSON
    company = TransportCompany("My Transport Company") # создаем объект TransportCompany
    for client_data in data['clients']: # проходим по всем данным клиентов
        client = Client(client_data['name'], client_data['cargo_weight'], client_data['is_vip']) # создаем объекты Client
        company.add_client(client) # добавляем клиентов в компанию
    for vehicle_data in data['vehicles']: # проходим по всем данным транспортных средств
        if 'max_altitude' in vehicle_data: # если транспортное средство - самолет
            vehicle = Airplane(vehicle_data['capacity'], vehicle_data['max_altitude']) # создаем объекты Airplane
        elif 'is_refrigerated' in vehicle_data: # если транспортное средство - фургон
            vehicle = Van(vehicle_data['capacity'], vehicle_data['is_refrigerated']) # создаем объекты Van
        company.add_vehicle(vehicle) # добавляем транспортные средства в компанию
    while True: # бесконечный цикл для работы с меню
        display_menu() # выводим меню
        choice = input("Выберите пункт меню: ") # запрашиваем выбор пользователя
        if choice == '1': # если пользователь выбрал пункт 1
            display_all_entries(company) # выводим все записи
        elif choice == '2': # если пользователь выбрал пункт
            entry_type = input("Тип записи (client/vehicle): ").lower() # запрашиваем тип записи
            entry_id = input("Введите имя клиента или ID транспортного средства: ") # запрашиваем имя клиента или ID транспортного средства 
            display_entry_by_id(company, entry_type, entry_id) # выводим запись по ID
        elif choice == '3': # если пользователь выбрал пункт 3
            entry_type = input("Тип записи (client/vehicle): ").lower() # запрашиваем тип записи
            add_entry(company, entry_type) # добавляем новую запись
        elif choice == '4': # если пользователь выбрал пункт 4
            entry_type = input("Тип записи (client/vehicle): ").lower() # запрашиваем тип записи
            entry_id = input("Введите имя клиента или ID транспортного средства для удаления: ") # запрашиваем имя клиента или ID для удаления
            delete_entry_by_id(company, entry_type, entry_id) # удаляем запись по ID
        elif choice == '5': # если пользователь выбрал пункт 5
            company.optimize_cargo_distribution() # оптимизируем распределение грузов
            save_data({'clients': [client.__dict__ for client in company.clients], # сохраняем данные клиентов
                       'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]}) # сохраняем данные транспортных средств
            print("Распределение грузов оптимизировано.") # выводим сообщение об оптимизации
        elif choice == '6': # если пользователь выбрал пункт 6
            print(f"Количество операций с записями: {len(company.clients) + len(company.vehicles)}") # выводим количество операций
            break # завершаем цикл и программу
        else: 
            print("Неверный выбор. Попробуйте снова.") # выводим сообщение об ошибке выбора
if __name__ == "__main__": 
    main() # запускаем основную функцию программы