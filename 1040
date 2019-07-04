entrada = input().split(" ")

nota1, nota2, nota3, nota4= entrada

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = float(float((nota1 * 2)+ (nota2 * 3) + (nota3 * 4) + (nota4 * 1))/10.0)

if media > 7.0:
  print("Media: %.1f\nAluno aprovado."%media)
elif 5.0 < media < 6.9:
  print("Media: %.1f\nAluno em exame."%media)
  notaExame = float(input("Nota do exame: "))
  final = float((media + notaExame)/2)
  if final > 5.0:
    print("Aluno aprovado.\nMedia final: %.1f"%(final))
  else:
    print("Nota do exame: %.1f\nAluno reprovado."%media)
else:
   print("Media: %.1f\nAluno reprovado."%media)  
