# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.


def find_second(search,target):
    return search.find(target,search.find(target)+1)
danton = "De l'audace, encore de l'audace, toujours de l'audace"
target = 'audace'
print find_second(danton,target)






#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13