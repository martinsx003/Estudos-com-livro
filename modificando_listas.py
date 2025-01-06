motos = ['bmw','honda','yamaha','suzuki'] #aqui criamos a lista
print (motos)

motos[0] = 'ducati' #aqui modificamos a lista utilizando o indice (no caso [0]) = e adicionando o novo valor 'ducati'
print("\n")
print (motos)

motos.append('triumph') #aqui adicionamos um novo item a lista usando o metodo .append 
print (motos)

motos.insert(0, 'peugeot') #aqui adicionamos um novo item a lista usando o metodo .insert() que é necessario especificar o indice que deseja que o item fique
print (motos)

del motos[2]# para deletarmos um item da lista usamos o meotodo del antes do nome da lista e o indice que deseja deletar
print (motos)

#aqui comecamos a usar o metodo pop(), que serve para deletar o ultimo item da lista, so que nesse caso podemos ter acesso a esse item excluido depois
#por exemplo como acontece aqui embaixo 

ultima_motos = motos.pop() # nesse caso removemos a moto triumph

print (motos)
print (ultima_motos)
print (motos)

print("\n")
print (f"a ultima moto que eu comprei é da marca {ultima_motos}!\n")

desejada = motos.pop(1) #aqui utilizamos o metodo pop() porem com o indice especificado, nesse caso foi o indice 1

print (f"\n {motos}\n")

print (f"tenho vontade de comprar uma moto da {desejada.title()}!\n")

        #sempre que o metodo pop for usado o item que for deletado nao fara mais parte da lista, por isso colocamos o item em outro variavel


#caso nao saiba o indice que deseja remover mas saiba o conteudo dele, podemos usar o metodo remove(), exemplo: motos.remove(ducati)
motos.remove('yamaha')
print (motos)

            #tambem podemos usar o metodo remove() para removermos um item que faz parte da lista e de uma variavel, por exemplo:
            #quando a moto é muito cara ela vai para a varival moto_cara, ai quando quisermos remover o item que esta classificado 
            #como uma moto cara, usamos o remove(moto_cara)

moto_cara = 'suzuki'
motos.remove(moto_cara) #aqui mesmo removendo o item da lista ele continua disponivel na variavel moto_cara
print (motos)
print ("\n")
print (f'nao irei comprar alguma moto da {moto_cara.title()} pq sao caras dms!')

