peso = float(input("infome seu peso \n"))
altura = float(input("informe sua altura \n"))
imc = peso / (altura ** 2)
print(imc)
if 18.50 > imc:
    print("abaixo do peso ")
elif 18 >= imc <25 :
    print("ideal")
elif 25 >= imc <30:
    print ("sobre peso")
elif 30 >= imc <40:
    print("obesidade")
elif imc >= 40:
    print("obesidade mórbida")
    