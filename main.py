from Conversion import ConversionAngulos

if __name__ == '__main__':
    operacion = ConversionAngulos()
    grados = operacion.ingresoAngulo()
    radianes = operacion.gradosARadianes(grados)
    print(f"{grados} grados son {radianes:.4f} radianes")
    print(f"{radianes:.4f} radianes son {operacion.radianesAGrados(radianes):.2f} grados")

