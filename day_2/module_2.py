'''
Created on 06/02/2018

@author: rita
'''
import utils

def soma_duas_vezes(valor_1,valor_2):
    valor_1 = utils.is_number(valor_1)
    valor_2 = utils.is_number(valor_2)
    return valor_1 + valor_2 if valor_1 != None and valor_2 != None else None 

if __name__ == '__main__':
    
    while True:
        valor = input('Introduz um valor inteiro: ')
        valor = utils.is_number(valor)
        if valor != None: break
        
    if (valor % 2 == 0): print('even')
    else: print ('odd')
    
    pass