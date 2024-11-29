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
    if entry_type == 'client':
        for idx, client in enumerate(company.clients):
            if client.name == entry_id:
                print(f"Клиент с именем {entry_id}: {client}")
                print(f"Позиция в списке: {idx}")
                return
    elif entry_type == 'vehicle':
        for idx, vehicle in enumerate(company.vehicles):
            if vehicle.vehicle_id == entry_id:
                print(f"Транспортное средство с ID {entry_id}: {vehicle}")
                print(f"Позиция в списке: {idx}")
                return
    print("Запись не найдена")
# добавление нового клиента или транспортного средства
def add_entry(company, entry_type):
    if entry_type == 'client':
        name = input("Введите имя клиента: ")
        cargo_weight = float(input("Введите вес груза: "))
        is_vip = input("VIP клиент? (да/нет): ").lower() == 'да'
        client = Client(name, cargo_weight, is_vip)
        company.add_client(client)
    elif entry_type == 'vehicle':
        vehicle_type = input("Тип транспортного средства (airplane/van): ").lower()
        capacity = float(input("Грузоподъемность: "))
        if vehicle_type == 'airplane':
            max_altitude = float(input("Максимальная высота полета: "))
            vehicle = Airplane(capacity, max_altitude)
        elif vehicle_type == 'van':
            is_refrigerated = input("Наличие холодильника (да/нет): ").lower() == 'да'
            vehicle = Van(capacity, is_refrigerated)
        company.add_vehicle(vehicle)
    save_data({'clients': [client.__dict__ for client in company.clients],
               'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]})
    print(f"{entry_type.capitalize()} добавлен(а) успешно.")
# удаление записи по полю (например, id)
def delete_entry_by_id(company, entry_type, entry_id):
    if entry_type == 'client':
        for client in company.clients:
            if client.name == entry_id:
                company.clients.remove(client)
                save_data({'clients': [client.__dict__ for client in company.clients],
                           'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]})
                print(f"Клиент с именем {entry_id} удалён.")
                return
    elif entry_type == 'vehicle':
        for vehicle in company.vehicles:
            if vehicle.vehicle_id == entry_id:
                company.vehicles.remove(vehicle)
                save_data({'clients': [client.__dict__ for client in company.clients],
                           'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]})
                print(f"Транспортное средство с ID {entry_id} удалено.")
                return
    print("Запись не найдена")
# основная часть программы
def main():
    data = load_data()
    company = TransportCompany("My Transport Company")
    for client_data in data['clients']:
        client = Client(client_data['name'], client_data['cargo_weight'], client_data['is_vip'])
        company.add_client(client)
    for vehicle_data in data['vehicles']:
        if 'max_altitude' in vehicle_data:
            vehicle = Airplane(vehicle_data['capacity'], vehicle_data['max_altitude'])
        elif 'is_refrigerated' in vehicle_data:
            vehicle = Van(vehicle_data['capacity'], vehicle_data['is_refrigerated'])
        company.add_vehicle(vehicle)
    while True:
        display_menu()
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            display_all_entries(company)
        elif choice == '2':
            entry_type = input("Тип записи (client/vehicle): ").lower()
            entry_id = input("Введите имя клиента или ID транспортного средства: ")
            display_entry_by_id(company, entry_type, entry_id)
        elif choice == '3':
            entry_type = input("Тип записи (client/vehicle): ").lower()
            add_entry(company, entry_type)
        elif choice == '4':
            entry_type = input("Тип записи (client/vehicle): ").lower()
            entry_id = input("Введите имя клиента или ID транспортного средства для удаления: ")
            delete_entry_by_id(company, entry_type, entry_id)
        elif choice == '5':
            company.optimize_cargo_distribution()
            save_data({'clients': [client.__dict__ for client in company.clients],
                       'vehicles': [vehicle.__dict__ for vehicle in company.vehicles]})
            print("Распределение грузов оптимизировано.")
        elif choice == '6':
            print(f"Количество операций с записями: {len(company.clients) + len(company.vehicles)}")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
if __name__ == "__main__":
    main()