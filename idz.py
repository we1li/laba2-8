import sys

list_route = []
spisok_new = []

def add_route():
    name_start = input('Начало маршрута: ')
    name_finish = input('Конец маршрута: ')
    num_route_get = input('Номер маршрута: ')

    num_route = int(num_route_get)

    if type(num_route) != int:
        print("Введенные данные не верны!")

    list_route_new = {
        'name_start': name_start,
        'name_finish': name_finish,
        'num_route': num_route
    }

    list_route.append(list_route_new)

    if len(list_route) > 1:
        list_route.sort(key=lambda item: item.get('num_route', ''))

def print_routes():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 15,
        '-' * 30,
        '-' * 20
    )

    print(line)
    print(
        '| {:^4} | {:^15} | {:^30} | {:^20} | '.format(
            "№",
            "Начало маршрута",
            "Конец маршрута",
            "№ Маршрута"
        )
    )
    print(line)

    for idx, spisok_new in enumerate(list_route, 1):
        print(
            '| {:>4} | {:<15} | {:<30} | {:<20} | '.format(
                idx,
                spisok_new.get('name_start', ''),
                spisok_new.get('name_finish', ''),
                spisok_new.get('num_route', 0)
            )
        )

    print(line)

def search_route():
    route_sear = input('Введите пункт маршрута: ')
    search_route = []
    for route_sear_itme in list_route:
        if route_sear == route_sear_itme['name_start']:
            search_route.append(route_sear_itme)
        if route_sear == route_sear_itme['name_finish']:
            search_route.append(route_sear_itme)

    if len(search_route) > 0:
        line_new = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 15,
                '-' * 30,
                '-' * 20
            )
        print(line_new)

        print(
                '| {:^4} | {:^15} | {:^30} | {:^20} | '.format(
                    "№",
                    "Начало маршрута",
                    "Конец маршрута",
                    "№ Маршрута"
                )
            )
        print(line_new)

        for idx_new, spisok_new_new in enumerate(search_route, 1):
            print(
                '| {:>4} | {:<15} | {:<30} | {:<20} | '.format(
                    idx_new,
                    spisok_new_new.get('name_start', ''),
                    spisok_new_new.get('name_finish', ''),
                    spisok_new_new.get('num_route', '')
                )
            )

        print(line_new)
    else:
        print('Таких маршрутов не найдено', file=sys.stderr)

def show_help():
    print('Список команд:\n')
    print('add - добавить маршрут.')
    print('list - вывести список маршрутов.')
    print('route <Пункуты маршрутов> - запросить Начало или конечные пункты маршрутов.')
    print('help - Справочник.')
    print('exit - Завершить работу программы.')

def main():
    while True:
        command = input('>>> ').lower()

        if command == 'exit':
            break

        elif command == 'add':
            add_route()

        elif command == 'list':
            print_routes()

        elif command == 'route':
            search_route()

        elif command == 'help':
            show_help()

        else:
            print(f'Команда <{command}> не существует.', file=sys.stderr)
            print('Введите <help> для просмотра доступных команд')

if __name__ == "__main__":
    main()
