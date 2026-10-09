dia_semana = int(input("Digite um Nùmero de 1 a 7 para mostrar o dia da semana -"))
match dia_semana:
  case 1:
    print("Domingo")
  case 2:
    print("Segunda")
  case 3:
    print("terça")
  case 4:
    print("Quarta")
  case 5:
    print("Quinta")
  case 6:
    print("Sexta")
  case 7:
    print("Sábado")
  case _:
    print("Dia inválido!")

