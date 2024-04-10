import tkinter as tk
import apl

class Formulario:
    def __init__(self):
        self.janela = tk.Tk()

        # Adicionar um rótulo e uma entrada para CPFs
        self.label_cpf = tk.Label(self.janela, text="Lista de CPFs separados por vírgula:")
        self.label_cpf.pack()
        self.entrada_cpf = tk.Text(self.janela, width=75, height=10)
        self.entrada_cpf.pack()

        # Adicionar um rótulo e um textarea para contribuição
        self.label_contribuicao = tk.Label(self.janela, text="Contribuição:")
        self.label_contribuicao.pack()
        self.entrada_contribuicao = tk.Text(self.janela, height=15, width=75)
        self.entrada_contribuicao.pack()

        # Adicionar um botão para enviar
        self.botao_enviar = tk.Button(self.janela, text="Enviar", command=self.enviar)
        self.botao_enviar.pack()

    def enviar(self):
        apl.sendRequest()

    def getJanela(self):
        return self.janela

    def getCpf(self):
        return self.entrada_cpf.get("1.0", "end-1c")

    def getContribuicao(self):
        return self.entrada_contribuicao.get("1.0", "end-1c")
