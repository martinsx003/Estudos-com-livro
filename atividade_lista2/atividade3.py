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