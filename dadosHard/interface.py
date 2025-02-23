import customtkinter

class Aplicacao:
    def __init__(self):
        '''
        Retorna a parte visual da aplicação.

        Args:
            root (str): Define a janela principal da aplicação.
            local_planilha (str): Guarda o caminho do diretório onde se localiza a planilha, inicialmente vazio.
    
        Returns:
            tela() (function): Contém a informação sobre os elementos visuais contidos na aplicação.
            root.mainloop() (function): Mantém a aplicação funcionado em um loop.
        '''
        self.root = root
        self._local_planilha = ''
        self.tela()

    def tela(self):
        '''
        Cria os elementos visuais e suas "tarefas".

        Args:
            root (str): Define a janela principal da aplicação.
    
        Returns:
            Void
        '''
        self.root.title('Automaizador de Cadastro de NFS')

        largura = 500
        altura = 300

        altura_tela = self.root.winfo_screenheight()
        largura_tela = self.root.winfo_screenwidth()

        posx = (largura_tela/2) - (largura/2)
        posy = (altura_tela /2) - (altura/2)

        self.root.geometry(f'{largura}x{altura}+{int(posx)}+{int(posy)}')
        self.root.wm_resizable(False, False)

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        titulo = customtkinter.CTkLabel(root, text='Cadastrar NFS', font=('Heveltica', 18))
        titulo.pack(padx=10, pady=10)

        textbox_planilha = customtkinter.CTkEntry(root, placeholder_text='Diretório da planilha', width=370)
        textbox_planilha.pack(padx=10, pady=10)

        botao_carregar_planilha = customtkinter.CTkButton(root, text='Abrir Planilha', command = lambda: self.abrir_planilha(textbox_planilha))
        botao_carregar_planilha.pack(padx=10, pady=10)

        textbox_mes = customtkinter.CTkEntry(root, placeholder_text='Mês do cadastro')
        textbox_mes.pack(padx=10, pady=10)

        botao_iniciar_automacao = customtkinter.CTkButton(root, text='Iniciar Automação', command = lambda: self.iniciar_automacao(textbox_mes.get()))
        
        botao_iniciar_automacao.pack(padx=10, pady=10)

if __name__ == '__main__':
    root = customtkinter.CTk()
    Aplicacao()
    root.mainloop()

