import customtkinter as ctk # https://customtkinter.tomschimansky.com/documentation/
import psutil # https://psutil.readthedocs.io/en/latest/
import math

# TODO Integrar com banco de dados

class Monitoracao(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PLCVision Monitoring System")
        self.geometry("900x500")
        ctk.set_appearance_mode("dark")
        
        # Configuração da sidebar
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        
        self.titulo_sidebar = ctk.CTkLabel(self.sidebar, text="Configuração", font=("Arial", 16, "bold"))
        self.titulo_sidebar.pack(pady=10)

        # CPU
        self.subtitulo_sidebar = ctk.CTkLabel(self.sidebar, text="CPU", font=("Arial", 13, "bold"))
        self.subtitulo_sidebar.pack(pady=10)
        
        self.temperatura = ctk.BooleanVar()
        self.temperatura_cpu = ctk.CTkCheckBox(self.sidebar, text="Temperatura", variable=self.temperatura, command=self.atualizar_infos)
        self.temperatura_cpu.pack(anchor="w", padx=10, pady=5)

        self.uso = ctk.BooleanVar()
        self.uso_cpu = ctk.CTkCheckBox(self.sidebar, text="Uso", variable=self.uso, command=self.atualizar_infos)
        self.uso_cpu.pack(anchor="w", padx=10, pady=5)

        self.atividade = ctk.BooleanVar()
        self.tempo_atividade_cpu = ctk.CTkCheckBox(self.sidebar, text="Tempo de Atividade", variable=self.atividade, command=self.atualizar_infos)
        self.tempo_atividade_cpu.pack(anchor="w", padx=10, pady=5)

        self.cache = ctk.BooleanVar()
        self.cache_cpu = ctk.CTkCheckBox(self.sidebar, text="Memória Cache", variable=self.cache, command=self.atualizar_infos)
        self.cache_cpu.pack(anchor="w", padx=10, pady=5)
        
        # RAM
        self.subtitulo_sidebar = ctk.CTkLabel(self.sidebar, text="RAM", font=("Arial", 13, "bold"))
        self.subtitulo_sidebar.pack(pady=10)

        self.uso_memoria = ctk.BooleanVar()
        self.uso_ram = ctk.CTkCheckBox(self.sidebar, text="Uso", variable=self.uso_memoria, command=self.atualizar_infos)
        self.uso_ram.pack(anchor="w", padx=10, pady=5)

        self.livre = ctk.BooleanVar()
        self.ram_livre = ctk.CTkCheckBox(self.sidebar, text="Uso", variable=self.livre, command=self.atualizar_infos)
        self.ram_livre.pack(anchor="w", padx=10, pady=5)

        # Ventuinha
        self.subtitulo_sidebar = ctk.CTkLabel(self.sidebar, text="Ventuinha", font=("Arial", 13, "bold"))
        self.subtitulo_sidebar.pack(pady=10)

        self.fan = ctk.BooleanVar()
        self.fan_ventilacao = ctk.CTkCheckBox(self.sidebar, text="Velocidade de Giro", variable=self.fan, command=self.atualizar_infos)
        self.fan_ventilacao.pack(anchor="w", padx=10, pady=5)
        
        # Área de exibição
        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.info_labels = {}
        self.atualizar_infos()
    
    def status_cor(self, value, thresholds):
        if value <= thresholds["ok"]:
            return "#04590c"  # Verde
        elif value <= thresholds["medium"]:
            return "#8a8706"  # Amarelo
        elif value <= thresholds["attention"]:
            return "#994202"  # Laranja
        else:
            return "#6e0101"  # Vermelho
    
    def atualizar_infos(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        index_coluna = 0
        
        if self.temperatura.get():
            temperatura = psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0].current # só no Linux
            cor = self.status_cor(temperatura, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Temperatura CPU: {temperatura}°C", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=0, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.uso.get():
            uso = psutil.cpu_percent(interval = None, percpu = False)
            cor = self.status_cor(uso, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Uso CPU: {uso}%", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=0, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.atividade.get():
            atividade = math.trunc(psutil.cpu_times(percpu = False).user / 60)
            cor = self.status_cor(atividade, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Tempo de Atividade CPU: {atividade}", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=0, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.cache.get():
            cache = psutil.virtual_memory().cached  
            cor = self.status_cor(cache, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Memória Cache CPU: {cache}%", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=0, column=index_coluna, padx=10, pady=10)
            index_coluna += 1

        index_coluna = 0
        
        if self.uso_memoria.get():
            uso = psutil.virtual_memory().percent
            cor = self.status_cor(uso, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Uso RAM: {uso}%", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=5, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        if self.livre.get():
            livre = math.trunc(psutil.virtual_memory().free/(1024**3))
            cor = self.status_cor(livre, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Memória Livre: {livre}", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=5, column=index_coluna, padx=10, pady=10)
            index_coluna += 1

        index_coluna = 0

        if self.fan.get():
            fan = psutil.sensors_fans()
            cor = self.status_cor(fan, {"ok": 40, "medium": 55, "attention": 70}) # TODO
            label = ctk.CTkLabel(self.display_frame, text=f"Velocidade de Giro: {fan}", fg_color=cor, width=200, height=50, corner_radius=8)
            label.grid(row=10, column=index_coluna, padx=10, pady=10)
            index_coluna += 1
        
        self.after(2000, self.atualizar_infos)

if __name__ == "__main__":
    app = Monitoracao()
    app.mainloop()


