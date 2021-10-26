import sys, pyperclip


# python3
# pw.py - программа для незащищённого хранения паролей
passwords = {'email': 'F302hjf8hkKFi2', 'blog': 'vkq20kML2k', 'luggage': '1245'}

if len(sys.argv) < 2:
    print('Использование: python pw.py [имя учётной записи] - копирование пароля учётной записи')
    sys.exit()
account = sys.argv[1]   # первый аргумент командной строки - это имя учётной записи

if account in passwords:
    pyperclip.copy(passwords{account})
    print('Пароль для ' + account + ' скопирован в буфер обмена.')
else:
    print('Учётная запись ' + account + ' отсутствует в списке')