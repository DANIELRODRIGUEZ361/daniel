nombre = imput("Ingrese su nombre\n")
apellido = imput("Ingrese su apellido\n")
edad = int(imput("ingrese su edad\n"))
sexo = int(imput("ingrese su sexo\n"))

if edad>0 and edad <=18:
print("Es menor de edad")
else:
print("Es mayor de edad")

if sexo==1 and sexo!=2:
print("Es UNA mujer")
else:
print("es UN hombre")