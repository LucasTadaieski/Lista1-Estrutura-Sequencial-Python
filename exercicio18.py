SegundosTotal = int(input("digite a duração total do evento em segundos:"))

horas = SegundosTotal // 3600
segundosRestantes = SegundosTotal % 3600
minutos = segundosRestantes // 60
segundosFinais = segundosRestantes % 60

print("A duração do evento foi de {} hora(s) {} minuto(s) e {} segundo(s)".format(horas, minutos, segundosFinais))
