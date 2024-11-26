bonus_constante = 1000

nome = input("Olá, qual é o seu nome: ")
print(f"Seja bem vindo {nome}")

salario = float(input("Qual é o valor do seu salario: "))
bonus_recebido = float(input("Qual o bonus calculado: "))
bonus = bonus_constante + salario * bonus_recebido 

print(f"Olá {nome}, o seu bonus é de: R${bonus}")