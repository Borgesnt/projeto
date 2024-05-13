idade = int(input('informe sua idade: \n'))

if idade >= 18:
    print("hora de se alistar")
elif idade < 18:
    print("ainda não vai se alistar")
    print("falta exatamente", 18 - idade, " anos para se alistar")