A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# A∩D
print(A.intersection(D))
# B∩D
print(B.intersection(D))
# C∩D
print(C.intersection(D))
# A∩B∩C∩D
print(A.intersection(B).intersection(C).intersection(D))