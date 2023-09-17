#Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных и поиска по фамилии.


def poisk(sername):
    lines = f.readlines()
    if line in lines: 
        if sername in line:
            print(line)


def izmenenie():
    with open ('text.txt', 'r') as f:
        old_data = f.read()
        sern1 = input("Введите фамилию, которую нужно изменить: ")
        sern2 = input("Введите фамилию, на какую меняем: ")
        new_data = old_data.replace(sern1, sern2)

    with open ('test.txt', 'w') as f:
        f.write(new_data)
        
def udalenie(sername):
    lines = f.readlines()
    if line in lines: 
        if sername in line:
            f = f.replace(line,'')
            
n = int(input(''' Для изменения данных справочника нажмите 1.
                  Для удаления данных справочника нажмите 2.
                  Для поиска по фамилии нажмите 3.'''))

f = open('text.txt', 'r+')

if n == 1:
    izmenenie()
elif n == 2:
    sername = input("Введите искомую фамилию: ")
    udalenie(sername)
else:
    sername = input("Введите искомую фамилию: ")
    poisk(sername)
 
f.close()      