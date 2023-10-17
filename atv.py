# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida

vel = int(input("digite a velocidade em km/h"))
if vel > int("60"):
    print("você recebeu uma multa por acesso de velocidade")
else:
    print("você está dentro da velocidade permitida")
    