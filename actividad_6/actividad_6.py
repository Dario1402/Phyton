#Clase
class Cuenta:

    #Constructor de la clase
    def __init__(self, titular, cantidad): 

      #Atributos de la instancia
      self.titular = titular
      self.cantidad = cantidad

    #Constructor para mostrar
    def mostrar(self):
      print("Titular:", self.titular)
      print("Cantidad: $", self.cantidad)

    #Constructor ingresar
    def ingresar(self, cantidad):
      if cantidad>0:
        self.cantidad += cantidad
        print("La cantidad ingresada es: $", cantidad,"\nLa cantidad total es: $", self.cantidad)  
      
        
    #Constructor retirar
    def retirar(self, cantidad):
      if cantidad > 0:
        self.cantidad -= cantidad
        print("La cantidad retirada es: $", cantidad,"\nLa cantidad total es: $", self.cantidad)

    
Cuenta1 = Cuenta("Dario",5000)
Cuenta1.mostrar()
Cuenta1.ingresar(-2000)
Cuenta1.ingresar(3000)
Cuenta1.retirar(-8000)
Cuenta1.retirar(6000)
