def Reverse(list):
    list.reverse()
    return list
def Reverse2(list):
    list.remove(3)
    list.remove(7)
    return list
def Remove3(set_list):
    set_list.remove(8)
    return set_list

list = [1,2,3,4,5,6,7,8,9,10]
print("Here is the list: ",list)
print("Here is the list reversed:", Reverse(list))
print("Here is that list but without 3 and 7:", Reverse2(list))
set_list = set(list)
print("Here is the list converted to a set:", set_list)
print("Here is the set without 8:", Remove3(set_list))


