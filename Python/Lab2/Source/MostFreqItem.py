import numpy as np
vec = np.random.random_integers(0,20,15)
print(vec)
# creates a vector of size 21
vec_mod = [0]*21

# iterate over vector and increment value at each index in vec_mod by 1
for i in vec:
    vec_mod[i] += 1

# print(vec_mod)

# index with max value in vec_mod is most frequent item
max = 0
for i in range(1,21):
    if vec_mod[max] < vec_mod[i]:
        max = i

print(max)



