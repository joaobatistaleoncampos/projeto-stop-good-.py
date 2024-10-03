print(" STOP GOOD")
print(" 1- coxinha R$ 2,00")
print(" 2- rissoles R$ 2,00")
print(" 3- bolinho de frango R$ 2,00")
print(" 4- fogazza R$ 2,00")
print("BEBIDAS")
print(" 5- refrigerante R$ 5,00 ")
print(" 6- suco R$ 5,00")
print(" ok- SAIR")

total = 0
while True:
   op = int(input("escolha qual opção"))

   if   ( op == 1):
        qtd =int(input("unidades?"))
        total = total + qtd * 2.00
   elif ( op == 2):
        qtd =int(input("unidades?"))
        total = total + qtd * 2.00
   elif ( op == 3):
        qtd =int(input("unidades?"))
        total = total + qtd * 2.00
   elif (op == 4):
        qtd = int(input("unidades?"))
        total = total + qtd * 2.00
   elif (op == 5):
        qtd = int(input("unidades?"))
        total = total + qtd * 5.00
   elif (op == 6):
        qtd = int(input("unidades?"))
        total = total + qtd * 5.00
   elif(op== 10):
        break

print(f" o total a ser pago é R${ total} volte sempre!!")