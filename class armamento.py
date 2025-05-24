#Sergio Gomez Lopez
class Armamento:
    def __init__ (self, __daño, __calidad, __tipo):
        self.__daño = __daño
        self.__calidad = __calidad
        self.__tipo = __tipo
    
    def get_daño(self):
        print(self.__daño)
    
    def set_daño(self, daño):
        self.__daño = daño
        
    def get_calidad(self):
        print(self.__calidad)
        
    def set_calidad(self, calidad):
        self.__calidad = calidad
        
    def get_tipo(self):
        print(self.__tipo)
        
    def set_tipo(self, tipo):
        self.__tipo = tipo
        
clase_1 = Armamento(100, "Legendario", "Rango")

#clase_1.daño = 200
#print(clase_1.daño)

clase_1.get_daño()
clase_1.set_daño(200)
clase_1.get_daño()

clase_1.get_calidad()
clase_1.set_calidad("Mitico")
clase_1.get_calidad()

clase_1.get_tipo()
clase_1.set_tipo("Melee")
clase_1.get_tipo()