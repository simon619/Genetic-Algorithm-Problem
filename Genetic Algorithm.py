# Pardon Me,
# Random Library Has A Bug. If You See 'Infinite ERROR' or 'Index Error' In Output, Please Rerun The Program.
# The Program Takes Input From Text File. The Transactions In The Text File Must Be Started From 2nd Line.
# Python Interpreter In Google Colab May Not Work Well With "quit()" Function.
import random
adj = []
with open('Your_Text_Input_File.txt') as textfile:
    for line in textfile:
        adj_row = [item.strip() for item in line.split(' ')]
        adj.append(adj_row)

print(adj)


def heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[largest] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


def heap_sort(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        heapify(A, len(A), i)

    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


info_list = []
list_of_shame = [[]]
counter = 1
m = 1
while m < len(adj):
    if adj[m][0] == 'l':
        info_list.append(int('-' + adj[m][1]))
    else:
        info_list.append(int(adj[m][1]))
    m += 1

print('Transactions: %s' % info_list)
impossible = (2 ** len(info_list)) + 1  # More Efficient Than 10 ** 5
bin_list = []
if len(info_list) <= 5:
    point = 2
else:
    point = 3

if len(info_list) >= 10 ** 2:
    print('The Transaction Is Too Much Big')
    print('-1')
    quit()

if len(info_list) <= 1:
    print('The Transaction Is Too Much Small')
    print('-1')
    quit()


def generate_bin_list(S):
    print('ERROR')
    for k in info_list:
        S.append(random.randint(0, 1))
    if 0 not in S:
        generate_bin_list(S)
    if 1 not in S:
        generate_bin_list(S)
    if len(bin_list) != 0:
        if S in bin_list:
            generate_bin_list(S)
    bin_list.append(S)


(A, B, C, D) = ([], [], [], [])
generate_bin_list(A)
generate_bin_list(B)
generate_bin_list(C)
generate_bin_list(D)
print('Initial State: %s' % bin_list)
print('')


def mutation():
    global counter
    r = 0
    while r < 4:  # Number of Selection Was Four. Also Can Be Written as len(bin_list)
        x = random.randint(0, len(info_list) - 1)
        y = random.randint(0, 1)
        bin_list[r][x] = y
        if len(list_of_shame) != 0:
            if bin_list[r] not in list_of_shame:
                list_of_shame.append(bin_list[r])
        # print('Shame %s' % list_of_shame)    # All The Mutation Record
        if len(list_of_shame) >= impossible:
            print('No Solution Found in %d Combinations' % (impossible - 1))
            list_of_shame.pop(0)
            print('List of Combinations %s' % list_of_shame)
            print('-1')
            quit()
        r += 1
    print('Mutation: %s' % bin_list)
    counter += 1
    print('')
    print('')
    fitness_function()


def selection_and_crossover():
    global counter
    temp0 = bin_list[0].copy()
    temp1 = bin_list[2].copy()
    bin_list[2] = temp0
    bin_list[3] = temp1
    print('Section: %s' % bin_list)
    for i in range(point, len(info_list)):
        bin_list[0][i], bin_list[1][i] = bin_list[1][i], bin_list[0][i]
    for j in range(point + 1, len(info_list)):
        bin_list[2][j], bin_list[3][j] = bin_list[3][j], bin_list[2][j]
    print('Crossover: %s' % bin_list)
    mutation()


def fitness_function():
    global counter
    print('Engineering Number: %d' % counter)
    dict = {}
    i = 0
    while i < len(bin_list):
        if 1 not in bin_list[i]:
            o = random.randint(0, len(info_list) - 1)
            bin_list[i][o] = 1
        else:
            pass
        count = 0
        for j in range(len(bin_list[i])):
            if bin_list[i][j] == 1:
                ind = j
                count = count + info_list[ind]
            else:
                pass
        if count == 0:
            result = ''.join(str(s) for s in bin_list[i])
            print('Output: %s' % result)
            quit()
        else:
            dict[abs(count)] = bin_list[i]
            i += 1
    sorting = []
    for k in dict.keys():
        sorting.append(k)
    heap_sort(sorting)
    for i in sorting:
        bin_list.pop(0)
        bin_list.append(dict[i])
    print('Fitness Function: %s' % bin_list)
    selection_and_crossover()


fitness_function()
