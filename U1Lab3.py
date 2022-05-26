from datetime import datetime 
#Clase Cliente con sus distintos atributos para el registro del cliente
class Cliente:
    def _init_(self,nombre,telefono,estado,contrasenaCliente):
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
        self.contrasenaCliente=contrasenaCliente
#Clase Tienda con sus distintos atributos para el registro de Tiendas
class Tienda:
    def _init_(self,nombreTienda,telefonoTienda,estadoTienda,gerenteTienda):
        self.nombreTienda=nombreTienda
        self.telefonoTienda=telefonoTienda
        self.estadoTienda=estadoTienda
        self.gerenteTienda=gerenteTienda
#Constante para Ingresar como Administrador del sistema
correoAdmin="anthony@gmail.com"
contrasenaAdmin="1234"
#Apertura del menú principal que conllevara 2 submenus
opcionMenuPrincipal = int(input("================================\n\tMenú Principal\n================================\n\t1. Cliente\n\t2. Admin\n\t3. salir\n================================"))
while opcionMenuPrincipal != 3:   #Mientras la opción no sea 3 que se repita, y si ingresamos 3 el bucle se acabe donde 3 sería la opcion salir

    if opcionMenuPrincipal == 1:
        #Apertura del submenu de Cliente donde se podrá llevar a cabo actividades que un cliente puede realizar con normalidad
        opcionMenucliente = int(input("================================\n\tMenú Cliente\n================================\n\t1. Registrarse al Sistema\n\t2. Inicio de Sesión\n\t3. Registrarse en una Tienda\n\t4. Historial de Tiendas\n\t5. Ver Estado\n\t6. Regresar\n================================"))
        while opcionMenucliente != 6:#Mientras la opción no sea 6 que se repita, y si ingresamos 6 el bucle se acabe donde 6 sería la opcion salir
            if opcionMenucliente == 1:
                print ("\tRegistro al Sistema")
                nombre = str(input("Ingrese su Nombre: "))
                telefono = int(input("Ingrese su Número de Telefono: "))
                print ("\tEstado \nNormal: Usted no tiene Covid \nCaso: Usted Tiene Covid \nCercano: Se verificara si se registra en un rango de tiempo a un cliente con Caso")
                estado = str(input("Ingrese su Estado (Normal o Caso): "))
                contrasenaCliente = str(input("Ingrese una Contraseña: "))
                print ("Se ha registrado correctamente... \nRecuerde que el usuario para iniciar sesión es su nombre")
                fecha=datetime.today().strftime("%Y-%m-%d")#con el uso de la libreria datetime calculamos 
                hora=datetime.today().strftime("%H:%M")#La fecha y la Hora
                print (fecha," ",hora)

            elif opcionMenucliente == 2:
                print ("================================")
                print ("\tInicio de Sesión")
                usuario = str(input("Ingrese el Usuario: "))
                while (usuario != nombre):#bucle mientras para validar el usuario con el diferente igual 
                    print ("Usuario Invalido... \nVuelva a Ingresar")
                    usuario = str(input("Ingrese el Usuario: "))   
                contrasena = str(input("Ingrese la Contraseña: "))
                while (contrasena != contrasenaCliente):#bucle para validar contraseña
                    print ("Contraseña Invalida... \nVuelva a Ingresar")
                    contrasena = str(input("Ingrese la Contraseña: "))
                print ("\tBIENVENIDO AL SISTEMA")          
                print ("================================") 

            elif opcionMenucliente == 3:
                i = 0#incio de iterador par el uso del bucle for posteriormente 
                numeroTiendasRegistrar = int(input("Número de Tiendas a Registrar: "))#ingresar el numero de tiendas a las que se va a registrar
                for i in range(numeroTiendasRegistrar):#incremento en for respecto al numero de tiendas
                    print ("\tRegistro a Tiendas")
                    nombreTienda = str(input("Ingrese el Nombre de la Tienda: "))
                    telefonoTienda = str(input("Ingese el Nro de Telefono de la Tienda: "))
                    gerenteTienda = str(input("Nombre del Gerente: "))
                    estadoTienda = str(input("Ingrese su Estado (Normal o Caso): "))
                    fechaTienda=datetime.today().strftime("%Y-%m-%d")
                    horaTienda=datetime.today().strftime("%H:%M")
                    print (fechaTienda," ",horaTienda)
                    print ("================================") 

            elif opcionMenucliente == 4:
                print ("\tHistorial de Tiendas")
                for i in range(numeroTiendasRegistrar):#bucle for para imprimir todas las tiendas registradas
                    print ("--------------------------------------------")
                    print ("Nro. Fecha       Hora     Tienda")
                    print (i+1,"  ",fechaTienda," ",horaTienda," ",nombreTienda)
                    print ("--------------------------------------------")
                print ("================================")

            elif opcionMenucliente == 5:
                print ("\tVer Estado")
                print (estado)#Ver el estado que ingreso el cliente al registrarse 
            elif opcionMenucliente == 6:
                print ("Ha regresado Correctamente")
            else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
            opcionMenucliente = int(input("================================\n\tMenú Cliente\n================================\n\t1. Registrarse al Sistema\n\t2. Inicio de Sesión\n\t3. Registrarse en una Tienda\n\t4. Historial de Tiendas\n\t5. Ver Estado\n\t6. Regresar\n================================"))
    
    elif opcionMenuPrincipal == 2:

        print ("================================")
        print ("\tInicio de Sesión")
        correoAdminLogin = str(input("Ingrese el Correo: "))
        while (correoAdminLogin != correoAdmin):#bucle mientras para validar los datos del administrador, para poder acceder a funciones especiales
            print ("Correo Invalido... \nVuelva a Ingresar")
            correoAdminLogin = str(input("Ingrese el Correo: "))  

        contrasenaAdminLogin = str(input("Ingrese la Contraseña: "))
        while (contrasenaAdminLogin != contrasenaAdmin):
            print ("Contraseña Invalida... \nVuelva a Ingresar")
            contrasenaAdminLogin = str(input("Ingrese la Contraseña: "))
            
        print ("\tBIENVENIDO AL SISTEMA ADMIN")          
        print ("================================")
        opcionMenuAdmin = int(input("============================================\n\tMenú Admin\n================================\n\t1. Detalles clientes, tiendas y visitas\n\t2. Estados Tienda y Clientes\n\t3. Regresar\n============================================"))
        while opcionMenuAdmin != 3:#inicio de otro submenu donde el administrador podrá realizar sus actividades 


            if opcionMenuAdmin == 1:
                print ("\tDETALLES CLIENTES")
                print ("------------------------------------------------------")
                print ("Nro.  Nombre    Telefono    Estado ")
                print ("1 "," ",nombre," ",telefono," ",estado)
                print ("------------------------------------------------------")

                for i in range(numeroTiendasRegistrar):#bucle for para imprimir las tiendas registradas
                    print ("------------------------------------------------------")
                    print ("Nro. Tienda  Telefono  Gerente  Estado")
                    print (i+1,"  ",nombreTienda," ",telefonoTienda," ",gerenteTienda," ",estadoTienda)
                    print ("------------------------------------------------------")
            elif opcionMenuAdmin == 2:
                print ("\tESTADOS CLIENTES Y TIENDAS")
                print ("=======================================")
                print ("Clientes: ")
                print (nombre, "\nEstado: ",estado)
                print ("=======================================")
                print ("Tiendas: ")
                for i in range(numeroTiendasRegistrar):#bucle for para imprimir los estados de las tiendas registradas
                    print (i+1," ",nombreTienda,"\nEstado: ",estadoTienda)

            elif opcionMenuAdmin == 3:
                print ("Ha regresado Correctamente")

            else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
            opcionMenuAdmin = int(input("============================================\n\tMenú Admin\n================================\n\t1. Detalles clientes, tiendas y visitas\n\t2. Estados Tienda y Clientes\n\t3. Regresar\n============================================"))

    elif opcionMenuPrincipal == 3:
        print ("Ha salido Correctamente")

    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar") 
    opcionMenuPrincipal = int(input("================================\n\tMenú Principal\n================================\n\t1. Cliente\n\t2. Admin\n\t3. salir\n================================"))
