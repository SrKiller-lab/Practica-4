class Cuenta_banco:
    def __init__ (self, __nombre, __saldo):
        self.__nombre = __nombre
        self.__saldo = __saldo
        

    def get_saldo(self):
        print(self.__saldo)
        
    def set_saldo(self, saldo):
        self.__saldo = saldo
        
    def get_nombre(self):
        print(self.__nombre)
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        

cuenta_1 = Cuenta_banco("Angel", 10000)

#cuenta_1.saldo = 11000

#print(cuenta_1.saldo)

cuenta_1.get_saldo()

cuenta_1.set_saldo(5000)
cuenta_1.get_saldo()

cuenta_1.get_nombre()
cuenta_1.set_nombre("Adrian")
cuenta_1.get_nombre()

