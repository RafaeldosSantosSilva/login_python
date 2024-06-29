#from tkinter import *
import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Estou logado")

def senha_mostrada():
    print(senha)

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email=customtkinter.CTkEntry(janela, placeholder_text="Digite seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)

mostrar_senha = customtkinter.CTkCheckBox(janela, text="Mostrar senha", command=senha_mostrada,)
mostrar_senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Logar", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()