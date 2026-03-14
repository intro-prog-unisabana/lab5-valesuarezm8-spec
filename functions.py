
def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    resultado = sum(calificaciones) / len(calificaciones)
    return resultado

calificaciones =[]  
promedio = promedio_estudiante(calificaciones)
print(promedio)

