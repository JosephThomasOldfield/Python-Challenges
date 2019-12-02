

variable = "ham"

if variable == "ham":
    print ("nice ham")
elif variable == "cheese":
    print("nice cheese")
else:
    print('not cheese or ham')

for i in range(5):
    print(i)

for i in ['sam', 'bob', 'ian']:
    print(i)

# Range does a lot of the work for us in reference to loops and lists. 
# ''' MultiLineComment '''

# In Iterable lists python takes the first thing from the list.

my_list = []

for i in range(5):
    my_list.append(i)

print(my_list)


# ~FUNCTIONS~

def my_func(a_string):
    print(a_string)

my_func("hello")



def returnfunc(ddstring):
    return ddstring

print(returnfunc("ddd"))



