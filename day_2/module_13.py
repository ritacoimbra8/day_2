'''
Created on 06/02/2018

@author: rita
'''

if __name__ == '__main__':
    
    dict = {}
    ## open file
    with open('pg3333.txt') as handle_in:
        for line in handle_in: # read line by line
            #line = line.rstrip()
            for word in line.split():
                word = word.strip() # clean spaces and line feed begin and end
                for char in word:
                    print(char)
                print(len(word))
                print(word.isalpha())
                if (len(word) == 0 or not word.isalpha()): continue
                word = word.lower()
                if word in dict: dict[word] += 1
                else: dict[word] = 1
    
    ## print dictionary    
    print('#number words: ' + str(len(dict))) 
#    sum_words = 0             
#     for key in dict:
#         print(key, dict[key])
#         sum_words += dict[key]
#     print('total words: ' + str(sum_words))

    dict_value = {}
    for key in dict:
        if dict[key] in dict_value: dict_value[dict[key]].append(key)
        else: dict_value[dict[key]] = [key]  
                         
    count = 0
    for sorted_key in sorted(dict_value.keys(), reverse=True):                     
        print(sorted_key, dict_value[sorted_key])
        count += 1
        if (count > 10): break
        
        
            