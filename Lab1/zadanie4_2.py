import datetime

urodziny = datetime.datetime(2000, 9, 15)
roznica = datetime.datetime.now() - urodziny
print(roznica.total_seconds())



print((datetime.datetime.now() - datetime.datetime(2000, 9, 15)).total_seconds())