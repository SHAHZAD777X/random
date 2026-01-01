# ACP-check the frequency of value x in dictionary
dict1 = {'Welcome': 10,'to': 2,'my': 10, 'class' :10}

print("DICTIONARY:" + str(dict1))
x = int(input("Enter the number to check frequency :"))
res = 0
for key in dict1:
    if dict1[key] ==x:
        res = res +1

print("frequency of x:" +str(res))