print("-----------------------------")
print("---Numeros pares e impares---")
print("Seleccione lo que quiera imprimir")

while True:
    selec = input('''
    1. Imprimir Pares
    2. Imprimir Impares
    seleccione una opción''')
   
    if selec == '1':
        numero = 0
        while numero < 101:
            if numero % 2 == 0:
             print (numero, "Es par")
            numero+=1 
    elif selec== '2':
        numero = 0
        while numero < 101:
            if numero % 2!= 0:
             print (numero, "Es impar")  
            numero+=1         
   
