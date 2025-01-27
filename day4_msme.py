# #IDENTITY OPERATOR
# x=10
# y=10
# print(id(x))
# print(id(y))
# print(x is y)
# print(x is not y)
#
# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
# print(a is b)

#MEMBERSHIP OPERATOR
#


#FOR AND WHILE

name=input("enter any name")

for i in name:
    if i.isupper():
        print(''.join(i),end='')
print('\n')
for j in name:
    if j.islower():
        print(''.join(j),end='')
print('\n')