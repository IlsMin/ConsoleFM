import sys
import os
import platform
import shutil

#from .. Lesson4 import use_functions
#import use_functions


menu_points = {  1 : "создать папку",
                 2 : "удалить (файл/папку)",
                 3 : "копировать (файл/папку)",
                 4 : "просмотр содержимого рабочей директории",
                 5 : "посмотреть только папки",
                 6 : "посмотреть только файлы",
                 7 : "просмотр информации об операционной системе",
                 8 : "создатель программы",
                 9 : "играть в викторину",
                10 : "мой банковский счет",
                11 : "смена рабочей директории",
                12 : "выход"
               }
def getDirName(prompt):
    path = input(prompt+ "? : ")
    return (os.path.exists(path), path)

def show_file_or_dir(only_dir):
    files = os.listdir(os.getcwd())
    rez = []
    for file in files:
        print (file, os.path.isfile(os.path.join(os.getcwd(), file)))
        if (os.path.isfile(os.path.join(os.getcwd(), file)) != only_dir):
           rez.append(file)
    print( rez)

def check_sys_path(path):
    fullpath = os.path.join( os.getcwd(), path)
    if( fullpath not in sys.path):
        sys.path.append(fullpath)
    #print (sys.path)
                

if sys.version_info.major < 3 or sys.version_info.minor < 10:
    print ("Внимание! Этот код исплользует оператор match и,\nследовательно, требует версию Питона не ниже 3.10")
    exit

# этот код не содержит блоков try !!!

choice =0
while(12 != choice):
    print('---')
    for (num, text) in menu_points.items(): 
        print(f'{num}\t: {text}')
    print('---')
    choice = int(input("Введите номер пункта меню: "))
    print (f"выбран пункт '{menu_points[choice]}'")

    if(9 == choice):
        check_sys_path("../Lesson3")
        import  victory
        victory.run_victory()
        continue
    if(10 == choice):
        check_sys_path("../Lesson4")
        import use_functions   
        use_functions.run_bank()
        continue 

    match choice:
        case 1:
            exists, path = getDirName("Имя создаваемой папки")
            if(not exists):
                os.mkdir(path)
            else: print(" такой каталог/файл уже существует")
            
        case 11:
            exists, path = getDirName("Имя директории")
            if(exists):
                os.chdi(path)
            else: print(" такой каталог не существует")

        case 2:
             exists, path = getDirName("Имя удаляемой папки/файла")
             fullname = os.path.join( os.getcwd(),path)
             if(not exists):
                 print("Нет такой папки/файла: ", fullname)
             else:
                #shutil.move()
                if (os.path.isfile(fullname)):
                    os.remove( fullname)
                else: os.rmdir(fullname)

        case 3:
            exists, path = getDirName("Имя копируемой папки/файла")
            if(not exists):
                 print("Нет такой папки/файла: ", os.path.join( os.getcwd(),path))
                 continue
            exists, dest = getDirName("Имя новой папки/файла")
            if( exists):
                 print(" такой каталог/файл уже существует", os.getcwd() + dest)
                 continue
            else:   shutil.copy(path, dest)
                
        case 4: print(os.listdir())
        case 5: show_file_or_dir(True);
        case 6: show_file_or_dir(False); 
        case 7: print ( sys.platform,  sys.version) #, sys.version_info)
        case 8: print ("Ильсур Мингараев (при содействии УИИ)")

        case _: print ("  Не существующий пункт меню")
