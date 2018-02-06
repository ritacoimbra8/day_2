'''
Created on 06/02/2018

@author: rita
'''
import utils
import sys

if __name__ == '__main__':
    
    max = None
    min = None 
    soma = 0
    len_vect = 0
    while True:
        number = input('float number? ')
        number = utils.is_float(number)
        if (number != None):
            if (number == 0.0): break
            len_vect += 1
            if (max == None or max < number): max = number
            if (min == None or min < number): min = number
            soma += number
            
    if (len_vect == 0):
        print('No value in vector')
        sys.exit(0)
                
    
        
    print('Max: {} Min: {} Average: {}'.format(max,min,soma/len_vect))
    pass