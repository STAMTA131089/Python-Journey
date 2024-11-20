#alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
# 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(orignial_text,shift_amount):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = []
    for a in orignial_text:
        index_of_char = alphabets.index(a)
        shift_index = 26-(index_of_char + shift_amount)
        #print(shift_index)
        l.append(alphabets[-shift_index])
    
    result = ""
    for x in l:
        result += x

    print(result)

def decrypt(orignial_text,shift_amount):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = []
    for a in orignial_text:
        index_of_char = alphabets.index(a)
        shift_index = 26-(index_of_char - shift_amount)
        #print(shift_index)
        l.append(alphabets[-shift_index])
    
    result = ""
    for x in l:
        result += x

    print(result)    
        
#encrypt("shailender",2)
decrypt("ujckngpfgt",2)