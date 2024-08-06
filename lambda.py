# # # # multiply=lambda x,y:x-y

# # # # data=multiply(500,60)

# # # # print("lambda output"+str(data))
# # # # name=multiply(100,50)

# # # # print(name)

# # # # from functools import reduce

# # # # multiply=lambda x,y:x**y

# # # # data=multiply(10,7)

# # # # print("lambda output"+str(data))
# # # # name=multiply(2,4)
# # # # print(name)

# # # #zzzzzzzzzzzzzzz
# # # # from abc import ABC,abstractmethod
# # # # class laptop(ABC):
# # # #     def display(self):
# # # #         pass


# # # # class sels (laptop):
# # # #     def display(self):
# # # #         print("lenovo laptop is sels")


# # # # class price(laptop):
# # # #     def display(self):
# # # #         print(" this laptop price 6000")


# # # # class office(laptop):
# # # #     def display(self):
# # # #         print("hed office kolkata")


# # # # s=sels()
# # # # s.display()

# # # # p=price()
# # # # p.display()


# # # # o=office()
# # # # o.display()


# # # list = [33, 40,23,6,45,140,7,8,9,90,56,43,2,1,3,]

# # # data = []

# # # for n in list:
# # #    if n % 2 == 0:
# # #       data.append(n)
# # # print(data)


# # # a=(1,2,3,4,5,6,7,8,10,14,56,37,80,36,)

# # # print("even number from the side list")
# # # even_a=list(filter(lambda x:x%2==0,a))
# # # print(even_a)

# # # print("odd number from the side list")
# # # odd_a=list(filter(lambda x:x%2!=0,a))
# # # print(odd_a)


# # t=[3,5,6,80,48,35,89]
# # print("this is orginal list")
# # print(list)

# # print("even number side list")
# # even_t=list(filter(lambda x:x%2==0,t))
# # print(even_t)

# # print("odd number side list")
# # odd_t=list(filter(lambda x:x%2!=0,t))
# # print(odd_t)




# # numbers = {1, 2, 3, 4}
# # result = map(lambda x: x+x, numbers)
# # print(result)

# # # convert to set and print it
# # print(list(result))

list_name=["rajuz","somnath","biswnath","subho"]
unique_name=list(set(list_name))
print(unique_name)
result_map=map(lambda x:x.lower(),list_name)
print("result_map",list(result_map))
lower_name=list(result_map)
return_sort=sorted(lower_name,reverse=True)
lower_name.sort(reverse=True)
print("ruselt_map sort",lower_name)
print("return_sort",return_sort)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a"in x:
#     newlist.append(x)

# print(newlist)



































































