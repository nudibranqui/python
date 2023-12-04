class Vehiculo:
    def_init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    
    def accelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print( "Marca: ", self.marca, "\nModelo: ", self.modelo, "\Enmarcha: ", self.enmarcha, "\nFrena: ", self.frena, "\nAcelera: ", self.acelera)