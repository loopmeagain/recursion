class Asiento:
    pasajero = None
    def estaLibre(self):
        return self.pasajero == None


    def ocupar(self,pasajero):   
        if(self.estaLibre()):
            self.pasajero = pasajero 

    def __repr__(self):
        if(self.estaLibre()):
            return "estoy libre"
        return "estoy ocupado"



    

class Minibus:
    asientos = []
    

    def capacidad(self,cantidad):
        for i in range(cantidad):
            self.asientos.append(Asiento())

    def __init__(self,CantidadAsientos=6):
        self.capacidad(CantidadAsientos)
    
    def asientoEstaLibre(self):
        return lambda unAsiento:unAsiento.estaLibre()
    def asientoEstaOcupado(self):
        return lambda unAsiento:not(unAsiento.estaLibre())




    def agregar(self,pasajero):
        
        asientosLibres = list(filter(self.asientoEstaLibre(),self.asientos))
        asientosOcupados = list(filter(self.asientoEstaOcupado(),self.asientos))
        print(len(asientosLibres))
        if(asientosLibres!=[] and len(asientosOcupados)<50):
            asientosLibres[0].ocupar(pasajero)
            

        

class Pasajero:
    pass


minibus = Minibus(60)
pasajero = Pasajero()
pasajero2 = Pasajero()
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
minibus.agregar(pasajero)
