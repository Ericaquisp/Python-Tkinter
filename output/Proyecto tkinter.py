"""
SMTP
¿Qué es y para qué sirve SMTP?
SMTP, Simple Mail Transfer Protocol por sus siglas en inglés, es un protocolo o conjunto de reglas 
de comunicación que utilizan los servidores de correo electrónico para enviar y recibir e-mails.
"""
from email.message import EmailMessage #Construir la estructura del email
import smtplib # conectar con el servidor y enviarlo
from tkinter import *
from tkinter import messagebox
#Python image Library
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk

"------------INTERFAZ TKINTER------------"
ventana =Tk()
ventana.title("Aplicación para mandar correos electronicos")
ventana.geometry("350x410")
ventana.resizable(0,0)
ventana.config(bd=10)


Label(ventana, text="ENVIAR CORREO VIA GMAIL",fg="black",font=("Arial", 15,"bold"),padx=5,pady=5).grid(row=0,column=0,columnspan=2)

#Imagen GMAIL
imagen_gmail=Image.open("logoo.jpg")
nueva_imagen=imagen_gmail.resize((125,84))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= Label(ventana, image= render)
label_imagen.image=render
label_imagen.grid(row=1,column=0,columnspan=2)

destinatario=tk.StringVar()
opciones = ttk.Combobox(ventana,
    font= "consolas 10 bold",
    width=27,
    values= ["fjcoronati@gmail.com","programacionsabattini@gmail.com","lafortaleza123@gmail.com", "mariaavalos7090@gmail.com", "danielprogramacion53@gmail.com", "axela5746@gmail.com"],
    state="readonly",
    textvariable=destinatario)
opciones.grid(row=3,column=1)

def mostrar():
    if(Otro.get() ==1):
        opciones = ttk.Combobox(ventana,
            font= "consolas 10 bold",
            width=27,
            values=  ["fjcoronati@gmail.com","programacionsabattini@gmail.com","lafortaleza123@gmail.com", "mariaavalos7090@gmail.com", "danielprogramacion53@gmail.com", "axela5746@gmail.com"],
            textvariable=destinatario)
        opciones.grid(row=3,column=1)
    else:
        opciones = ttk.Combobox(ventana,
            font= "consolas 10 bold",
            width=27,
            values=  ["fjcoronati@gmail.com","programacionsabattini@gmail.com","lafortaleza123@gmail.com", "mariaavalos7090@gmail.com", "danielprogramacion53@gmail.com", "axela5746@gmail.com"],
            state="readonly",
            textvariable=destinatario)
        opciones.grid(row=3,column=1)
        
Otro = IntVar()
Otro_button = Checkbutton(ventana, text="Otro" ,variable= Otro ,command=mostrar)
Otro_button.grid(row=4,column=1)


asunto=StringVar(ventana)
Label(ventana, text="Mi correo: velasquezerica41@gmail.com",fg="white",bg="pink",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=2,column=0,columnspan=2,pady=5)
  
Label(ventana, text="Destinatario:",fg="black",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=3,column=0)

Label(ventana, text="Asunto:",fg="black",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=5,column=0)
Entry(ventana,textvariable=asunto, width=34).grid(row=5,column=1)

Label(ventana, text="Mensaje:",fg="black",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=6,column=0)
mensaje=Text(ventana,height=5,width=28,padx=5,pady=5)
mensaje.grid(row=6,column=1)
mensaje.config(font=("Arial", 9),padx=5, pady=5)


"------------ENVIO DE CORREO------------"
def enviar_email():
    remitente = "velasquezerica41@gmail.com"
    #Estrutura de email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario.get()
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0, 'end')))
    #Envio de email
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "ynjn rqjf fssp bjmb")
    smtp.sendmail(remitente, destinatario.get(), email.as_string())
    messagebox.showinfo("MENSAJERIA","Mensaje enviado correctamente ")
    smtp.quit()

"------------BOTON------------"
Button(ventana,text="ENVIAR",command=enviar_email,height=2,width=10,bg="black",fg="white",font=("Arial", 10,"bold")).grid(row=7,column=0,columnspan=2,padx=5,pady=10)

ventana.mainloop()