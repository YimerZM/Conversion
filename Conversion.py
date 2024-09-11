import math

class ConversionAngulos:
    def ingresoAngulo(self):
        angulo = float(input("Ingrese el ángulo en grados: "))
        return angulo

    def gradosARadianes(self, grados):
        return grados * math.pi / 180

    def radianesAGrados(self, radianes):
        return radianes * 180 / math.pi

if __name__ == '__main__':
    operacion = ConversionAngulos()
    grados = operacion.ingresoAngulo()
    radianes = operacion.gradosARadianes(grados)
    print(f"{grados} grados son {radianes:.4f} radianes")
    print(f"{radianes:.4f} radianes son {operacion.radianesAGrados(radianes):.2f} grados")
