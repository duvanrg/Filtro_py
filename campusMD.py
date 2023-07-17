import complements as comp
import core
import os

diccCitas = {"data":[]}

def clearbar():
    os.system('clear' if os.name == 'posix' else 'cls')

def LoadDataCitas(args):
    global diccCitas
    if core.CheckData(args):
        return core.LoadData(args)
    else:
        diccCitas["data"] = core.CreateData(args, diccCitas)
        return core.LoadData(args)
    
def AddCita():
    print('+','-'*56,"+")
    print('|{:^58}|'.format('AGREGAR CITA'))
    print('+','-'*56,"+")
    print('|{:^58}|'.format('Ingrese los datos del Paciente'))
    print('+','-'*56,"+")
    nombre = str(input("Nombre: ")).title()
    fecha = comp.VerifyDate(str(input("Fecha(dd/mm/aaaa): ")))
    if(fecha == False):
        print("Fecha no valida")
        return False
    hora = comp.VerefyHour(str(input("Hora (hh:mm): ")))
    if(hora == False):
        print("Hora no valida")
        return False
    motivo = str(input("Motivo: ")).capitalize()
    data = {
        "Nombre": nombre,
        "Fecha": fecha,
        "Hora": hora,
        "Motivo": motivo
    }
    core.CreateData("Citas.json", data)

def SearchCita():
    diccCitas = LoadDataCitas("Citas.json")
    save = []
    cont = 1
    if len(diccCitas["data"]) >=1:
        print('+','-'*56,"+")
        print('|{:^58}|'.format('AGREGAR CITA'))
        print('+','-'*56,"+")
        print('{:^58}'.format('\nSeleccione el dato a buscar del paciente'))
        print('+','-'*36,"+")
        for key in diccCitas["data"][0]:
            if key != "Hora":
                print('|{:^5}|{:^32}|'.format(cont, key))
                print('+','-'*36,"+")
                cont += 1
                save.append(key)
        select = save[int(input("> "))-1]
        if select != "Fecha":
            search = str(input(f"ingrese {select}: ")).title()
        else:
            search = comp.VerifyDate(str(input("Fecha(dd/mm/aaaa): ")))
            if(search == False):
                print("Fecha no valida")
                return False
        clearbar()
        cont = 1
        band = 1
        for i, item in enumerate(diccCitas["data"]):
            if item[select] == search:   
                print('\n+','-'*56,"+")
                print('|{:^58}|'.format(f'PACIENTE {cont}'))
                print('+','-'*56,"+")
                for key in diccCitas["data"][0]:
                    if (key == "Motivo") and (len(item[key])>50):
                        if band == 1:
                            print('+','-'*56,"+")
                            print('|{:^58}|'.format(key))
                            print('+','-'*56,"+")
                            band = 0
                        modi = item[key].split(' ')

                        for c in range(0, len(modi), 6):
                            n = ' '
                            text = modi[c:c+6]
                            print('|{:^58}|'.format(n.join(text)))
                        print('+','-'*56,"+")
                    else:
                        print('|{:^8}|{:^49}|'.format(key, item[key]))
                        print('+','-'*56,"+")
                cont += 1
    else:
        print('+','-'*56,"+")   
        print('|{:^58}|'.format('NO EXISTEN CITAS'))
        print('+','-'*56,"+")  

def EditCita():
    diccCitas = LoadDataCitas("Citas.json")
    edit = True
    save = []
    if len(diccCitas["data"]) >=1:
        print('+','-'*68,"+")
        print('|{:^70}|'.format('EDITAR CITA'))
        print('+','-'*68,"+")
        print('|{:^5}|{:^15}|{:^10}|{:^7}|{:^29}|'.format("nro","Nombre","Fecha","Hora","Motivo"))
        print('+','-'*68,"+")
        for i, item in enumerate(diccCitas["data"]):
            if (len(item["Motivo"])>26):
                modi = item["Motivo"].split(' ')
                for c in range(0, len(modi), 4):
                    n = ' '
                    t = modi[c:c+4]
                    motivo = n.join(t)
                    motivo += "..."
                    break
                    
                print('|{:^5}|{:^15}|{:^10}|{:^7}|{:^29}|'.format(i+1, item["Nombre"], item["Fecha"], item["Hora"],motivo))
                print('+','-'*68,"+")
            else:
                print('|{:^5}|{:^15}|{:^10}|{:^7}|{:^29}|'.format(i+1, item["Nombre"], item["Fecha"], item["Hora"], item["Motivo"]))
                print('+','-'*68,"+")
        print('|{:^70}|'.format('Ingrese el numero(nro) del paciente'))
        print('+','-'*68,"+")
        search = diccCitas["data"][int(input("> "))-1]
        clearbar()
        while edit:
            os.system("clear")
            cont = 1
            print('+','-'*46,"+")
            print('|{:^48}|'.format('SELECCIONE EL DATO A EDITAR'))
            print('+','-'*46,"+")
            for key, data in search.items():
                print('|{:^5}|{:^22}|{:^19}|'.format(cont, key, data))
                print('+','-'*46,"+")
                cont += 1
                save.append(key)
            print('|{:^48}|'.format('Ingrese el numero(nro) del dato'))
            print('+','-'*46,"+")
            select = save[int(input("> "))-1] 
            os.system("clear")
            print('+','-'*46,"+")
            print('|{:^48}|'.format(f'EDITANDO {select.upper()}'))
            print('+','-'*46,"+")
            if select == "Fecha":
                var = comp.VerifyDate(str(input("nueva Fecha(dd/mm/aaaa): ")))
                if(var == False):
                    print("Fecha no valida")
                    return False
            elif select == "Hora":
                var = comp.VerefyHour(str(input("nueva Hora (hh:mm): ")))
                if(var == False):
                    print("Hora no valida")
                    return False
            else:
                var = str(input(f"nuevo {select}: ")).title()
            diccCitas["data"][diccCitas["data"].index(search)][select] = var
            print("¿Desea modificar otro dato?","1. Si","2. No",sep="\n")
            if (int(input("> "))==2) or select == False:
                edit = False
        core.EditarData("Citas.json",diccCitas)
    else:
        print('+','-'*56,"+")   
        print('|{:^58}|'.format('NO EXISTEN CITAS'))
        print('+','-'*56,"+")     
        
def CancelCita():
    diccCitas = LoadDataCitas("Citas.json")
    save = []
    if len(diccCitas["data"]) >=1:
        print('+','-'*68,"+")
        print('|{:^70}|'.format('CANCELAR CITA'))
        print('+','-'*68,"+")
        print('|{:^5}|{:^15}|{:^10}|{:^7}|{:^29}|'.format("nro","Nombre","Fecha","Hora","Motivo"))
        print('+','-'*68,"+")
        for i, item in enumerate(diccCitas["data"]):
            if (len(item["Motivo"])>26):
                modi = item["Motivo"].split(' ')
                for c in range(0, len(modi), 4):
                    n = ' '
                    t = modi[c:c+4]
                    motivo = n.join(t)
                    motivo += "..."
                    break
                    
                print('|{:^5}|{:^15}|{:^10}|{:^7}|{:^29}|'.format(i+1, item["Nombre"], item["Fecha"], item["Hora"],motivo))
                print('+','-'*68,"+")
            else:
                print('|{:^5}|{:^15}|{:^10}|{:^7}|{:^29}|'.format(i+1, item["Nombre"], item["Fecha"], item["Hora"], item["Motivo"]))
                print('+','-'*68,"+")
        print('|{:^70}|'.format('Ingrese el numero(nro) del paciente'))
        print('+','-'*68,"+")
        search = diccCitas["data"][int(input("> "))-1]
        clearbar()
        print('+','-'*66,"+")
        print('|{:^68}|'.format('DATOS DE PACIENTE'))
        print('+','-'*66,"+")
        for key, data in search.items():
                print('|{:^22}|{:^25}|'.format(key, data))
                print('+','-'*46,"+")
        print("¿Confirma la cancelacion de la cita?","1. Si","2. No",sep="\n")
        if (int(input("> "))==1):
            diccCitas["data"].remove(search)
            core.EditarData("Citas.json",diccCitas)
    else:
        print('+','-'*56,"+")   
        print('|{:^58}|'.format('NO EXISTEN CITAS'))
        print('+','-'*56,"+") 

if __name__ == '__main__':
    opc = 0
    run = True
    menu = ["Agregar Cita","Buscar Cita","Modificar Cita","Cancelar Cita","Salir"]
    while run:
        try:
            clearbar()
            print('+','-'*36,"+")
            print('|{:^38}|'.format('MENU CITAS CAMPUSMD'))
            print('+','-'*36,"+")
            for i, item in enumerate(menu):
                print('|{:^5}|{:^32}|'.format(i+1, item))
                print('+','-'*36,"+")
            opc = int(input("> "))
            clearbar()
            if opc == 1:
                AddCita()
            elif opc == 2:
                SearchCita()
            elif opc == 3:
                EditCita()
            elif opc == 4:
                CancelCita()            
            elif opc == 5:
                print("⠀╭ ◜◝ ͡ ◝ ͡ ◜◝╮","(  Saliendo  )","╰ ͜ ⠀ ͜   ͜   ͜  ╯","        O","         o","         °","〃∩ _∧＿∧_♡","  |('・ω・）♡"," ¨ヽ_っ＿/￣￣￣/","　    ＼/＿＿＿/",sep="\n")
                run = False
            else:
                print('+','-'*36,"+")
                print('|{:^38}|'.format('valor no valido'))
                print('+','-'*36,"+")        
        except ValueError:
            print("Error, ingrese El valor correcto")
        except IndexError as e:
            print("Se produjo un error: ",e)
        else:
            input("presione Enter para continuar...")
    