# creating tuples with diffrent types:
tuplex = ("tupple", False, 3.2, 1)
print(tuplex)

# create a tuple:
tuplex = (4, 6, 8, 2, 3, 1)

# Tupples are immutable so you can't change them:
# Using merge of tupple using the + operator:
tuplex = tuplex + (9,)
print(tuplex)
 
# counts the occurence of 50 in the tupple
tupple1 = (50, 10, 60, 70, 50)
print(tupple1.count(50))

# create a tupple
tupplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# used tuple[star: stop] the start index is inclusive so is the stop
_slice = tupplex[3 : 5]

# is exclusive
print(_slice)

# if the start index is defined, is taken from the beg inng of the tupple
_slice = tupplex[:6]
print(_slice)                           


# Palemdronme number:
def palind(r):
    e = len(r) -1
    s = 0
    while(s < e):
        if(r[s] != r[e]):
            return False
        s += 1
        e -= 1
        return True

r = (1,2,3,3,2,1)

if palind(r):
    print("The tuple IS A flip-flop")
else:
    print("The tuple is NOT a flip-flop")

# Wether prediction:
wether = (1, 1, 1, 0, 1, 1, 0)
sunny = 0
rainy = 0

for i in range(0, 7):
    if(wether[i] == 0):
        rainy +=1
    else:
        sunny += 1

if sunny > rainy:
    print("Good wether today :)")
else:
    print("Bad wether today :(")