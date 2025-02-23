import mysql.connector as db # https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html
import customtkinter as ctk # https://customtkinter.tomschimansky.com/documentation/
from dotenv import dotenv_values # https://pypi.org/project/python-dotenv/
import psutil # https://psutil.readthedocs.io/en/latest/
import math

class Monitoracao(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('PLCVision Monitoring System')
        self.geometry('900x500')
        ctk.set_appearance_mode('dark')

        # TODO self._variaveis_env = dotenv_values('.env')

        # self._conexao_db = db.connect(
        #     host=self._variaveis_env['DB_HOST'],
        #     port=self._variaveis_env['DB_PORT'],
        #     user=self._variaveis_env['DB_USER'],
        #     password=self._variaveis_env['DB_PASSWORD']
        # )

        self._dados_limites = {
            'temperatura_cpu': {
                'ok': 40,
                'mediano': 55,
                'atencao': 70
            },
            'uso_cpu': {
                'ok': 40,
                'mediano': 55,
                'atencao': 70
            },
            'atividade_cpu': {
                'ok': 700, # quase 2 anos
                'mediano': 2000, # 5,4 anos
                'atencao': 3200 # 8,7 anos
            },
            'uso_ram': {
                'ok': 40,
                'mediano': 55,
                'atencao': 70
            },
            'memoria_livre': {
                'ok': 10,
                'mediano': 5,
                'atencao': 3
            },
            'giro_fan': {
                'ok': 3000,                
                'mediano': 1200,
                'atencao': 500
            }
        }

        self._id_plc = 1
        
        # Configuração da sidebar
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar.pack(side='left', fill='y', padx=10, pady=10)
        
        self.titulo_sidebar = ctk.CTkLabel(self.sidebar, text='Configuração', font=('Arial', 16, 'bold'))
        self.titulo_sidebar.pack(pady=10)

        # CPU
        self.subtitulo_sidebar = ctk.CTkLabel(self.sidebar, text='CPU', font=('Arial', 14, 'bold'))
        self.subtitulo_sidebar.pack(pady=10)
        
        self.temperatura = ctk.BooleanVar()
        self.temperatura_cpu = ctk.CTkCheckBox(self.sidebar, text='Temperatura', variable=self.temperatura, command=self.atualizar_infos)
        self.temperatura_cpu.pack(anchor='w', padx=10, pady=5)

        self.uso = ctk.BooleanVar()
        self.uso_cpu = ctk.CTkCheckBox(self.sidebar, text='Uso', variable=self.uso, command=self.atualizar_infos)
        self.uso_cpu.pack(anchor='w', padx=10, pady=5)

        self.atividade = ctk.BooleanVar()
        self.tempo_atividade_cpu = ctk.CTkCheckBox(self.sidebar, text='Tempo de Atividade', variable=self.atividade, command=self.atualizar_infos)
        self.tempo_atividade_cpu.pack(anchor='w', padx=10, pady=5)
        
        # RAM
        self.subtitulo_sidebar = ctk.CTkLabel(self.sidebar, text='RAM', font=('Arial', 14, 'bold'))
        self.subtitulo_sidebar.pack(pady=10)

        self.uso_memoria = ctk.BooleanVar()
        self.uso_ram = ctk.CTkCheckBox(self.sidebar, text='Uso', variable=self.uso_memoria, command=self.atualizar_infos)
        self.uso_ram.pack(anchor='w', padx=10, pady=5)

        self.livre = ctk.BooleanVar()
        self.ram_livre = ctk.CTkCheckBox(self.sidebar, text='Memória Livre', variable=self.livre, command=self.atualizar_infos)
        self.ram_livre.pack(anchor='w', padx=10, pady=5)

        # Ventuinha
        self.subtitulo_sidebar = ctk.CTkLabel(self.sidebar, text='Ventuinha', font=('Arial', 14, 'bold'))
        self.subtitulo_sidebar.pack(pady=10)

        self.fan = ctk.BooleanVar()
        self.fan_ventilacao = ctk.CTkCheckBox(self.sidebar, text='Velocidade de Giro', variable=self.fan, command=self.atualizar_infos)
        self.fan_ventilacao.pack(anchor='w', padx=10, pady=5)
        
        # Área de exibição
        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.pack(expand=True, fill='both', padx=0, pady=10)
        
        self.atualizar_infos()

    def armazenar_dados(self, dados):
        colunas = ''
        valores = ''

        for dado in dados:
            for i, valor in enumerate(dado):
                is_ultima = i == len(dado) - 1
                colunas += f'{valor['nome_coluna']}{',' if not is_ultima else ''}'
                valores += f'{valor['dado']}{',' if not is_ultima else ''}'
        
        # TODO executor = self._conexao_db.cursor()  
        query = f'INSERT INTO dados.informacoes(fkPlc,{colunas}) VALUES ({self._id_plc}, {valores});'

        print(query)
        # executor.execute(query)
        # self._conexao_db.commit()
        # executor.close()
    
    def status_cor(self, value, limites, is_decrescente):
        if is_decrescente:
            if value < limites['atencao']:
                return '#6e0101'
            elif limites['atencao'] >= value < limites['mediano']:
                return '#994202'
            elif limites['mediano'] >= value < limites['ok']:
                return '#8a8706'
            else:
                return '#04590c'
        else: 
            if value > limites['atencao']:
                return '#6e0101'
            elif limites['atencao'] <= value > limites['mediano']:
                return '#994202'
            elif limites['mediano'] <= value > limites['ok']:
                return '#8a8706'
            else:
                return '#04590c'

    def verificar_cpu(self):
        index_coluna = 0
        dados = []

        if self.temperatura.get() or self.uso.get() or self.atividade.get():
            self.titulo_cpu = ctk.CTkLabel(self.display_frame, text='CPU', font=('Arial', 20, 'bold'))
            self.titulo_cpu.grid(row=0, column=index_coluna, padx=100, pady=10)

        if self.temperatura.get():
            temperatura = psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0].current # só no Linux
            cor = self.status_cor(temperatura, self._dados_limites['temperatura_cpu'], False)
            dados.append({'nome_coluna': 'temperaturaCpu', 'dado': temperatura})

            label = ctk.CTkLabel(self.display_frame, text=f'Temperatura: {temperatura}°C', fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=2, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.uso.get():
            uso = psutil.cpu_percent(interval = None, percpu = False)
            cor = self.status_cor(uso, self._dados_limites['uso_cpu'], False)
            dados.append({'nome_coluna': 'usoCpu', 'dado': uso})

            label = ctk.CTkLabel(self.display_frame, text=f'Uso: {uso}%', fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=2, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.atividade.get():
            atividade = math.trunc((((psutil.cpu_times(percpu = False).user / 60 ** 2) / 24) * (10 **2))) / (10 ** 2)
            cor = self.status_cor(atividade, self._dados_limites['atividade_cpu'], False)
            dados.append({'nome_coluna': 'atividadeCpu', 'dado': atividade})

            label = ctk.CTkLabel(self.display_frame, text=f'Tempo de Atividade: {atividade} {'dia' if atividade <= 1 else 'dias'}', fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=2, column=index_coluna, padx=10, pady=10)
            index_coluna += 1

        return dados

    def verificar_ram(self):
        index_coluna = 0
        dados = []

        if self.uso_memoria.get() or self.livre.get():
            self.titulo_ram = ctk.CTkLabel(self.display_frame, text='RAM', font=('Arial', 20, 'bold'))
            self.titulo_ram.grid(row=5, column=index_coluna, padx=0, pady=10)
        
        if self.uso_memoria.get():
            uso = psutil.virtual_memory().percent
            cor = self.status_cor(uso, self._dados_limites['uso_ram'], False)
            dados.append({'nome_coluna': 'usoMemoriaRam', 'dado': uso})

            label = ctk.CTkLabel(self.display_frame, text=f'Uso: {uso}%', fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=7, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.livre.get():
            livre = math.trunc(psutil.virtual_memory().free/(1024**3))
            cor = self.status_cor(livre, self._dados_limites['memoria_livre'], True)
            dados.append({'nome_coluna': 'memoriaRamLivre', 'dado': livre})

            label = ctk.CTkLabel(self.display_frame, text=f'Memória Livre: {livre} {'GiB' if livre <= 1 else 'GiBs'}', fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=7, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        return dados
    
    def verificar_fan(self):
        index_coluna = 0

        dados = []

        if self.fan.get():
            self.titulo_ventuinha = ctk.CTkLabel(self.display_frame, text='RAM', font=('Arial', 20, 'bold'))
            self.titulo_ventuinha.grid(row=10, column=index_coluna, padx=0, pady=10)

            fan = psutil.sensors_fans() # TODO fazer teste com as possíveis fans
            cor = self.status_cor(fan, self._dados_limites['giros_fan'], True)
            dados.append({'nome_coluna': 'velcidadeGiroVentuinha', 'dado': fan})

            label = ctk.CTkLabel(self.display_frame, text=f'Velocidade de Giro: {fan} RPM', fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=12, column=index_coluna, padx=10, pady=10)
            index_coluna += 1

        return dados
           
    def atualizar_infos(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        is_info_armazenar = False
        dados = []

        dados_cpu = self.verificar_cpu()
        dados_ram = self.verificar_ram()
        dados_fan = self.verificar_fan()

        if len(dados_cpu) != 0 or len(dados_ram) != 0 or len(dados_fan) != 0:
            is_info_armazenar = True
        
        if is_info_armazenar:
            dados.append(dados_cpu + dados_ram + dados_fan)
            self.armazenar_dados(dados)
        
        self.after(5000, self.atualizar_infos) # 5 sec

if __name__ == '__main__':
    app = Monitoracao()
    app.mainloop()