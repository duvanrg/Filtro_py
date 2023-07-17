import os

def VerifyDate(date):
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]
    try:
        info = date.split('/')
        if len(info)!= 3:
            return False
        if not info[0].isdigit():
            return False
        if not info[1].isdigit():
            return False
        if not info[2].isdigit():
            return False
        if int(info[1])==2:
            if int(info[2])%4 != 0:
                if int(info[2])%100 != 0:
                    if int(info[2])%400!= 0:
                        if int(info[0]) < 1 or int(info[0]) > 29:
                            return False
                if int(info[2])%4 != 0 and int(info[2])%100!= 0:
                    if int(info[0]) < 1 or int(info[0]) > 28:
                        return False
        elif int(info[1]) in days31:
            if int(info[0]) < 1 or int(info[0]) > 31:
                return False
        elif int(info[1]) in days30:
            if int(info[0]) < 1 or int(info[0]) > 30:
                return False        
        if int(info[1]) < 1 or int(info[1]) > 12:
            return False
        if int(info[2]) < 1900 or int(info[2]) > 2099:
            return False
    except Exception as e:
        print("Error al ingresar la fecha", e)
        return False
    return date

def VerefyHour(hour):
    try:
        info = hour.split(':')
        if len(info)!= 2:
            return False
        if not info[0].isdigit():
            return False
        if not info[1].isdigit():
            return False
        if int(info[0]) > 23:
            return False
        if int(info[1]) > 59:
            return False
    except Exception as e:
        print("Error al ingresar la hora", e)
        return False
    return hour