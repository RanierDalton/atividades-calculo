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
        # Cada atributo representa os segundos que a CPU gastou no modo determinado.
        cpu_user_time = math.trunc(psutil.cpu_times(percpu = False).user / 60)
        # print(f'Sua CPU ficou {cpu_user_time:.0f} minutos parados')

        cpu_usage_percentage = math.trunc(psutil.cpu_percent(interval=None))
        # print(f'Você está utilizando {cpu_usage_percentage:.2f}% da sua CPU')

        armazenar_dados(cpu_user_time, cpu_usage_percentage)

        '''
        percentage_memory = psutil.virtual_memory().percent
        free_memory_ram = math.trunc(psutil.virtual_memory().free/(1024**3)) + math.trunc(psutil.virtual_memory().inactive/(1024**3))
        print(f'Você está utilizando {percentage_memory:.2f}% da sua RAM')
        print(f'Você tem {free_memory_ram}GiB de memória sobrando da sua RAM')

        used_disk_percentage = psutil.disk_usage('/').percent
        free_memory_disk = math.trunc(psutil.disk_usage('/').free/(1024**3))
        print(f'Você está utilizando {used_disk_percentage:.2f}% do seu Disco Rígido')
        print(f'Você tem {free_memory_disk}GiB de memória sobrando do seu Disco Rígido')
        '''
        time.sleep(30)

'''
# utilização atual da CPU
    cpu_usage = psutil.cpu_percent(interval = None, percpu = False)

    # número de CPUs lógicas no sistema
    cpu_count = psutil.cpu_count(logical=False)

    # frequência da CPU como um nome duplo
    cpu_hz = psutil.cpu_freq()

    # Disoc e Memória
    psutil.disk_partitions()

    # Retorna estatísticas de uso de disco sobre a partição que contém o caminho dado
    # print(psutil.disk_usage('/').total/1024**2) # Megas

    # print(psutil. disk_partitions(all = True))
    # print(psutil.virtual_memory().total/(1024**3)) # Gigas
    # print(psutil.swap_memory().total / 1024**3)
'''   
if __name__ == '__main__':
    captar_dados()
