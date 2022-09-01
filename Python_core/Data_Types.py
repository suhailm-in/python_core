
# Data Type List

list1=[12,24,37,"hello world","how are you","wellcome"]
#     [ 0, 1, 2,"     3     ","     4     ","   5    "]
#     [-6,-5,-4,"    -3     ","    -2     ","  -1    "]

print(list1)
print(list1[0])   # answer "12"
print(list1[2])   # answer "37"
print(list1[-1])  # answer "wellcome"

#Q how meny items in "list1" ? (lenght)
print(len(list1)) # answer "6"

#Q which data type "list1"
print(type(list1)) # answer "<class 'list'>"

#---------------------------------------------------------------

list11=[1,2,3,4,5]
list12=[6,7,8,9,0]
print(list11+list12)
# answer [1,2,3,4,5,6,7,8,9,0]

#---------------------------------------------------------------

list21=[20,60,80,208,684]
list21[2]=497
print(list21)