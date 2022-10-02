#Funciones para la sección de matemáticas
def Vol_cilindro (PI, rad, altura):
    return (PI*rad**2)*altura

def Aceleracion (Vo, Vf, t):
    return (Vf-Vo)/t

def Regla_de_tres (v1, v2, v3):
    return v1*v2/v3

def Probabilidad (lista):
    Total=sum(lista)
    Grupo_interes=lista[2]+lista[3]
    R=((Total)-(Grupo_interes))/(Total)
    return R*100

def modulo_vector_resultante (matriz):
    i=0
    Suma_componentesx=0
    Suma_componentesy=0
    for linea in matriz:
        j=0
        for columna in linea:
            if j==0:
                Suma_componentesx=Suma_componentesx + matriz[i][j]
            if j==1:
                Suma_componentesy=Suma_componentesy + matriz[i][j]
            j=j+1
        i=i+1
        
    Modulo=((Suma_componentesx**2)+(Suma_componentesy**2))
    Modulo=Modulo**(1/2)
    return Modulo


def Intentos_mate (Res_correcta, cont_mate):
    i=0
    while i<2:
        R=float(input("Introduce tu respuesta"))
        if R ==Res_correcta:
            print ("Muye bien hecho", nombre, "Tu respuesta es correcta\n\n")
            return cont_mate+1
        elif R !=Res_correcta:
            print ("Has fallado, intenta otra vez")
        i=i+1
        
    print("Se agotaron tus intentos, has fallado :( \nRespuesta correcta:",
          "%.1f" %Res_correcta, "\n\n")
    
    return cont_mate
        
        
def Intentos_español (Res_correcta, cont_español):
    i=0
    while i<2:
        R=str(input("Introduce tu respuesta"))
        if R ==Res_correcta:
            print ("Muye bien hecho", nombre, "Tu respuesta es correcta \n\n")
            return cont_español+1
        elif R !=Res_correcta:
                print ("Has fallado, intenta otra vez")
            
        i=i+1
   
    print("Se agotaron tus intentos, has fallado :( \nRespuesta correcta:",
          Res_correcta, "\n\n")
    
    return cont_español         
 
 
#Inicio del programa

nombre=input("Introduzca su nombre")
edad= input("Introduzca su edad")
print("")

print ("Bienvenido a este test de inteligencia", nombre)
print("")


print ("Para cada pregunta poseeras de dos intentos")
print("")
print("")
print ("Sección matemáticas")
print("")
cont_mate=0
 
print ("Redondea tu respuesta a 1 solo decimal en caso de ser necesarios")

print ("""Pregunta 1: Calcula el volumen de un cilindro con los siguientes datos:
\nPI=3.1415 \nradio=5 \naltura=10""")
Vol= float("%.1f" %Vol_cilindro(3.1415, 5, 10))
cont_mate=Intentos_mate(Vol, cont_mate)


print ("""Pregunta 2: El vector R es la suma del vector A (3i + 4j) y el vector B (5i -6j)
\n Calcula el módulo o magnitud del vector R""")
Matriz=[[3, 4],[5,-6]]
Modulo_vector=float("%.1f" %modulo_vector_resultante (Matriz))
cont_mate=Intentos_mate(Modulo_vector, cont_mate)


if cont_mate <2:
    print ("""Pregunta 3 (versión fácil): Si un almacén de petróleo puede contener hasta 100 L
    \nCalcula al cantidad de petróleo que pueden contener 10 almacenes""")
    
    Regla3=Regla_de_tres(10, 100, 1)
    cont_mate=Intentos_mate(Regla3, cont_mate)

else:
    print ("""Pregunta 3 (versión difícil): En una bolsa hay 8 canicas azules,
    4 canicas verdes, 1 canica amarilla, 3 canicas naranjas y 7 canicas moradas
    \nSi agarro una canica al azar, que posibilidad hay de que no me salga
    una canica amarilla o naranja  \n""")
    print ("Recuerda multiplicar tu resultado x100 para que el resultado de tu porcentaje sea de 0 a 100")
    lista=[8, 4, 1, 3, 7]
    Prob=float("%.1f" %Probabilidad(lista))
    cont_mate=Intentos_mate(Prob, cont_mate)
  

print("Tu puntuación de matemáticas ha sido de", cont_mate, "de 3  \n")

print("Sección español")
print("Importante: Escribe tus respuestas empezando con mayusculas y con sus acentos correspondientes")
cont_español=0

print ("Pregunta 1: Cual de las siguientes palabras es esdrújula: \nMaíz \nÁrbol \nSábado \n")
cont_español=Intentos_español ("Sábado", cont_español)


print ("""Pregunta 2: En esta oración, ¨Escribiste mal esa palabra,
ya que hidrógeno lleva acento en la primera o¨, \ncual de las siguientes funciones del lenguaje predomina:
\nMetalinguística \nReferencial \nEmotiva \n""")
cont_español=Intentos_español ("Metalinguística", cont_español)


if cont_español<2:
    print ("""Pregunta 3 (versión fácil): Cuál de las siguientes palabras es sinónimo de intromisión:
\nPleito \nCorrespondencia \nIntrusión \nConjetura  \n""")
    cont_español=Intentos_español ("Intrusión", cont_español)
    
else:
    print ("""Pregunta 3 (versión difícil): En la siguiente frase: ¨Lleve a mi novia a Francia
y en ese país tan romántico le pedí su mano¨, Escribe la figura retórica empleada \n""")
    cont_español=Intentos_español ("Sinécdoque",cont_español)
print("Tu puntuación de español ha sido de", cont_español, "de 3 \n\n")

if cont_mate!=cont_español:
    if cont_mate<cont_español:
        print ("Dados los resultados de tu examen", nombre,
               "es notable que tu inteligencia en español es superior a tu inteligencia en matemáticas")
    else:
        print ("Dados los resultados de tu examen", nombre,
               "es notable que tu inteligencia en matemáticas es superior a tu inteligencia en español")
else:
    print ("Dados los resultados de tu examen", nombre,
           "podemos afirmar que tu intelgencia matemática esta igualmente desarrollada que tu inteligencai linguistica")