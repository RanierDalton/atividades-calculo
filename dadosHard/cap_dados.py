import psutil # https://psutil.readthedocs.io/en/latest/
import time
import math
import mysql.connector as db # importando a lib
    
def armazenar_dados(minutos_parados, porcentagem_cpu):
    banco = db.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='password'
    )
    
    executor = banco.cursor()
    query = f'INSERT INTO dados.informacoes(minutosParados, porcentagemCPU) VALUES ({minutos_parados}, {porcentagem_cpu});'

    executor.execute(query)
    banco.commit()
    executor.close()

def captar_dados():
    while True:
        # Conteúdos cpu 
        porcentagem_uso_cpu = psutil.cpu_percent(interval = None, percpu = False)

        tempo_ativo_cpu = math.trunc(psutil.cpu_times(percpu = False).user / 60)

        # temperatura_cpu = psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0].current

        # Conteúdos RAM
        porcentagem_uso_ram = psutil.virtual_memory().percent

        memoria_ram_usada = math.trunc(psutil.virtual_memory().used/(1024**3))

        memoria_ram_total = math.trunc(psutil.virtual_memory().total/(1024**3))

        armazenar_dados(cpu_user_time, cpu_usage_percentage) # todo

        time.sleep(30)

if __name__ == '__main__':
    captar_dados()
