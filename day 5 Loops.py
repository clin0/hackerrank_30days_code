n = int(input())

for i in range(1,11):
    result = n * i
    print('{} x {} = {}'.format(n, i, result))


"""
#this is the first round. Things work but could be better
n = int(input())
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    result = n * i
    print(str(n) + " x " + str(i) + " = " + str(result))

# moral of the story. 
#  Use range function to show a list of numbers.
#  Use .format() method to display results

# For time control purpose. 7'12 min complated the tast.
"""