import psutil 

print(psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0].current)