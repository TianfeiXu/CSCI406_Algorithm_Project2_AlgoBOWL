import random

test_file = open('input.txt','w')

count = 1000


test_file.writelines("1000")
test_file.writelines('\n')

arr = []

i = 0

while i < 1000:
    if i < 300:
        x = random.randint(2,1000)
    elif i < 600:
        x = random.randint(1000,1000000)
    elif i < 1000:
        x = random.randint(1000000,1000000000)
        
    if x not in arr:
        arr.append(x)
        i = i + 1

arr.sort()

print(arr)

for i in range(len(arr)-1):
    test_file.writelines(str(arr[i]))
    test_file.writelines(' ')

test_file.writelines(str(arr[len(arr)-1]))
print(len(arr))
test_file.close()


# test_file = open('input.txt','r')
# values = test_file.readlines()
# for value in values:
#     print(value.split(' '))
