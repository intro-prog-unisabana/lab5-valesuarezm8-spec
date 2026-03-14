
def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0,0
    return sum(calificaciones) / len(calificaciones) 

calificaciones =[85, 92, 78]     
promedio = promedio_estudiante(calificaciones)
print(promedio)

