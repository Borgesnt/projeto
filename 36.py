valordacasa = int(input("informe o valor da casa: \n"))
salario = int(input("informe seu salário: \n"))
quantosanos = int(input("quantos anos o senhor deseje pagar? \n"))
percentual = 30
prestação = salario*(percentual/100)
resto = salario - prestação
valormensal = valordacasa/quantosanos
if valormensal > resto :
    print("impresto negado")
else:
    print( "impresto aprovado")