import os
import sys
import win32api
import winreg
import shutil
from datetime import datetime

result = win32api.MessageBox(None,"Orginizar as fotos?", "Organazier",1)

def folder_path_from_photo_date(file):
    date = photo_shorting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')   

def photo_shorting_date(file):
    date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

def move_photo(file):
    new_folder = folder_path_from_photo_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.move(file,new_folder + '/' + file)

if result == 1:
    listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
    print(listOfFiles)
    for numero in listOfFiles:
        move_photo(numero)
elif result == 2:
    exit()




print("Fim")
