#rstrip exclui o espaco do lado direito
#lstrip exclui o espaco do lado esquerdo 
#strip exclui o espaco de ambos os lados


linguagem_favorita = 'python ' #aqui criamos uma string com um espaco no final

print (linguagem_favorita) #aqui nos mostra o print com o espaco no final da string
print (linguagem_favorita.rstrip()) #ja aqui nao temos mais espaco pois usamos o rstrip para remover o espaco do fibal da palavra, porem como esse metodo 
#é utilizado no print ele n sera armazenado para o proximo print, sendo necessario o uso do rstrip dnv, caso queira solucionar isso, utilize o .strip para
#sobrecresver o valor da variavrl assim como é feito no exemplo 1, fazendo isso é so solicitar o print com a variavel ja sobrescrita que nao tera mais espavos
print (linguagem_favorita)


linguagem_favorita1 = 'java '
linguagem_favorita1 = linguagem_favorita1.rstrip() #exemplo 1
print  (linguagem_favorita1)