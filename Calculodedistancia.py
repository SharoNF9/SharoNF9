#Primera Cordenada (2,4)
punto1x = ''
punto1y = ''

#Segunda cordenada (3,6)
punto2x = ''
punto2y = ''

#----------Calculo de Distancia-------
def distancia(x1,y1,x2,y2):
    try:
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)
        d=((x1 - x2)**2 + (y1 - y2)**2)**0.5
        return "La distancia es de:" + str(d)
    except:
        return"Error, no se puede realizar este calculo"
       
#-----------Pregunta al usuario------------
while True:
 print('''
 ------------CALCULO DE DISTACIA ENTRE PUNTOS---------
 ''')
 punto1x =input('Ingrese la cordenada en X del primer punto')
 punto1y =input('Ingrese la cordenada en Y del primer punto')
 punto2x =input('Ingrese la cordenada en X del primer punto')
 punto1y =input('Ingrese la cordenada en Y del primer punto')

 dist = distancia(punto1x,punto1y,punto2x,punto2y)
 print(dist)
 input("Prseione Enter para continuar... ")
