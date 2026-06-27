# sahur system - [1] / v-1.0 / 25.06.2026

import os, time, datetime 

print("sahur system - [1] / v-1.0 / 25.06.2026"), time.sleep(1)
print(" [1]-System : Запуск \n"), time.sleep(1)
print(" [2]-System : Проверка систем (1) "), time.sleep(0.3)
print(" [3]-System : Проверка систем (2) "), time.sleep(1)

# os.system('cls'),time.sleep(1)

log = open('sahur-system-[1]/database.txt','r')
last_log = log.read()
print("последняя сессия :", last_log)

log = open('sahur-system-[1]/database.txt','w')
a = str(str(datetime.datetime.now())[:-10])
log.write(a)
log.close()

log = open('sahur-system-[1]/database.txt','r')
last_log = log.read()
print("текущая сессия   :", last_log)

time.sleep(1)

def menu():
  print("Добро пожаловать!"), time.sleep(1)
  while True:
    print("╭──────────────╮"), time.sleep(0.1)
    print("│ главное меню │"), time.sleep(0.1)
    print("│──────────────│"), time.sleep(0.1)
    print("│[1] -  Старт  │"), time.sleep(0.1)
    print("│[2] -         │"), time.sleep(0.1)
    print("│[3] -  Выйти  │"), time.sleep(0.1)
    print('╰──────────────╯'), time.sleep(0.5)
    de = input(' >> ')
    if de == '1':
        print('Запуск'), time.sleep(1), os.system('cls')
        os.startfile('D:/Program Files/Telegram Desktop/Telegram.exe'), time.sleep(1)
        os.startfile('C:/Happ/Happ/Happ.exe'), time.sleep(1)
        os.startfile('C:/Program Files/Yandex/YandexTelemost/YandexTelemost.exe'), time.sleep(1)
        os.startfile('C:/Program Files/Mozilla Firefox/firefox.exe')

        os.system('cls')
        continue
    elif de == '2':
        print('2'), time.sleep(1)
        os.system('cls')
        continue
    elif de == '3':
        print("До свидания!"), time.sleep(1)
        break
    else: 
       os.system('cls')
       continue


def error():
   print("\033[0;31;40m ошибка \033[0m\n"), time.sleep(1)

def critical_error():
    print("\033[1;31;40m [!] критическая ошибка \033[0m\n"), time.sleep(1)
    de = input('$ ')
    
#error()
#critical_error()
menu()

log = open('sahur-system-[1]/database.txt','w')
a = str(str(datetime.datetime.now())[:-10])
log.write(a)
log.close()

print("\033[0;33;40m [ℹ]-System : stop \033[0m\n"), time.sleep(1)
exit()