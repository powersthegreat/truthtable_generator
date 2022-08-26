variables = ["p", "q", "r"]
equations = ["p  q", "True", "p+q+r"]
joined = variables + equations
p = True
q = False
print(eval(equations[0]))

# print(p + (not q))