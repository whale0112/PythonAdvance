f = open("새파일.txt", 'w')

for i in range(1, 11):
    data = '{}번째 줄.\n'.format(i)
    f.write(data)

f.close()

f = open('새파일.txt', 'r')

lines = f.readlines()
for line in lines:
    print(line)

f.close()
