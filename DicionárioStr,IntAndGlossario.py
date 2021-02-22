#Dicionarios
Informações = {
               'Nome'     :   'Paola'       ,
               'Sobrenome':   'Caçarrolha'  ,
               'Idade'    :   '40'          ,
               'Cidade'   :   'SP'
              }

print('Seu nome é: '        +  Informações['Nome']
     )
print('Seu sobrenome é: '   +  Informações['Sobrenome']
     )    
print('Sua Idade é: '       +  Informações['Idade']
     )
print('Sua Cidade é: '      + Informações['Cidade']
     )



#Dicionarios com numeros inteiros é necessario converter de str para int.
Numeros = {'Carlos'  : 1,
           'Roberto' : 2,
           'Maria'   : 3          
          }

print('O Carlos é o numero: ' + str(Numeros['Carlos']))
print('O Roberto é o numero ' + str(Numeros['Roberto']))            
print('A Maria é o numero: '  + str(Numeros['Maria']))



#Glossário de termos
Aprendizado = {'elif-if-else':'Atributos de condição',
               'pop'    :'o termo de lista pop remove o ultimo item da lista',
               'del'    : 'o del remove um item em espécifico em uma lista',
               'append' : 'O append acrescenta um item ao final de uma lista',
               'insert' : 'O insert acrescenta na posição que preferir'
              }

print('\nPop: '  + Aprendizado['pop']    +
      '\nDel: '  + Aprendizado['del']    +
      '\nAppend' + Aprendizado['append'] +
      '\nInsert:'+ Aprendizado['insert']
     )

