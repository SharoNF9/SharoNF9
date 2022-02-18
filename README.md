#Nombre del algoritmo
print ("Sharon Figueroa")
print("---------------------------")
print("CALCULAR AREAS Y PERIMETROS")
print("---------------------------")

while True:
    res = input('''
    1.Rectangulo
    2.Cuadrado 
    3.Circulo
    4.Salida
Seleccione una opcion''')
    if res== '1':
     #Entrada 
        print("Ingrese la base y Altura")
        base = float (input("Base:"))
        altura = float (input ("Altura "))    
    #Proceso
        area = base * altura
        perimetro = 2(base) +2(altura)
    #salida
        print ("---------------------------")
        print("Area:",area)
        print("Perimetro:" ,perimetro)

    elif res== '2':
       #Entrada 
        print("Ingrese un lado del cuadrado")
        lado = float (input("lado:"))  
        #Proceso
        area = 2(lado)
        perimetro = (lado)*4
        #salida
        print ("---------------------------")
        print ("El Area:",area)
        print ("El perimetro:",perimetro )
    elif res== '3':
       #Entrada 
        radio = float (input("Ingrse el radio del circulo:"))   
        #Proceso
        area = 3.1416*radio*radio
        perimetro = 2*3.1416* radio
        #salida
        print ("---------------------------")
        print("Area:",area)
        print("Perimetro:" ,perimetro )
    elif res == '4':
        print ("adiosito")
        break 
    else:
        print('Por favr selecciona una opcion correcta')
