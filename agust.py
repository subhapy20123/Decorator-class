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