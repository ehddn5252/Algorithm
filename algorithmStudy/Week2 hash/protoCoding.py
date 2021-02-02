tuples = [('kim',30), ('han',10), ('min',20), ('han',70), ('min', 90)]
 
def age(t):
    return t[1]
 
def name(t):
    return t[0]
 
tuples.sort(key=age)
print(tuples)
 
tuples.sort(key=name)
print(tuples)
