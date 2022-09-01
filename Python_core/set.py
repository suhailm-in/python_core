number={10,20,30,40,40,50,60}  # duplication note working print one time only (40,40)
print(number)
print(type(number))
# add number
number.add(70)
print(number)
# remove number
number.remove(30)
print(number)


seta={1,2,3,4,5,6}
setb={5,6,7,8,9,0}
print(seta | setb)  # union
print(seta & setb)  # intersept
print(seta - setb)  # defrents a in b
print(setb - seta)  # defrents b in a

