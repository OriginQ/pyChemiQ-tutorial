from pychemiq import FermionOperator
from pychemiq import PauliOperator

# Fermion Operator
a = FermionOperator("0 1+", 2)
b = FermionOperator("2+ 3", 3)
c = FermionOperator("1+ 3 5+ 1",1)

plus = a + b
minus = a - b
multiply = a * b
print("a + b = {}".format(plus))
print("a - b = {}".format(minus))
print("a * b = {}".format(multiply))

print(multiply.normal_ordered())
print("data = {}".format(a.data()))


# Pauli Operator
p1 = PauliOperator()
p2 = PauliOperator("Z0 Z1", 2)
p3 = PauliOperator({"Z0 Z1": 2, "X1 Y2": 3})
p4 = PauliOperator(5)
p5 = PauliOperator("", 5)

a = PauliOperator("Z0 Z1", 4)
b = PauliOperator("X5 Y6", 3)
plus = a + b
minus = a - b
muliply = a * b
print(plus)

a = PauliOperator("Z0 Z1", 2)
b = PauliOperator("X5 Y6", 3)
print(a.get_max_index())
print(b.get_max_index())

print("data = {}".format(a.data()))