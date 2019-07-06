'''def rev(arr):

    list1 =  reversed(list(arr))
    return "".join(list1)
a = rev("geeks")
print(a)

str = "ankita"
print(list(str))'''

def rever(str):
    reverseddd =""
    for val in str:
        reverseddd = val + reverseddd
        print(reverseddd)
    
    return reverseddd
b = rever("ankita")
print(b)

