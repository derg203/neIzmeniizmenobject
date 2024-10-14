#1
immutable_var = (1,True, 'данил',4.04, ['привет',2,3,4])
print(immutable_var)
immutable_var[4][0]='пока'
print(immutable_var)
# заменить можно только список в самом кортеже как он является заменяемым
#сам кортеж изменить нельзя
#2
mutable_list = ['помидо','огурец','хлеб','колбаса']
print(mutable_list)
mutable_list [0] = 'майонез'
print(mutable_list)
mutable_list.append('бутерброд')
print(mutable_list)
mutable_list.extend(['помидор','буженина'])
print(mutable_list)
mutable_list.remove('помидор')
print(mutable_list)
print(mutable_list[0:4:2])