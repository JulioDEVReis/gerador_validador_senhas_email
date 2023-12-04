import random
import re
import sqlite3
import string
import bcrypt

from customtkinter import *
from CTkMessagebox import CTkMessagebox
from validate_email_address import validate_email

class Application:
    def __init__(self):
        self.janela = root
        self.config_janela()
        self.executa_login()
        self.monta_tabela_bd()

    def config_janela(self):
        self.janela.title('Login - Gerador e Validador de senhas')
        self.janela.configure(bg='#C5D4EB')
        self.janela.resizable(0, 0)
        self.janela.geometry('400x400')

    def conecta_bd(self):
        self.conn = sqlite3.connect('usuarios.bd')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def monta_tabela_bd(self):
        self.conecta_bd()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (cod INTEGER PRIMARY KEY, nome_usuario CHAR(128) NOT NULL, email CHAR(128) NOT NULL, senha CHAR(20) NOT NULL) """)
        self.conn.commit()
        self.desconecta_bd()

    def executa_login(self):
        # Criação do Frame Login
        self.frame1 = CTkFrame(self.janela)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.etiqueta_login = CTkLabel(self.frame1, text='Fazer Login:', font=("roboto", 14))
        self.etiqueta_login.place(relx=0.37, rely=0.05)

        # Entry Email
        self.label_user = CTkLabel(self.frame1, text='Email:')
        self.label_user.place(relx=0.1, rely=0.22)
        self.user = CTkEntry(self.frame1)
        self.user.focus()
        self.user.place(relx=0.1, rely=0.28, relwidth=0.8)

        # Entry senha
        self.label_senha = CTkLabel(self.frame1, text='Senha:')
        self.label_senha.place(relx=0.1, rely=0.37)
        self.senha = CTkEntry(self.frame1, show='*')
        self.senha.place(relx=0.1, rely=0.43, relwidth=0.8)

        def verificar_login():
            email_digitado = self.user.get()
            senha_digitada = self.senha.get()

            self.conecta_bd()
            self.cursor.execute(""" SELECT * FROM usuarios WHERE email = ? """, (email_digitado, ))
            resultado = self.cursor.fetchone()
            self.desconecta_bd()

            # Verificação do usuario e senha digitada
            if resultado:
                senha_armazenada = resultado[3]
                print(senha_armazenada)
                CTkMessagebox(title='Login bem sucedido', message='Parabéns! Login bem sucedido!', icon="check", option_1="Continuar") if bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_armazenada) else CTkMessagebox(title='Erro de Login', message='Usuário ou senha digitados não conferem!', icon="cancel", option_1="Voltar!")
            else:
                print("sem resultado")
                CTkMessagebox(title='Erro de Login', message='Usuário ou senha digitados não conferem!', icon="cancel",
                              option_1="Voltar!")

        # Botão de Login e Registo
        self.botao_login = CTkButton(self.frame1, text='Login', command=verificar_login)
        self.botao_login.place(relx=0.17, rely=0.65, relwidth=0.3)
        self.botao_registo = CTkButton(self.frame1, text='Registo', command=self.realiza_registo)
        self.botao_registo.place(relx=0.53, rely=0.65, relwidth=0.3)

    def validar_email(self):
        email = self.registo_email.get()
        if validate_email(email):
            print("email validado")
            return True
        else:
            CTkMessagebox(
                message='O Email precisa ter o padrão válido',
                icon="cancel")
            self.executa_login()

    def validar_senha(self):
        senha = self.registo_senha.get()
        # Verificar a inclusão de tamanho e expressões regulares (RE)
        if (
                len(senha) < 8 or
                not re.search(r'[A-Z]', senha) or
                not re.search(r'\d', senha) or
                not re.search(r'[!@#$%?]', senha)
        ):
            CTkMessagebox(
                message='A Senha precisa ter no mínimo 8 caracteres, uma letra MAIUSCULA, um número e um caractere especial',
                icon="cancel")
            self.executa_login()
        else:
            print("senha validada")
            return True

    def realiza_registo(self):
        [widget.destroy() for widget in self.janela.winfo_children()]
        # Criação do Frame Registo
        self.frame2 = CTkFrame(self.janela)
        self.frame2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)
        self.etiqueta_registo = CTkLabel(self.frame2, text='Registo de usuário:', font=("roboto", 14))
        self.etiqueta_registo.place(relx=0.33, rely=0.25)
        # Criação do Frame Formulário de Registo
        self.frame3 = CTkFrame(self.janela)
        self.frame3.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.6)
        # Entry Email
        self.registo_email = CTkEntry(self.frame3, placeholder_text='Digite seu Email:')
        self.registo_email.place(relx=0.05, rely=0.1, relwidth=0.9)
        # Entry Nome e Apelido
        self.registo_nome = CTkEntry(self.frame3, placeholder_text='Digite seu Nome e Apelido:')
        self.registo_nome.place(relx=0.05, rely=0.30, relwidth=0.9)

        # Função para gerar senha automaticamente
        def gerar_senha():
            caracteres_senha = string.ascii_letters + string.digits * 3 + "!@#?" * 2
            senha_sugerida = ''.join(random.choice(caracteres_senha) for _ in range(12))
            return senha_sugerida

        def mostra_senha():
            if checkbox_gerar_senha.get():
                senha_gerada = gerar_senha()
                self.registo_senha.delete(0, "end")
                self.registo_senha.insert(0, senha_gerada)
            else:
                self.registo_senha.delete(0, "end")
                self.registo_senha.configure(placeholder_text='Digite sua Senha:')

        # Entry Senha
        self.registo_senha = CTkEntry(self.frame3, placeholder_text='Digite sua Senha:')
        self.registo_senha.place(relx=0.05, rely=0.5, relwidth=0.9)
        # Checkbox de Geração de senha
        checkbox_gerar_senha = CTkCheckBox(self.frame3, text="Gerar Senha Automaticamente")
        checkbox_gerar_senha.place(relx=0.05, rely=0.64)
        checkbox_gerar_senha.configure(command=mostra_senha)
        # Botão de Registo e Voltar
        self.botao_finaliza_registo = CTkButton(self.frame3, text='Registo', command=self.verifica_registo)
        self.botao_finaliza_registo.place(relx=0.17, rely=0.80, relwidth=0.3)
        self.botao_voltar = CTkButton(self.frame3, text='Voltar', command=self.executa_login)
        self.botao_voltar.place(relx=0.53, rely=0.80, relwidth=0.3)

    def criptografar_senha(self, senha):
        # Gerar um SALT aleatorio
        salt = bcrypt.gensalt()
        # Usar o salt para criar um HASH da senha
        senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_criptografada

    def verifica_registo(self):
        self.validar_email()
        self.validar_senha()
        print("Registo verificado")
        if self.validar_senha and self.validar_email:
            senha_criptografada = self.criptografar_senha(self.registo_senha.get())
            self.executa_cadastro_BD(self.registo_email.get(), self.registo_nome.get(), senha_criptografada)

    def executa_cadastro_BD(self, email, nome, senha):
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO usuarios (nome_usuario, email, senha) VALUES (?, ?, ?) """, (nome, email, senha))
        self.conn.commit()
        self.desconecta_bd()
        print("cadastro incluido no BD")
        self.executa_login()


if __name__ == '__main__':
    root = CTk()
    app = Application()
    root.mainloop()