''' ENTRADA
- ler o nome do aluuno
- ler o número da turma
- ler 3 notas
'''

''' PROCESSAMENTO
calcular média
verificar status (média >= 70 e aprovado)

'''

''' SAÍDA
Mosrtrar a soma das notas
Mostrar a m´dia das notas
Mostra se foi aprovado ou reprovado

'''

nome = input("Nome do aluno")
numeroTurma = int(input("Número da turma"))
nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))

media = (nota1+nota2+nota3)/3

if media >= 7:
  status = "Aprovado"
  
else: 
   status = "Reprovado"

print(f"O aluno(a){nome} da turma {numeroTurma} ficou com a média {media} e foi {status}")
