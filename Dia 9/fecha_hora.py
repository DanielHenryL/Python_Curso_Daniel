import datetime

# Ejercicio 2: Tiempo despierto
despierta = datetime.datetime(2022, 11, 9, 7, 30, 0)
duerme = datetime.datetime(2022, 11, 9, 22, 30, 20)
vigilia = duerme - despierta
print(vigilia.seconds)


print('\n')
# ejercicio 1: edad actual
nacimiento = datetime.date(1997, 3, 27).year
actual = datetime.date(2022, 11, 9).year
edad_actual = actual - nacimiento
print(edad_actual)


print('\n')
# fecha y hora
mi_hora_fecha = datetime.datetime(2025, 3, 27, 5, 39, 40)
print(mi_hora_fecha)
mi_hora_fecha = mi_hora_fecha.replace(month=10)
print(mi_hora_fecha)

print('\n')
# fecha(date)
mi_fecha = datetime.date(2025, 3, 27)
print(mi_fecha)
print(mi_fecha.year)
print(mi_fecha.month)
print(mi_fecha.day)
print(mi_fecha.ctime())
print(mi_fecha.today())


print('\n')
# hora(time)
mi_hora = datetime.time(14, 16, 25, 2000)
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)
print(mi_hora.second)
print(mi_hora.microsecond)
print(mi_hora.fold)

