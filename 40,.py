nota = float(input("informe sua primeira nota \n"))
nota2 = float(input("informe sua segunda nota \n "))
media = (nota+nota2)/2

if media <= 5:
    print("reprovado")
elif 5 <= media <7:
    print ("recuperação")
else:
    print("aprovado")
