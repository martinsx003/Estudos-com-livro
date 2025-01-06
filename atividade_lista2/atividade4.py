convidados = ['joao','stefani','violet',]

print (convidados)
print("\n ======================== \n")

print (f'parabens {convidados[0].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[1].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[2].title()} voce foi convidado para uma festa de aniversario!\n')

print (f"rapaz... o {convidados[0].title()} deu mole, ele nao vai vir para a festa!")

convidados[0] = 'Julia'

print (f'\nparabens {convidados[0].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[1].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[2].title()} voce foi convidado para uma festa de aniversario!')

print ("\n")

print("rapaziada, achei um salao maior pra fazer a festa de aniversario!\n")
convidados.insert(0, 'kawan')
convidados.insert(2, 'mirely')
convidados.append('tiffany')

print (convidados)

print (f'\nparabens {convidados[0].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[1].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[2].title()} voce foi convidado para uma festa de aniversario!')
print (f'\nparabens {convidados[3].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[4].title()} voce foi convidado para uma festa de aniversario!\n')
print (f'parabens {convidados[5].title()} voce foi convidado para uma festa de aniversario!')

print ("\n")
print ("rapaziada, pessima noticia, cancelaram o salao, agora a festa vai ser na goma do pai, e la so pode ir duas pessoas\n")

cancelados = convidados.pop()

#print (cancelados)

print(f'perdao {cancelados} infelizmente nao vai dar pra voce vir!\n')

cancelados = convidados.pop(0)

print(f'perdao {cancelados} infelizmente nao vai dar pra voce vir!\n')

cancelados = convidados.pop(1)

print(f'perdao {cancelados} infelizmente nao vai dar pra voce vir!\n')

cancelados = convidados.pop(0)

print(f'perdao {cancelados} infelizmente nao vai dar pra voce vir!\n')

print (f"{convidados[0].title()} moio pro resto do pessoal mas pra gente ainda tem!\n")
print (f"{convidados[1].title()} moio pro resto do pessoal mas pra gente ainda tem!\n")

del convidados[0]
del convidados [0]
print (convidados)