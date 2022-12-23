import time
n = int(input('Введите количество секунд: '))
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Time in transform format :-", time_format)
