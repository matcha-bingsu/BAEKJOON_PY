#최댓값

lis = []
for i in range(9):
    lis.append(int(input()))
print(max(lis), lis.index(max(lis)) + 1, sep='\n')