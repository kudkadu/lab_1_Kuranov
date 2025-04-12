# main.py

# Простые структуры для хранения данных (в реальном приложении нужна БД!)
customers = []
cars = []
repair_jobs = []
job_id_counter = 1

def add_customer():
    print("\n--- Добавление нового клиента ---")
    name = input("Имя клиента: ")
    phone = input("Телефон клиента: ")
    customer = {"id": len(customers) + 1, "name": name, "phone": phone}
    customers.append(customer)
    print(f"Клиент '{name}' успешно добавлен с ID {customer['id']}.")
    return customer['id']

def add_car():
    prdfghjklint("\n--- Добавление нового автомобиля ---")
    make = input("Марка: ")
    model = input("Модель: ")
    year = input("Год выпуска: ")
    vin = input("VIN: ")
    owner_id = int(input("ID владельца (клиента): "))

    # Проверка, существует ли клиент
    if any(c['id'] == owner_id for c in customers):
        car = {"id": len(cars) + 1, "make": make, "model": model, "year": year, "vin": vin, "owner_id": owner_id}
        cars.append(car)
        print(f"Автомобиль '{make} {model}' (VIN: {vin}) успешно добавлен с ID {car['id']}.")
        return car['id']
    else:
        print(f"Ошибка: Клиент с ID {owner_id} не найден.")
        return None

def add_repair_job():
    global job_id_counter
    print("\n--- Добавление нового заказа на ремонт ---")
    car_id = int(input("ID автомобиля для ремонта: "))
    description = input("Описание работ: ")
    status = "Новый" # Статусы: Новый, В работе, Завершен, Отменен

    # Проверка, существует ли автомобиль
    if any(c['id'] == car_id for c in cars):
        job = {"id": job_id_counter, "car_id": car_id, "description": description, "status": status}
        repair_jobs.append(job)
        job_id_counter += 1
        print(f"Заказ на ремонт ID {job['id']} для автомобиля ID {car_id} успешно создан.")
        return job['id']
    else:
        print(f"Ошибка: Автомобиль с ID {car_id} не найден.")
        return None

def view_jobs():
    print("\n--- Список заказов на ремонт ---")
    if not repair_jobs:
        print("Заказов пока нет.")
        return

    for job in repair_jobs:
        # Найдем информацию об авто и владельце для полноты картины
        car_info = next((c for c in cars if c['id'] == job['car_id']), None)
        owner_info = None
        if car_info:
             owner_info = next((cust for cust in customers if cust['id'] == car_info['owner_id']), None)

        print(f"ID Заказа: {job['id']}")
        if car_info:
             print(f"  Авто: {car_info['make']} {car_info['model']} (VIN: {car_info['vin']})")
        if owner_info:
             print(f"  Владелец: {owner_info['name']} (Тел: {owner_info['phone']})")
        print(f"  Описание: {job['description']}")
        print(f"  Статус: {job['status']}")
        print("-" * 20)

# Простой текстовый интерфейс
def main_menu():
    while True:
        print("\n--- Главное меню Автомастерской ---")
        print("1. Добавить клиента")
        print("2. Добавить автомобиль")
        print("3. Добавить заказ на ремонт")
        print("4. Просмотреть все заказы")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            add_car()
        elif choice == '3':
            add_repair_job()
        elif choice == '4':
            view_jobs()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

# Запуск главного меню
if __name__ == "__main__":
    # Добавим несколько тестовых данных для начала
    customers.append({"id": 1, "name": "Иван Петров", "phone": "123-45-67"})
    cars.append({"id": 1, "make": "Toyota", "model": "Camry", "year": "2020", "vin": "VIN001", "owner_id": 1})
    print("Тестовые данные загружены.")

    main_menu()