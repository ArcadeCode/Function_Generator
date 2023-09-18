from random import randint
from string import ascii_lowercase

def get_function(xcubeCanBeNegative=False) :
    # Nb generator
    if xcubeCanBeNegative == False :
        a = randint(1,9)
    else :
        a = randint(-9,9)

    b = randint(-9,9)
    c = randint(-9,9)

    # We must have x² and x != 0
    if a == 0 :
        a+=1
    if b == 0 :
        b+=1

    # For get '+' sign when the nb is positive for more read comprehension
    if a >= 0 :
        a = "+"+str(a)
    if b >= 0 :
        b = "+"+str(b)
    if c >= 0 :
        c = "+"+str(c)

    if c == "+0" :
        result = f"{a}x² {b}x"
    else :
        result = f"{a}x² {b}x {c}"
    return result

# Const
gen_nb = 26
gen_x_negative = True # not x but x² : it allow to get negative x² !

# Print result :
print("Écrivez la forme canonique de : ")
for i in range(gen_nb) :
    print(ascii_lowercase[i]+") "+get_function(gen_x_negative))
    '''Print  letter) and the question like : a) x²+x+0'''