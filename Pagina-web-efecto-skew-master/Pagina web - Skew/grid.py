from tkinter import*
Raíz= Tk ()
Raíz.title("Ventana principal")
Raíz.config(bg="white")
MiFrame=Frame()
MiFrame.pack()
Miframe=Frame()
Miframe.pack()
Miframe.config(width=330, height=545, bg="white", cursor="star")
Myframe=Frame()
Myframe.pack()

mila=Label(MiFrame, fg="red", font=("Arial",16), text="Registro para nuevos clientes",pady=10).grid(row=0,column=0)

nombre=Label(Miframe, font=("Arial",9), text="Nombre",pady=10,padx=30   ).grid(row=1,column=0)

apellidos=Label(Miframe, font=("Arial",9), text="Apellidos",pady=10).grid(row=3,column=0)

telefono=Label(Miframe, font=("Arial",9), text="Telefono",pady=10).grid(row=5,column=0)

direccion=Label(Miframe, font=("Arial",9), text="Direccion",pady=10).grid(row=7,column=0)

registrar=Button(Myframe, font=("Arial",9), text="Registrar", pady=1,padx=50).grid(row=10,column=1)

mien=Entry(Miframe, bd=1).grid(row=1,column=1)

mient=Entry(Miframe, bd=1).grid(row=3,column=1)

mientr=Entry(Miframe, bd=1).grid(row=5,column=1)

mientry=Entry(Miframe, bd=1).grid(row=7,column=1)
Raíz.mainloop()