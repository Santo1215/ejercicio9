from datetime import datetime
nombres = []


class Evento:
    def __init__(self):
        pass
   
    def crearevento(self): 
        self.crearevento = input("INGRESE EL NOMBRE DEL EVENTO")

    def tiempo_restante(fecha_evento):
        hoy = datetime.now()
        diferencia = fecha_evento - hoy
        dias_restantes = diferencia.days
        return dias_restantes

    if __name__ == "__main__":
        try:
            fecha_str = input("INGRESE LA FECHA DEL EVENTO (YYYY-MM-DD): ")
            fecha_evento = datetime.strptime(fecha_str, '%Y-%m-%d')
            dias_restantes = tiempo_restante(fecha_evento)

            if dias_restantes > 0:
                print(f"FALTAN {dias_restantes} DIAS PARA LA FECHA {fecha_evento}.")
            elif dias_restantes == 0:
                print("¡Hoy es el evento!")
            else:
                print(f"EL EVENTO YA HA PASADO, LA FECHA {fecha_evento} FUE HACE {-dias_restantes} DIAS.")
        except ValueError:
            print("Error: INGRESA UNA FECHA VALIDA EN EL FORMATO 'YYYY-MM-DD'.")

class Participante(Evento):
    def __init__(self):
        pass
   
    def agregarparticipantes(self):
        
        self.cantidadparticipantes = int(input("INGRESE LA CANTIDAD DE PARTICIPANTES"))
        n = self.cantidadparticipantes
        for i in range (self.cantidadparticipantes):
            nombre = input(f"INGRESE EL NOMBRE DEL PARTICIPANTE {i+1} ")
            nombres.append(nombre)

class Notificacion(Participante):
    def __init__(self):
        pass

    def notificar(self):
        for i in range (self.cantidadparticipantes):
            print(f"EL PARTICIPANTE {nombres[i]} HA SIDO NOTIFICADO DEL EVENTO {self.crearevento}")

 
n = Notificacion()
n.crearevento()
n.agregarparticipantes()
n.notificar()
