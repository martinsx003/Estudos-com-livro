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