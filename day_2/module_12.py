'''
Created on 06/02/2018

@author: rita
'''
import utils
import sys
import os

if __name__ == '__main__':
    
    file_name = input('file to sum: ')
    
#     if (not os.path.exists(file_name)):
#         print("File '{}'does not exist".format(file_name))
#         sys.exit(1)
    
    soma = 0
    try:
        with open(file_name) as handle_in:
            for line in handle_in: ## read line by line
                valor = utils.is_number(line)
                if (valor != None): soma += valor
    except:
        print("File '{}'does not exist".format(file_name))
        sys.exit(1)
            
    print('Sum: {}'.format(soma))