sexo = str(input("informe seu sexo: \n")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("dados invalidos pfv informe seu dados ")).strip().upper()[0]
print ("sexo {} registrado com sucesso ".format(sexo))