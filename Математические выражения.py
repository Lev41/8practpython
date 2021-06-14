from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

add = 'add'
mul = 'mul'

fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

a, b = var('a'), var('b')

Original_pattern = (mul, (add, 5, a), b)

exp1 = (mul, 2, (add, 3, 1))
exp2 = (add, 5, (mul, 8, 1))
exp3 = (mul, (add, 5, a), b)
exp4 = (mul, (add, 5, a), 2)

print(run(0, (a,b), eq(Original_pattern, exp1)))
print(run(0, (a,b), eq(Original_pattern, exp2))) 
print(run(0, (a,b), eq(Original_pattern, exp3)))
print(run(0, (a,b), eq(Original_pattern, exp4)))