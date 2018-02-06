'''
Created on 06/02/2018

@author: rita
'''
def is_number(valor):
    """
    
    """    
    try:
        return int(valor)
    except:
        return None

def is_float(valor):
    """
    param: any value
    return: float
    """    
    try:
        return float(valor)
    except:
        return None
