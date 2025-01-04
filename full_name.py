primeiro_nome = "stefani" #variavel com primeiro nome
segundo_nome = "murari" #variavel com segundo nome
nome_completo = f"{primeiro_nome} {segundo_nome}" # variavel recebe o valor das duas variaveis citadas

print (nome_completo) 

print ("========================================")

primeiro_nome1 = "joao"
segundo_nome1 = "vitor"
nome_completo1 = f"{primeiro_nome1} {segundo_nome1}" 

print (f"Ola, {nome_completo1.title()}!") #exibe o resultado do print porem usando o metodo title e usando o texto colocado direto dentro do print

print ("========================================")

primeiro_nome2 = "violet"
segundo_nome2 = "murari"
nome_completo2 = f"{primeiro_nome2} {segundo_nome2}"
mensagem = f"Ola, {nome_completo2.title()}!" #aqui passamos toda informacao para uma variavel para nos facilirar nas futuras chamadas do print com o texto escolhido

print (mensagem) #aqui a chamada do print é simplificada


print ("\tcom espaco") #o \t adiciona um espaco antes do texto, pode ser interpretado como um tempo antes do texto 

print ("pessoas: \n \nSte \nJoao \nViolet ") #o \n para adicionar uma quebra de linha 

print ("pessoas: \n \n\tSte \nJoao \n\tViolet ") #o \n para adicionar uma quebra de linha, tambem pode se combinado com o \t dando um espaco antes da palavra
