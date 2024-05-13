lado = int(input("informe o primeiro lado \n"))
lado2 = int(input("informe o primeiro segundo \n"))
lado3 = int(input("informe o primeiro terceiro \n"))

if lado == lado2 and lado == lado3:
    print("Equilatero")
elif lado == lado2 and lado != lado3:
    print("isoceles")
elif lado == lado3 and lado != lado2:
    print("isoceles")
elif  lado3 == lado2 and lado != lado3:
    print("isoceles")
else:
    print("Escaleno")