A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# A U B
print(A.union(B))
# B U C
print(B.union(C))
# B U C U D
print(B.union(C).union(D))
# A U B U C U D
print(A.union(B).union(C).union(D))