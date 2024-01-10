list1=[2,3,5,6,8,49,13,28]
list2=[11,31,4,18,24,22,14,9]
print("List1:",list1)
print("List2:",list2)

print("Length of List1:",len(list1))
print("Length of List2:",len(list2))
if len(list1)==len(list2):
    print("The length of the lists are same")
else:
    print("The length of the list are not same")

print("Sum of the list1:",sum(list1))
print("Sum of the list2:",sum(list2))
if sum(list1)==sum(list2):
    print("The sum of the Lists are same")
else:
    print("The sum of the Lists are not same")

check=any(item in list1 for item in list2)
print("Any value occur in both:",check)
