idade =  int(input("informe a idade do atleta: \n"))

if 9 <= idade < 14:
    print("Mirim")
elif 14 <= idade <= 19:
    print("Infantil")
elif idade == 20:
    print("senior")
else:
    print('master')