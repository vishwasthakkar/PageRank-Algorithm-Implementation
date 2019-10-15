import math
import operator
from collections import defaultdict

P = defaultdict(list)

vertices_file = open('vertices-edu.txt','r')
vertices_file_read = vertices_file.readlines()

for line in vertices_file_read:
    names = line.split()
    P[int(names[0])] = names[1]

N = len(P)

file = open('edges-edu.txt','r')
file_read = file.readlines()

#Before we move on to the algorithm we must first construct our data structures
#First we construct the incoming links data structure and the number of pages
M = defaultdict(list)

for line in file_read:
    element = line.split()
    M[int(element[1])].append(int(element[0]))


#Now we initialize 'L' (ie Number of out-links from a particular page) using P
L = {}
for p in P.keys():
    L[p] = 0


for values in M.values():
    for value in values:
        L[value] += 1

# print(M)
# print(P)
# print(N)
# print(L)


# Constructing a data structure for storing sink nodes
S = []
for node in L:
    if L.get(node) == 0:
        S.append(node)
# print(S)

# The last data structure we need is d
d = 0.85

# Initializing Page ranks to 1 / N
PR = {}

for p in P:
    PR[p] = 1.0 / N
# print(PR)
print("Data Structures created...")
print("Starting iterations...\n\n")

def calculate_perplexity():
    entropy = 0
    for page in PR.keys():
        entropy += PR[page] * math.log(PR[page], 2)
    entropy = -entropy
    return 2 ** entropy


def test_convergence(j):
    perp_val = calculate_perplexity()
    perplexity.append(perp_val)
    if len(perplexity)>4:
        if(int(perplexity[j]))==(int(perplexity[j-1]))==(int(perplexity[j-2]))==(int(perplexity[j-3])):
            # print(calculate_perplexity())
            return False
        else:
            return True
    else:
        return True

newPR = {}
perplexity = []
iteration = 0
# while test_convergence(iteration): #while convergence

write_file = open('PerplexityValues.txt','a')

# while iteration < 100:
while test_convergence(iteration):
    print("Doing Iteration: " + str(iteration + 1))
    sinkPR = 0
    for p in S:
        sinkPR += PR[p]
    for p in P:
        newPR[p] = (1.0 - d) / N
        newPR[p] += d * sinkPR / N
        for q in M[p]:
            newPR[p] += d * PR[q] / L[q]
    for p in P:
        PR[p] = newPR[p]

    iteration += 1

# print("\n\n")
# print(perplexity)
count = 0
for value in perplexity:
    write_file.write("Iteration: " + str(count + 1) + "\t" + str(value) + "\n")
    count += 1

totalPR = 0
for value in PR.values():
    totalPR += value

print("-------")
print(totalPR)
# print('***********')
# name = open('', r)
# print('----------')
# print(perplexity)

# print(float(len(S)) / float(N))

# name_file = open('task#1-graph.txt','r')
# name_read = name_file.readlines()
#
# name = {}
# for vertice in name_read:
#     v = vertice.split()
#     name[v[0]] = v[1]
#
#
# # print(name)
# SortedPR = sorted(PR.items(), key=operator.itemgetter(1), reverse=True)
#
# write_file = open('task#1.txt','a')
# write_file.write("\n\n")
# for value in SortedPR:
#     write_file.write(str(value[0]) + "\t" + str(name[value[0]]) + "\t" + str(value[1]) + "\n")
    # write_file.write(name[value[0]])
    # write_file.write(value[1])

