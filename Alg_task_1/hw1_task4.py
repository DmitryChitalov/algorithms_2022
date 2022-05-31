storage = {'Kirill': ['1234sd', False], 'Adam': ['143ses', True],
           'Mike': ['12345cf', False], 'Sam': ['987665ae', False],
           'Alex': ['123459qw', True], 'Clark': ['989898sde', False]}


def check_auth(lib: dict, name):
    if lib[name][1] == 1:
        print('Пользователь уже активирован')
    else:
        print('Пользователь еще не активирован. Пройдите активацию')


def check_auth_sec(lib: dict, name):
    for key, values in lib.items():
        if key == name:
            if values[1] == 1:
                print('Пользователь уже активирован')
            else:
                print('Пользователь еще не активирован. Пройдите активацию')


check_auth(storage, 'Kirill')
check_auth(storage, 'Adam')
check_auth_sec(storage, 'Adam')
