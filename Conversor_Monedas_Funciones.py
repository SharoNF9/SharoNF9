#Menu -> a Quetzales, Dolares a Euros, Euros a Dolares
#Funciones

def DolarQuetzal (dolar):
      quetzales = dolar * 7.71
      return quetzales

def QuetzalDolar (quetzal):
          dolares = quetzal * 0.12
          return dolares
def Euroquetzal (euro):
            quetzales = euro *0.116963 
            return quetzales 
def QuetzalEuro (quetzal):
            euros = quetzal * 8.54
            return euros
    

print ("------Conversor de Monedas-------")

while True:
    res = input('''
    1. Dolares a Quetzales
    2. Quetzales a Dolares
    3. Euros a quetzales
    4. Quetzales a Euros
    5. Salida
    Seleccione una opcion:''')

    if res == '1':
     print ("Ingrse la cantidad de dolares")
     dolaresaquetzales = float (input("Dolares:")) 
     print ("La cantidad en quetzales es:", DolarQuetzal)
    
        
    elif res == '2':
     print("Ingrse la cantidad de quetzales")
     (QuetzalDolar)

    elif res == '3':
        print ("Ingrese la cantidad de Euros")
        (Euroquetzal)
    
    elif res == '4':
        print ("Ingrese la cantidad de quetzales")
        (QuetzalEuro)
    
    elif res == '5':
        print("Gracias por usar el conversor")
        break

