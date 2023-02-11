import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import PhotoImage
from Pessoa import Pessoa
import pyodbc


"""Criação do layout do programa"""


class Criar:
    def __init__(self, telaprincipal):
        self.telaprincipal = telaprincipal
        global bg
        self.height = 1440
        self.width = 1025
        bg = PhotoImage(file='BACKGROUND.png')
        back = Label(image=bg)
        back.place(x=-2, y=0)
        self.frame = tkinter.Frame(bg='#D4FFF7')
        self.frame.place(
            x=0,
            y=136,
            width=165,
            height=1000)
        self.botoes()
        self.entradas()
        self.labels()

    def botoes(self):
        # Criação dos botões
        self.botao = tkinter.Button()
        self.botao.place(
            x=20,
            y=210,
            height=40,
            width=120)
        self.botao.configure(text='Adicionar',
                             font='Jost', command=self.clicadc)

        self.botao1 = tkinter.Button()
        self.botao1.place(
            x=20,
            y=270,
            height=40,
            width=120)
        self.botao1.configure(text='Editar', font='Jost')

        self.botao2 = tkinter.Button()
        self.botao2.place(
            x=20,
            y=330,
            height=40,
            width=120)
        self.botao2.configure(text='Limpar', font='Jost', command=self.cliclimpar)

        self.botao3 = tkinter.Button()
        self.botao3.place(
            x=20,
            y=390,
            height=40,
            width=120)
        self.botao3.configure(text='Procurar', font='Jost', command=self.clicprocurar)

        self.botao4 = tkinter.Button()
        self.botao4.place(
            x=20,
            y=450,
            height=40,
            width=120)
        self.botao4.configure(text='Excluir', font='Jost', command=self.clicdeletar)

        self.botao5 = tkinter.Button()
        self.botao5.place(
            x=20,
            y=520,
            height=40,
            width=120)
        self.botao5.configure(text='Sair', font='Jost', command=self.telaprincipal.destroy)

    # Criação das entradas de dados

    def entradas(self):
        self.entcad = tkinter.Entry(self.telaprincipal, relief="solid")
        self.entcad.place(
            x=200,
            y=175,
            width=75,
            height=30)
        self.entnome = tkinter.Entry(self.telaprincipal, relief="solid")
        self.entnome.place(
            x=300,
            y=175,
            width=300,
            height=30)
        self.entdata = tkinter.Entry(self.telaprincipal, relief="solid")
        self.entdata.place(
            x=620,
            y=175,
            width=150,
            height=30)
        self.entidade = tkinter.Entry(relief="solid")
        self.entidade.place(
            x=820,
            y=175,
            width=100,
            height=30)
        self.entcpf = tkinter.Entry(relief="solid")
        self.entcpf.place(
            x=970,
            y=175,
            width=100,
            height=30)
        self.entcep = tkinter.Entry(relief="solid")
        self.entcep.place(
            x=200,
            y=275,
            width=100,
            height=30)
        self.entrua = tkinter.Entry(relief="solid")
        self.entrua.place(
            x=350,
            y=275,
            width=300,
            height=30)
        self.entnum = tkinter.Entry(relief="solid")
        self.entnum.place(
            x=700,
            y=275,
            width=100,
            height=30)
        self.entbairro = tkinter.Entry(relief="solid")
        self.entbairro.place(
            x=850,
            y=275,
            width=220,
            height=30)
        self.entcomplem = tkinter.Entry(relief="solid")
        self.entcomplem.place(
            x=200,
            y=350,
            width=250,
            height=30)
        self.entcid = tkinter.Entry(relief="solid")
        self.entcid.place(
            x=500,
            y=350,
            width=150,
            height=30)
        self.entest = tkinter.Entry(relief="solid")
        self.entest.place(
            x=700,
            y=350,
            width=150,
            height=30)
        self.entpais = tkinter.Entry(relief="solid")
        self.entpais.place(
            x=900,
            y=350,
            width=170,
            height=30)
        self.enttel1 = tkinter.Entry(relief="solid")
        self.enttel1.place(
            x=200,
            y=450,
            width=150,
            height=30)
        self.enttel2 = tkinter.Entry(relief="solid")
        self.enttel2.place(
            x=425,
            y=450,
            width=150,
            height=30)
        self.entemail = tkinter.Entry(relief="solid")
        self.entemail.place(
            x=650,
            y=450,
            width=200,
            height=30)
        self.entobs = tkinter.Text(relief="solid")
        self.entobs.place(
            x=200,
            y=525,
            width=400,
            height=100)
        self.entretorna = tkinter.Text(relief="solid")
        self.entretorna.place(
            x=770,
            y=525,
            width=300,
            height=100)
        return self

    def labels(self):  # Criação das etiquetas
        self.labelcad = tkinter.Label(text="Cadastro", background='white')
        self.labelcad.place(
            x=198,
            y=150)
        self.labelmenu = tkinter.Label(text="Menu", background='#D4FFF7', font='Jost')
        self.labelmenu.place(
            x=55,
            y=160)
        self.labelnome = tkinter.Label(text="Nome", background='white')
        self.labelnome.place(
            x=300,
            y=150)
        self.labeldn = tkinter.Label(text="Data de Nascimento", background='white')
        self.labeldn.place(
            x=620,
            y=150)
        self.labelidade = tkinter.Label(text="Idade", background='white')
        self.labelidade.place(
            x=820,
            y=150)
        self.labelcpf = tkinter.Label(text="CPF", background='white')
        self.labelcpf.place(
            x=970,
            y=150)
        self.labelend = tkinter.Label(text="Endereço Residencial", background='white')
        self.labelend.place(
            x=198,
            y=225)
        self.labelcep = tkinter.Label(text="CEP", background='white')
        self.labelcep.place(
            x=198,
            y=250)
        self.labelrua = tkinter.Label(text="Logradouro", background='white')
        self.labelrua.place(
            x=350,
            y=250)
        self.labelnum = tkinter.Label(text="Número", background='white')
        self.labelnum.place(
            x=700,
            y=250)
        self.labelbairro = tkinter.Label(text="Bairro", background='white')
        self.labelbairro.place(
            x=850,
            y=250)
        self.labelcomplem = tkinter.Label(text="Complemento", background='white')
        self.labelcomplem.place(
            x=198,
            y=325)
        self.labelcid = tkinter.Label(text="Cidade", background='white')
        self.labelcid.place(
            x=500,
            y=325)
        self.labelest = tkinter.Label(text="Estado", background='white')
        self.labelest.place(
            x=700,
            y=325)
        self.labelest = tkinter.Label(text="País", background='white')
        self.labelest.place(
            x=900,
            y=325)
        self.labelest = tkinter.Label(text="Contatos", background='white')
        self.labelest.place(
            x=200,
            y=400)
        self.labeltel1 = tkinter.Label(text="Telefone 1", background='white')
        self.labeltel1.place(
            x=200,
            y=425)
        self.labeltel2 = tkinter.Label(text="Telefone 1", background='white')
        self.labeltel2.place(
            x=425,
            y=425)
        self.labelemail = tkinter.Label(text="E-mail", background='white')
        self.labelemail.place(
            x=650,
            y=425)
        self.labelobs = tkinter.Label(text="Observações", background='white')
        self.labelobs.place(
            x=200,
            y=500)
        self.labelobs = tkinter.Label(text="Busca", background='white')
        self.labelobs.place(
            x=770,
            y=500)

    def trataent(self):
        self.cad = str(self.entcad.get())
        self.nome = str(self.entnome.get())
        self.data = str(self.entdata.get())
        self.cpf = str(self.entcpf.get())
        self.cep = str(self.entcep.get())
        self.rua = str(self.entrua.get())
        self.num = str(self.entnum.get())
        self.bairro = str(self.entbairro.get())
        self.comp = str(self.entcomplem.get())
        self.cid = str(self.entcid.get())
        self.estado = str(self.entest.get())
        self.pais = str(self.entpais.get())
        self.tel1 = str(self.enttel1.get())
        self.tel2 = str(self.enttel2.get())
        self.email = str(self.entemail.get())
        self.obs = str(self.entobs.get('1.0', 'end'))
        return self.cad, self.nome, self.data, self.cpf, self.cep, self.rua, \
               self.num, self.bairro, self.comp, self.cid, self.estado, \
               self.pais, self.tel1, self.tel2, self.email, self.obs

    # Método para buscar os valores das entradas
    def buscaent(self):
        self.cad = self.entcad.get()
        self.nome = self.entnome.get()
        self.data = self.entdata.get()
        self.cpf = self.entcpf.get()
        self.cep = self.entcep.get()
        self.rua = self.entrua.get()
        self.num = self.entnum.get()
        self.bairro = self.entbairro.get()
        self.comp = self.entcomplem.get()
        self.cid = self.entcid.get()
        self.estado = self.entest.get()
        self.pais = self.entpais.get()
        self.tel1 = self.enttel1.get()
        self.tel2 = self.enttel2.get()
        self.email = self.entemail.get()
        self.obs = self.entobs.get('1.0', 'end')
        return self.cad, self.nome, self.data, self.cpf, self.cep, self.rua, \
               self.num, self.bairro, self.comp, self.cid, self.estado, \
               self.pais, self.tel1, self.tel2, self.email, self.obs

    # Método para limpar as entradas
    def limpeza(self):
        self.entcad.delete('0', 'end')
        self.entnome.delete('0', 'end')
        self.entdata.delete('0', 'end')
        self.entidade.delete('0', 'end')
        self.entcpf.delete('0', 'end')
        self.entcep.delete('0', 'end')
        self.entrua.delete('0', 'end')
        self.entnum.delete('0', 'end')
        self.entbairro.delete('0', 'end')
        self.entcomplem.delete('0', 'end')
        self.entcid.delete('0', 'end')
        self.entest.delete('0', 'end')
        self.entpais.delete('0', 'end')
        self.enttel1.delete('0', 'end')
        self.enttel2.delete('0', 'end')
        self.entemail.delete('0', 'end')
        self.entobs.delete('1.0', 'end')
        self.entretorna.delete('1.0', 'end')

    # Método para retornar valores para o usuário

    def inserir(self, pessoa):
        self.entcad.insert(0, '{}'.format(pessoa.cad))
        self.entnome.insert(0, '{}'.format(pessoa.nome))
        self.entdata.insert(0, '{}'.format(pessoa.data))
        self.entcpf.insert(0, '{}'.format(pessoa.cpf))
        self.entcep.insert(0, '{}'.format(pessoa.cep))
        self.entrua.insert(0, '{}'.format(pessoa.rua))
        self.entnum.insert(0, '{}'.format(pessoa.num))
        self.entbairro.insert(0,'{}'.format(pessoa.bairro))
        self.entcomplem.insert(0, '{}'.format(pessoa.comp))
        self.entcid.insert(0, '{}'.format(pessoa.cid))
        self.entest.insert(0, '{}'.format(pessoa.estado))
        self.entpais.insert(0, '{}'.format(pessoa.pais))
        self.enttel1.insert(0, '{}'.format(pessoa.tel1))
        self.enttel2.insert(0, '{}'.format(pessoa.tel2))
        self.entemail.insert(0, '{}'.format(pessoa.email))
        self.entobs.insert('1.0', '{}'.format(pessoa.obs))
        return

    def clicadc(self):
        dadosstr = self.trataent()
        self.pessoa = Pessoa(*dadosstr)
        self.pessoa.adicionar()

    # Método para função do botão limpar
    def cliclimpar(self):
        self.limpeza()

    # Método para função do botão excluir
    def clicdeletar(self):
        dadosstr = self.trataent()
        self.pessoa = Pessoa(*dadosstr)
        self.pessoa.excluir()

    # Método para função do botão procurar
    def clicprocurar(self):
        dados = self.buscaent()
        self.pessoa = Pessoa(*dados)
        self.pessoa.procurar()
        self.inserir(self.pessoa)
