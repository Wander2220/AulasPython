segundos = float(input("Digite a quantidade de segundos:"))

dias = segundos / 84.400
horas = segundos / 3.600
minutos = segundos / 60

print("%.3f segundos é igual a %.0f dia(s)" % (segundos, dias))
print("%.3f segundos é igual a %.1f hora(s)" % (segundos,horas))
print("%.3f segundos é igual a %.3f minuto(s)" % (segundos, minutos))
