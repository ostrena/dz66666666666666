import os

import argparse

if __name__ == "__main__":
    print("Здравствуйте!")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-n", "--name", default="люди!", help='имя пользователя')
    parser.add_argument("-a", '--age', default=0, help='введите возраст')
    parser.add_argument("-p", '--path', default=r"C:\Users\Алиса\ро", help='путь к файлу')
    path = os.getcwd()
    args = parser.parse_args()
    file = open(args.path, 'a')
    print(f'привет {args.name}!')
    print(args)
    try:
        file.write('name- ' + args.name + '\n')
    file.write('age- ' + (str(args.age)) + '\n')
    file.write('path- ' + args.path + '\n')
    finally:
    file.close()
else:
    print("файл запущен не напрямую")
