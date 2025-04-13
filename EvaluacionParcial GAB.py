# Objetivo: Evaluacion Parcial
# Nombre : Añasco Bendezu Giancarlos
# Fecha: 13/04/25

print("IE MI PAIS - Recolecta 5to Año")
while(True):
    menu=int(input("""
****** MENU DE OPCIONES ******
                   
1. AUTENTICARSE
2. REGISTRAR DONACIONES
3. CALCULADORA
4. REPORTE TOTAL
5. SALIR DEL PROGRAMA
                   """))
    
    if(menu ==1):
        while (True):
            contraseña=71343436
            
            usuario=str(input("Ingrese su usuario (Apellido Paterno): "))
            contraseña=int(input("Ingrese Contraseña: "))
            if (contraseña<=999999999):
                break
            else:
                print("ERROR la contraseña no es valida")
            
    while(True):
        menu=int(input("""
****** MENU DE OPCIONES ******
                   
2. REGISTRAR DONACIONES
3. CALCULADORA
4. REPORTE TOTAL
5. SALIR DEL PROGRAMA
                   """))
        if(menu ==2):
            seccion=str(input("Ingrese su sección A/B/C/D: "))
            if (seccion=="A" or "B" or "C" or "D"):
                break
            else:
                print("ERROR Ingrese una seccion valida A/B/C/D")
    
            n=int(input("Ingrese el numero de alumnos: "))
            if (n>0):
                break
            else:
                print("ERROR Ingrese solo numeros positivos")
            
            n=0
            i=0
            varACU1=0
            while(i<n):
                i+=1
                while (True):
                    ApellidoAlum=str(input("Ingrese apellido paterno del alumno: "))
                    DniAlum=int(input("Ingrese el DNI del alumno: "))
                    if (DniAlum<99999999):
                        break
                    else:
                        print("ERROR El numero de DNI no es valido")
                    GeneroAlum=str(input("Ingrese el sexo del alumno M/F: "))
                    if GeneroAlum=="M":
                        break
                    elif GeneroAlum=="F":
                        break
                    else:
                        print("ERROR genero invalido, ingrese solo M ó F")
                    while (True):
                            respuesta = input("¿El alumno usa lentes? SI/NO: ").upper()

                            if respuesta == "SI":
                                UsoLentes = True
                                break
                            elif respuesta == "NO":
                                UsoLentes = False
                                break
                            else:
                                print("ERROR Ingresa solo SI o NO")

                            if UsoLentes==True:
                                print("El alumno usa lentes")
                            else:
                                print("El alumno no usa lentes")
                    edadAlum=int(input("Ingresar edad del alumno: "))
                    menorEdad=int(13<=edadAlum<18)
                    mayorEdad=int(edadAlum=18)
                    if (13<=edadAlum<=18):
                        break
                
                    else:
                        print("ERROR LA EDAD NO ES CORRECTA")

                    MontoAlumn=float(input("Ingresa el monto de tu donacion: "))
                    if (MontoAlumn>0):
                        print("GRACIAS por tu donacion de:", MontoAlumn)
                    
                    varACU1=varACU1+(GeneroAlum=="M") #VARON
                    varACU2=varACU2+(GeneroAlum=="F") #MUJER
                    varACU3=varACU3+(respuesta=="SI"-varACU1) #CON LENTES - varones
                    varACU4=varACU4+(respuesta=="SI"-varACU2) #CON LENTES - mujeres
                    varACU5=varACU5+(respuesta=="NO") #SIN LENTES total
                    varACU6=varACU6+menorEdad
                    varACU7=varACU7+mayorEdad
                    varACU8=varACU8+MontoAlumn #MONTO TOTAL RECAUDADO


        
        if(menu ==3):
            while(True):
                menu=int(input("""
****** MENU DE OPCIONES ******
1. SUMA DE DOS NUMEROS       
2. RESTA DE DOS NUMEROS
3. MULTIPLICACION DE DOS NUMEROS
4. DIVICION DE DOS NUMEROS
5. MODULO DE DOS NUMEROS
                   """))
                if (menu ==1):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    suma=a+b
                    print("La suma es: ",suma)
                if (menu ==2):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    resta=a-b
                    print("La resta es: ",resta)
                if (menu ==3):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    multiplicacion=a*b
                    print("La multiplicacion es: ",multiplicacion)
                if (menu ==4):
                    a=float(input("Ingrese numero 1: "))
                    b=float(input("Ingrese numero 2: "))
                    if b!=0:
                        divicion=a/b
                        print("La divicion es: ", divicion)
                    else:
                        print("ERROR no se puede dividor entre cero")
                if (menu ==5):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    modulo=a%b
                    print("El modulo (MOD) es: ",modulo)

        if(menu ==4):
            print("****** REPORTE TOTAL ******")
            print("La cantidad de alumnos masculinos ingresados es: ", varACU1 )
            print("La cantidad de alumnas femeninas ingresadas es: ", varACU2)
            print("La cantidad de alumnos con lentes son: ", varACU4)
            print("La cantidad de alumnas con lentes son: ", varACU3)
            print("La cantidad de alumnas y alumnos SIN lentes son: ", varACU5)
            print("La cantidad de alumnos menores de edad son: ", varACU6)
            print("La cantidad de alumnos mayores de edad son: ", varACU7)
            print("La seccion ingresada fue: ", seccion)
            print("El monto total recaudado es: ", varACU8)
            print("El monto total recaudado - refrigerio del experto (s/50) es: ", varACU8-50)
            print("El monto neto total recaudado es: ", varACU8-50)

        if(menu ==5):
            print("Esta saliendo de TECNICAS DE PROGRAMACION :P :()")



            

                    

    









