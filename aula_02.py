# Condicionais

'''
IF -> 
ELIF ->
ELSE ->

----

# setar variavel
projeto_aula_01_concluido = False

if projeto_aula_01_concluido == True:
  print('Muito bem, será remunerado! :)')
else:
  print('Volte ao trabalho, ainda não terminou!!!')

-----

estou_livre = True

if estou_livre == True:
  print('Posso te ajudar agora.')
else:
  print('Desculpe, peça ao meu irmão para te ajudar...')

'''

'''
# cheguei atrasado, apos 3x nao poderei entrar e serei suspenso

estou_atrasado = True
numero_atraso = 3

if estou_atrasado == True:
    atraso = numero_atraso + 1
    print('vou verificar, se for 3x estará suspenso!')

if atraso <= 3:
    print('Ufa, pode entrar!')

else:
    print('Você está suspenso!!')
'''

# cheque aprovacao aluno
print("digite decimal exemplo '4.4','6.7', separado por vírgulas.")

#receber notas
nota_math = input('Qual sua nota Matemática? ')
nota_physic = input('Qual sua nota Física? ')
nota_psycology = input('Qual sua nota Psicologia? ')
nota_geografic = input('Qual sua nota Geografia? ')
nota_english = input('Qual sua nota Inglês? ')

media_total = int(6)


#somar notas
total_nota = int(nota_english) + int(nota_geografic) + int(nota_math) + int(nota_physic) + int(nota_psycology)

#transformar em um variavel boleana
materias = 5

#tirar media das notas
media = total_nota / materias


if media >= media_total:
  print("Parabéns, você passou de série! sua média foi "); print(media)

if media < media_total:
  print("Desculpe, você não foi aprovado(a)! Sua média foi "); print(media)
  
