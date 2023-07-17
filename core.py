#https://github.com/duvanrg/Filtro_py.git
import json

def CreateData(*args: dict):
    if CheckData(args[0]) == False:
        with open("data/"+args[0], "w") as write_file:
            json.dump(args[1], write_file, indent = 4)
            write_file.close()
    else:
        with open("data/"+args[0], "r+") as file:
            fileData = json.load(file)
            fileData['data'].append(args[1])
            file.seek(0)
            json.dump(fileData, file, indent = 4)
            file.close()

def EditarData(*args):
    with open("data/"+args[0], "w") as write_file:
        json.dump(args[1], write_file, indent = 4)
        write_file.close()

def LoadData(FileName):
    if CheckData(FileName)== True:
        with open("data/"+FileName, "r") as read_file:
            dicc = json.load(read_file)
        return dicc

def CheckData(FileName):
    try:
        with open("data/"+FileName, "r") as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
