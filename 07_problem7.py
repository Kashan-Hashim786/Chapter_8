list1 = ["Kashan","Arslan","Almir","Danish","Akram"]

def rem(list1,word):
    n = []
    for item in list1:
        if not(item == word):
            n.append(item.strip(word))
            
    return n
 
print(rem(list1,"an"))