import json  # Импортируем модуль json для работы с JSON файлами

def employees_rewrite(sort_type):
    # Список допустимых ключей для сортировки
    valid_keys = ['firstname', 'lastname', 'department', 'salary']

    # Проверяем, что переданный ключ для сортировки находится в списке допустимых
    if sort_type.lower() not in valid_keys:
        raise ValueError('Bad key for sorting')  # Вызываем исключение, если ключ недопустим

    # Открываем файл employees.json для чтения
    with open('employees.json', 'r') as file:
        data = json.load(file)  # Загружаем данные из JSON файла
        employees = data['employees']  # Получаем список сотрудников из данных

        sorted_employees = []  # Создаем пустой список для отсортированных сотрудников
        for employee in employees:
            if sort_type in employee:  # Проверяем, есть ли ключ для сортировки у текущего сотрудника
                sorted_employees.append(employee)  # Добавляем сотрудника в список для сортировки

        # Сортируем список отсортированных сотрудников по выбранному ключу
        if sort_type.lower() == 'salary':
            sorted_employees.sort(key=lambda x: x[sort_type], reverse=True)  # Сортировка по убыванию для зарплаты
        else:
            sorted_employees.sort(key=lambda x: x[sort_type])  # Сортировка по возрастанию для других ключей

    output_filename = f'employees_{sort_type.lower()}_sorted.json'  # Формируем имя выходного файла
    with open(output_filename, 'w') as output_file:
        json.dump({'employees': sorted_employees}, output_file, indent=4)  # Записываем отсортированных сотрудников в новый JSON файл

# Пример вызова функции для сортировки по фамилии, имени, отделу и зарплате
employees_rewrite('firstName')
employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('salary')
