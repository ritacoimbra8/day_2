'''
Created on 06/02/2018

@author: rita
'''

def fibonacci(value):
    
    if (value < 2): return 1
    
    value_1 = 0
    value_2 = 1
    for i in range(2, value+1):
        return_value = value_1 + value_2
        print('i {} value_1 {}   value_2 {}  soma: {}'.format(i, value_1,\
                    value_2,return_value))
        value_1 = value_2
        value_2 = return_value
        
    return return_value    
        
if __name__ == '__main__':
    
    print(fibonacci(10))