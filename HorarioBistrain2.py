import time
print("Este programa otorga la mecanica del Horario Bistrain")
print("Indica las horas y minutos del Horario Bistrain:")

loop = "si"

ss = 0
mm = int(input("Ingresa los minutos: "))
hh = int(input("Ingresa las horas: "))

while loop == "si" or loop == "SI":

	while (ss<60):
		ss+=1
		print ("Hrs:", hh, "Min:", mm,"Seg:", ss)
		time.sleep(1)
		


		if (ss>59):
			ss=0
			mm = mm+1

		if (mm>49):
			mm = 0
			hh = hh+1

		if (hh>= 28.40):
			hh= 0
			mm= 0
			ss= 0

	loop = input("¿Deseas realizar otra operacion? (si/no)")