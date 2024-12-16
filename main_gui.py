import dearpygui.dearpygui as dpg # импортируем библиотеку dearpygui для создания графического интерфейса
import os # импортируем библиотеку os для работы с файловой системой
import json # импортируем библиотеку json для работы с json-файлами
from transport.client import Client # импортируем класс Сlient из модуля transport.client
from transport.airplane import Airplane  # импортируем класс Аirplane из модуля transport.airplane
from transport.van import Van # импортируем класс Van из модуля transport.van
from transport.transport_company import TransportCompany # импортируем класс TransportCompany из модуля transport.transport_company
from transport.vehicle import Vehicle # импортируем класс Vehicle из модуля transport.vehicle
def show_about(): # определяем функцию для отображения окна "O программе"
    if dpg.does_item_exist("about_window"): # проверяем, существует ли окно "about_window"
        return # если окно существует, выходим из функции
    # создаем модальное окно "O программе"
    with dpg.window(label = "О программе", width = 500, height = 500, modal = True, tag = "about_window"):
        dpg.add_text("Лабораторная работа 12") # добавляем текст с номером лабораторной работы
        dpg.add_text("Вариант 4") # добавляем текст с вариантом
        dpg.add_text("Разработчик: Поляк Е.В.") # добавляем текст с ФИО разработчика
        # добавляем кнопку для закрытия окна
        dpg.add_button(label = "закрыть", callback = lambda: dpg.delete_item("about_window")) 
def setup_fonts(): # определяем функцию для настройки шрифтов
    with dpg.font_registry(): # создаем реестр шрифтов
        with dpg.font("C:/Windows/Fonts/Arial.ttf", 25) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default) # добавляем подсказку диапазона шрифтов для обычного текста
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic) # добавляем подсказку диапазона шрифтов для кириллицы
            dpg.bind_font(default_font) # привязываем шрифт как основной
# глобальная переменная для хранения данных
company = TransportCompany("My Transport Company") # создаем объект компании TransportCompany
# функции для обновления таблиц
def update_clients_table(): # определяем функцию для обновления таблицы клиентов
    dpg.delete_item("clients_table", children_only = True) # удаляем все элементы таблицы клиентов, кроме её самой 
    for client in company.clients: # проходим по всем клиентам в компании
        with dpg.table_row(parent = "clients_table"): 
            dpg.add_text(client.name) # добавляем строку в таблицу клиентов
            dpg.add_text(str(client.cargo_weight)) # добавляем текст с весом груза клиента
            dpg.add_text("да" if client.is_vip else "нет") # добавляем текст с информацией о vip-статусе клиента
def update_vehicles_table(): # определяем функцию для обновления таблицы транспортных средств
    dpg.delete_item("vehicles_table", children_only = True) # удаляем все элементы таблицы транспортных средств, кроме её самой
    for vehicle in company.vehicles: # проходим по всем транспортным средствам в компании
        # добавляем строку в таблицу транспортных средств
        with dpg.table_row(parent = "vehicles_table"): 
            dpg.add_text(str(vehicle.vehicle_id)) # добавляем текст с id транспортного средства
            dpg.add_text(str(vehicle.capacity)) # добавляем текст с грузоподъемностью транспортного средства
            dpg.add_text(str(vehicle.current_load)) # добавляем текст с текущей загрузкой транспортного средства
            if isinstance(vehicle, Airplane): # если транспортное средство - самолет
                dpg.add_text(f"Высота: {vehicle.flight_height}") # добавляем текст с высотой полета самолета
            elif isinstance(vehicle, Van): # если транспортное средство - фургон
                dpg.add_text(f"Холодильник: {"да" if vehicle.is_refrigerated else "нет"}") # добавляем текст с информацией о наличии холодильника в фургоне
# функции для вывода транспортных средств и клиентов
def show_all_clients(): # функция для отображения всех клиентов
    if dpg.does_item_exist("all_clients_window"): # проверяем, существует ли окно "all_clients_window"
        return # если окно существует, выходим из функции
    # создаем модальное окно "Все клиенты"
    with dpg.window(label="Все клиенты", modal = True, width = 600, height = 400, tag = "all_clients_window"):
        # создаем таблицу с заголовком 
        with dpg.table(header_row = True):
            dpg.add_table_column(label = "Имя клиента") # добавляем столбец "Имя клиента"
            dpg.add_table_column(label = "Вес груза") # добавляем столбец "Вес груза"
            dpg.add_table_column(label = "VIP статус") # добавляем столбец "VIP статус"
            for client in company.clients: # проходим по всем клиентам в компании
                with dpg.table_row(): # добавляем строку в таблицу клиентов
                    dpg.add_text(client.name) # добавляем текст с именем клиента
                    dpg.add_text(str(client.cargo_weight)) # добавляем текст с весом груза клиента
                    dpg.add_text("да" if client.is_vip else "нет") # добавляем текст с информацией о vip-статусе клиента
        dpg.add_button(label="закрыть", callback = lambda: dpg.delete_item("all_clients_window")) # добавляем кнопку для закрытия окна
def show_all_vehicles(): # функция для отображения всех транспортных средств
    if dpg.does_item_exist("all_vehicles_window"): # проверяем, существует ли окно "all_vehicles_window"
        return # если окно существует, выходим из функции
    # создаем модальное окно "Все транспортные средства"
    with dpg.window(label="Все транспортные средства", modal = True, width = 850, height = 800, tag = "all_vehicles_window"):
        # создаем таблицу с заголовком
        with dpg.table(header_row = True):
            dpg.add_table_column(label = "ID") # добавляем столбец "ID"
            dpg.add_table_column(label = "Грузоподъемность") # добавляем столбец "Грузоподъемность"
            dpg.add_table_column(label = "Текущая загрузка") # добавляем столбец "Текущая загрузка"
            dpg.add_table_column(label = "Особенности") # добавляем столбец "Особенности"
            for vehicle in company.vehicles: # проходим по всем транспортным средствам в компании
                with dpg.table_row(): # добавляем строку в таблицу транспортных средств
                    dpg.add_text(str(vehicle.vehicle_id))  # ID транспортного средства
                    dpg.add_text(str(vehicle.capacity))  # Грузоподъемность
                    dpg.add_text(str(vehicle.current_load))  # Текущая загрузка
                    if isinstance(vehicle, Airplane): # если транспортное средство - самолет
                        dpg.add_text(f"Высота: {vehicle.flight_height}") # добавляем текст с высотой полета самолета
                    elif isinstance(vehicle, Van): # если транспортное средство - фургон
                        dpg.add_text(f"Холодильник: {"да" if vehicle.is_refrigerated else "нет"}") # добавляем текст с информацией о наличии холодильника в фургоне
        dpg.add_button(label = "закрыть", callback = lambda: dpg.delete_item("all_vehicles_window")) # добавляем кнопку для закрытия окна
def show_vip_clients(): # функция для отображения vip клиентов
    if dpg.does_item_exist("vip_clients_window"): # проверяем, существует ли окно "vip_clients_window"
        return # если окно существует, выходим из функции
    # создаем модальное окно "VIP клиенты"
    with dpg.window(label = "VIP клиенты", modal = True, width = 600, height = 400, tag = "vip_clients_window"):
        # создаем таблицу с заголовком
        with dpg.table(header_row = True):
            dpg.add_table_column(label = "Имя клиента") # добавляем столбец "Имя клиента"
            dpg.add_table_column(label = "Вес груза") # добавляем столбец "Вес груза"
            for client in filter(lambda c: c.is_vip, company.clients): # фильтруем клиентов, оставляя только vip клиентов
                with dpg.table_row(): # добавляем строку в таблицу клиентов
                    dpg.add_text(client.name) # добавляем текст с именем клиента
                    dpg.add_text(str(client.cargo_weight)) # добавляем текст с весом груза клиента
        dpg.add_button(label = "закрыть", callback = lambda: dpg.delete_item("vip_clients_window")) # добавляем кнопку для закрытия окна
def show_loaded_vehicles(): # функция для отображения загруженных транспортных средств
    # проверка, существует ли окно с загруженными транспортными средствами
    if dpg.does_item_exist("loaded_vehicles_window"): 
        print("Существует окно с загруженными транспортными средствами.") # вывод сообщения, если окно существует
        return # выход из функции
    # проверка, есть ли транспортные средства с загрузкой больше нуля
    loaded_vehicles = list(filter(lambda v: v.current_load > 0, company.vehicles))
    if not loaded_vehicles: # если нет загруженных транспортных средств
        print("Нет загруженных транспортных средств.") # вывод сообщения об этом
        return # выход из функции
    # создание окна для отображения загруженных транспортных средств
    with dpg.window(label = "Загруженные транспортные средства", modal = True, width = 600, height = 400, tag = "loaded_vehicles_window"):
        # создание таблицы с заголовком
        with dpg.table(header_row = True):
            dpg.add_table_column(label = "ID") # добавление столбца для ID транспортного средства
            dpg.add_table_column(label = "Грузоподъемность") # добавление столбца для грузоподъемности
            dpg.add_table_column(label = "Текущая загрузка") # добавление столбца для текущей загрузки
            dpg.add_table_column(label = "Особенности") # добавление столбца для особенностей
            # добавляем загруженные транспортные средства в таблицу
            for vehicle in loaded_vehicles:
                with dpg.table_row(): # создание строки для каждого транспортного средства
                    dpg.add_text(str(vehicle.vehicle_id))  # ID транспортного средства
                    dpg.add_text(str(vehicle.capacity))  # Грузоподъемность
                    dpg.add_text(str(vehicle.current_load))  # Текущая загрузка
                    # проверка типа транспортного средства
                    if isinstance(vehicle, Airplane): # если транспортное средство - самолет
                        dpg.add_text(f"Высота: {vehicle.flight_height}")  # вывод высоты для самолета
                    elif isinstance(vehicle, Van): # если транспортное средство - фургон
                        dpg.add_text(f"Холодильник: {"да" if vehicle.is_refrigerated else "нет"}")  # вывод информации о наличии холодильника для фургона
        dpg.add_button(label = "закрыть", callback = lambda: dpg.delete_item("loaded_vehicles_window")) # добавление кнопки для закрытия окна
    print("Создано окно с загруженными транспортными средствами.") # вывод сообщения о создании окна
def show_client_form():  # функция для отображения формы добавления клиента
    if dpg.does_item_exist("client_form"):  # проверка, существует ли уже форма "client_form"
        return  # если форма существует, выходим из функции
    # создание окна для добавления клиента
    with dpg.window(label = "Добавить клиента", width = 500, height = 500, modal = True, tag = "client_form"):
        dpg.add_text("Имя клиента: ")  # добавляем текстовое поле "Имя клиента"
        dpg.add_input_text(tag = "client_name", width = 250)  # добавляем поле ввода текста для имени клиента
        dpg.add_text("Вес груза: ")  # добавляем текстовое поле "Вес груза"
        dpg.add_input_text(tag = "client_cargo_weight", width = 250)  # добавляем поле ввода текста для веса груза
        dpg.add_text("VIP статус: ")  # добавляем текстовое поле "VIP статус"
        dpg.add_checkbox(tag = "client_is_vip")  # добавляем чекбокс для VIP статуса
        dpg.add_button(label = "сохранить", callback = save_client)  # добавляем кнопку "сохранить" с обратным вызовом функции save_client
        dpg.add_button(label = "отмена", callback = lambda: dpg.delete_item("client_form"))  # добавляем кнопку "отмена" с обратным вызовом для удаления формы
def save_client():  # функция для сохранения данных клиента
    name = dpg.get_value("client_name")  # получение значения имени клиента из поля ввода
    cargo_weight = dpg.get_value("client_cargo_weight")  # получение значения веса груза из поля ввода
    is_vip = dpg.get_value("client_is_vip")  # получение значения vip-статуса из чекбокса
    # проверка, что имя не пустое, вес груза является числом и больше 0
    if name and cargo_weight.isdigit() and int(cargo_weight) > 0:
        client = Client(name, int(cargo_weight), is_vip)  # создание объекта клиента
        company.add_client(client)  # добавление клиента в компанию
        update_clients_table()  # обновление таблицы клиентов
        dpg.delete_item("client_form")  # удаление формы добавления клиента
    else:
        # установка значения статуса с сообщением об ошибке
        dpg.set_value("status", "Ошибка: Проверьте введённые данные!")
def show_vehicle_form():  # функция для отображения формы добавления транспортного средства
    if dpg.does_item_exist("vehicle_form"):  # проверка, существует ли уже форма "vehicle_form"
        return  # если форма существует, выходим из функции
    # создание окна для добавления транспортного средства
    with dpg.window(label = "Добавить транспорт", width = 400, height = 300, modal = True, tag = "vehicle_form"):
        dpg.add_text("Тип транспорта: ")  # добавляем текстовое поле "Тип транспорта"
        dpg.add_combo(["Самолет", "Фургон"], tag = "vehicle_type", width = 250, callback = toggle_vehicle_specific_fields)  # добавляем выпадающий список для выбора типа транспорта
        dpg.add_text("Грузоподъемность (в тоннах): ")  # добавляем текстовое поле "Грузоподъемность (в тоннах)"
        dpg.add_input_text(tag = "vehicle_capacity", width = 250)  # добавляем поле ввода текста для грузоподъемности
        dpg.add_text("Введите высоту полёта: ", tag = "flight_height_label", show = False)  # добавляем текстовое поле "Введите высоту полёта" (скрытое по умолчанию)
        dpg.add_input_text(tag = "flight_height", width = 250, show = False)  # добавляем поле ввода текста для высоты полёта (скрытое по умолчанию)
        dpg.add_text("Есть ли холодильник: ", tag = "refrigerator_label", show = False)  # добавляем текстовое поле "Есть ли холодильник" (скрытое по умолчанию)
        dpg.add_checkbox(tag = "refrigerator", show = False)  # добавляем чекбокс для холодильника (скрытое по умолчанию)
        dpg.add_button(label = "сохранить", callback = save_vehicle)  # добавляем кнопку "сохранить" с обратным вызовом функции save_vehicle
        dpg.add_button(label = "отмена", callback = lambda: dpg.delete_item("vehicle_form"))  # добавляем кнопку "отмена" с обратным вызовом для удаления формы
def toggle_vehicle_specific_fields(sender, app_data):  # функция для переключения отображения полей, специфичных для транспортного средства
    if app_data == "Самолет":  # если выбран тип транспорта "Самолет"
        dpg.configure_item("flight_height_label", show = True)  # показываем метку "Введите высоту полёта"
        dpg.configure_item("flight_height", show = True)  # показываем поле ввода "flight_height"
        dpg.configure_item("refrigerator_label", show = False)  # скрываем метку "Есть ли холодильник"
        dpg.configure_item("refrigerator", show = False)  # скрываем чекбокс "refrigerator"
    elif app_data == "Фургон":  # если выбран тип транспорта "Фургон"
        dpg.configure_item("flight_height_label", show = False)  # скрываем метку "Введите высоту полёта"
        dpg.configure_item("flight_height", show = False)  # скрываем поле ввода "flight_height"
        dpg.configure_item("refrigerator_label", show = True)  # показываем метку "Есть ли холодильник"
        dpg.configure_item("refrigerator", show = True)  # показываем чекбокс "refrigerator"
def save_vehicle():  # функция для сохранения данных транспортного средства
    vehicle_type = dpg.get_value("vehicle_type")  # получение значения типа транспорта из выпадающего списка
    capacity = dpg.get_value("vehicle_capacity")  # получение значения грузоподъемности из поля ввода
    # проверка, что грузоподъемность является числом и больше 0
    if capacity.isdigit() and int(capacity) > 0:
        capacity = int(capacity)  # преобразование грузоподъемности в целое число
        if vehicle_type == "Самолет":  # если выбран тип транспорта "Самолет"
            flight_height = dpg.get_value("flight_height")  # получение значения высоты полёта из поля ввода
            # проверка, что высота полёта является числом и больше 0
            if flight_height.isdigit() and int(flight_height) > 0:
                vehicle = Airplane(capacity, int(flight_height))  # создание объекта самолета с переданной высотой полёта
            else:
                dpg.set_value("status", "Ошибка: Проверьте высоту полёта!")  # установка значения статуса с сообщением об ошибке
                return  # выход из функции
        elif vehicle_type == "Фургон":  # если выбран тип транспорта "Фургон"
            has_refrigerator = dpg.get_value("refrigerator")  # получение значения наличия холодильника из чекбокса
            vehicle = Van(capacity, has_refrigerator)  # создание объекта фургона с переданным значением холодильника
        else:
            vehicle = Vehicle(capacity)  # создание объекта транспортного средства по умолчанию (грузовик)
        company.add_vehicle(vehicle)  # добавление транспортного средства в компанию
        update_vehicles_table()  # обновление таблицы транспортных средств
        dpg.delete_item("vehicle_form")  # закрытие формы добавления транспортного средства
    else:
        dpg.set_value("status", "Ошибка: Проверьте введённые данные!")  # установка значения статуса с сообщением об ошибке
def show_authorized_clients():  # функция для отображения VIP клиентов
    # проверка существования окна
    if dpg.does_item_exist("clients_window"):  # проверка, существует ли уже окно "clients_window"
        return  # если окно существует, выходим из функции
    # создаем окно с VIP клиентами
    with dpg.window(label = "VIP клиенты", modal = True, width = 600, height = 400, tag = "clients_window"):
        # добавляем таблицу с данными
        with dpg.table(header_row = True):  # создаем таблицу с заголовком
            dpg.add_table_column(label = "Имя клиента")  # добавляем столбец "Имя клиента"
            dpg.add_table_column(label = "Вес груза")  # добавляем столбец "Вес груза"
            dpg.add_table_column(label = "VIP статус")  # добавляем столбец "VIP статус"
            for client in filter(lambda c: c.is_vip, company.clients):  # проходим по всем VIP клиентам в компании
                with dpg.table_row():  # добавляем строку в таблицу клиентов
                    dpg.add_text(client.name)  # добавляем текст с именем клиента
                    dpg.add_text(str(client.cargo_weight))  # добавляем текст с весом груза клиента
                    dpg.add_text("да")  # добавляем текст с информацией о VIP статусе клиента
        # кнопка для закрытия окна
        dpg.add_button(label = "закрыть", callback = lambda: dpg.delete_item("clients_window"))  # добавляем кнопку для закрытия окна
def authorize_vehicle(vehicle):  # функция для авторизации транспортного средства
    vehicle.is_authorized = True  # например, авторизуем транспортное средство
def export_results():  # функция для экспорта результатов
    data = {  # создаем словарь с данными клиентов и транспортных средств
        "clients": [{"name": c.name, "cargo_weight": c.cargo_weight, "is_vip": c.is_vip} for c in company.clients],  # добавляем данные клиентов
        "vehicles": [  # добавляем данные транспортных средств
            {
                "vehicle_id": v.vehicle_id,  # id транспортного средства
                "capacity": v.capacity,  # грузоподъемность транспортного средства
                "current_load": v.current_load,  # текущая загрузка транспортного средства
                "type": "Airplane" if isinstance(v, Airplane) else "Van" if isinstance(v, Van) else "Truck",  # тип транспортного средства
                "details": {  # дополнительные детали транспортного средства
                    "flight_height": getattr(v, 'flight_height', None),  # высота полета для самолета (если применимо)
                    "has_refrigerator": getattr(v, 'has_refrigerator', None)  # наличие холодильника для фургона (если применимо)
                }
            } for v in company.vehicles
        ]
    }
    with open("export.json", "w", encoding = "utf-8") as file:  # открываем файл для записи данных
        json.dump(data, file, ensure_ascii = False, indent = 4)  # записываем данные в файл в формате json
    dpg.set_value("status", "Результаты экспортированы в файл export.json.")  # обновляем значение статуса с сообщением об успешном экспорте
def distribute_cargo():  # функция для распределения груза
    company.distribute_cargo()  # вызов метода distribute_cargo() для распределения груза в компании
    update_vehicles_table()  # обновление таблицы транспортных средств
    dpg.set_value("status", "Грузы успешно распределены!")  # обновление значения статуса с сообщением об успешном распределении груза
def distribute_cargo_results():  # функция для отображения результатов распределения груза
    # проверяем, существует ли уже окно с результатами распределения
    if dpg.does_item_exist("cargo_distribution_window"):  # проверка, существует ли окно "cargo_distribution_window"
        return  # если окно существует, выходим из функции
    # создаем окно для отображения результатов
    with dpg.window(label = "Распределение груза", modal = True, width = 1000, height = 800, tag = "cargo_distribution_window"):
        # создаем таблицу для отображения результатов
        with dpg.table(header_row = True):  # создаем таблицу с заголовком
            dpg.add_table_column(label = "Транспортное средство")  # добавляем столбец "Транспортное средство"
            dpg.add_table_column(label = "Грузоподъемность")  # добавляем столбец "Грузоподъемность"
            dpg.add_table_column(label = "Текущий груз")  # добавляем столбец "Текущий груз"
            dpg.add_table_column(label = "Распределенный груз")  # добавляем столбец "Распределенный груз"
            # пример распределения груза: для каждого транспортного средства
            for vehicle in company.vehicles:  # проходим по всем транспортным средствам в компании
                # пример распределения груза
                distributed_cargo = vehicle.current_load  # здесь вы можете взять данные из своей логики распределения
                with dpg.table_row():  # создаем строку в таблице
                    dpg.add_text(vehicle.vehicle_id)  # идентификатор транспортного средства
                    dpg.add_text(str(vehicle.capacity))  # грузоподъемность
                    dpg.add_text(str(vehicle.current_load))  # текущий груз
                    dpg.add_text(str(distributed_cargo))  # распределенный груз
        # кнопка для закрытия окна
        dpg.add_button(label = "закрыть", callback = lambda: dpg.delete_item("cargo_distribution_window"))  # добавляем кнопку для закрытия окна
def distribute_cargo():  # функция для распределения груза
    company.distribute_cargo()  # вызываем метод для распределения грузов
    update_vehicles_table()  # обновляем таблицу с транспортными средствами
    dpg.set_value("status", "Грузы успешно распределены!")  # обновляем значение статуса с сообщением об успешном распределении грузов
def setup_global_key_handlers():  # функция для настройки глобальных обработчиков клавиш
    # настройка глобальных обработчиков клавиш для всех окон
    def handle_escape():  # функция для обработки нажатия клавиши escape
        # закрытие всех открытых окон
        open_windows = [  # список всех окон, которые нужно закрыть
            "client_form",
            "vehicle_form",
            "clients_window",
            "all_vehicles_window",
            "about_window",
            "all_clients_window",
            "cargo_distribution_window",
        ]
        for window in open_windows:  # проходим по каждому окну в списке
            if dpg.does_item_exist(window):  # проверяем, существует ли окно
                dpg.delete_item(window)  # удаляем окно
    def handle_enter():  # функция для обработки нажатия клавиши Enter
        # сохранение данных в активной форме
        if dpg.does_item_exist("client_form"):  # если существует форма "client_form"
            save_client()  # сохраняем данные клиента
        elif dpg.does_item_exist("vehicle_form"):  # если существует форма "vehicle_form"
            save_vehicle()  # сохраняем данные транспортного средства
        else:
            print("Нет активной формы для сохранения.")  # вывод сообщения об отсутствии активной формы для сохранения
    # глобальная регистрация обработчиков
    with dpg.handler_registry():  # создание реестра обработчиков
        dpg.add_key_down_handler(key = dpg.mvKey_Escape, callback = lambda: handle_escape())  # добавляем обработчик нажатия клавиши Escape для закрытия окон
        dpg.add_key_down_handler(key = dpg.mvKey_Return, callback = lambda: handle_enter())  # добавляем обработчик нажатия клавиши Enter для сохранения данных
def main_window():  # функция для создания основного окна приложения
    with dpg.window(label = "Основное окно", width = 1000, height = 1000):  # создаем окно с заданной шириной и высотой
        dpg.add_button(label = "О программе", callback = show_about)  # добавляем кнопку "О программе" с обратным вызовом функции show_about
        with dpg.group(horizontal = True):  # создаем горизонтальную группу для размещения элементов
            # клиенты
            with dpg.group():  # создаем группу для клиентов
                dpg.add_text("Клиенты", tag = "clients_text")  # добавляем текст "Клиенты"
                dpg.add_button(label = "Добавить клиента", callback = show_client_form)  # добавляем кнопку "Добавить клиента" с обратным вызовом функции show_client_form
                dpg.add_button(label = "Все клиенты", callback = show_all_clients)  # добавляем кнопку "Все клиенты" с обратным вызовом функции show_all_clients
                dpg.add_button(label = "VIP клиенты", callback = show_authorized_clients)  # добавляем кнопку "VIP клиентЫ" с обратным вызовом функции show_authorized_clients
            # транспортные средства
            with dpg.group():  # создаем группу для транспортных средств
                dpg.add_text("Транспортные средства", tag = "vehicles_text")  # добавляем текст "Транспортные средства"
                dpg.add_button(label = "Добавить транспорт", callback = show_vehicle_form)  # добавляем кнопку "Добавить транспорт" с обратным вызовом функции show_vehicle_form
                dpg.add_button(label = "Распределить грузы", callback = distribute_cargo)  # добавляем кнопку "Распределить грузы" с обратным вызовом функции distribute_cargo
                dpg.add_button(label = "Все транспортные средства", callback = show_all_vehicles)  # добавляем кнопку "Все транспортные средства" с обратным вызовом функции show_all_vehicles
                dpg.add_button(label = "Результат распределения", callback = distribute_cargo_results)  # добавляем кнопку "Результат распределения" с обратным вызовом функции distribute_cargo_results
                dpg.add_button(label = "Экспортировать результат", callback = export_results)  # добавляем кнопку "Экспортировать результат" с обратным вызовом функции export_results
        dpg.add_text("", tag = "status")  # добавляем текстовое поле для отображения статуса
# запуск приложения
dpg.create_context()  # создаем контекст dearpygui
setup_fonts()  # настраиваем шрифты
main_window()  # создаем основное окно
# настройка обработчиков клавиш
setup_global_key_handlers()  # настраиваем глобальные обработчики клавиш
dpg.create_viewport(title = "My Transport Company", width = 800, height = 600)  # создаем видовой экран с заголовком и заданными размерами
dpg.setup_dearpygui()  # настраиваем dearpygui
dpg.show_viewport()  # отображаем видовой экран
dpg.start_dearpygui()  # запускаем dearpygui
dpg.destroy_context()  # уничтожаем контекст dearpygui