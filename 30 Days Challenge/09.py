N = int(raw_input().strip())
phonebook = {}

for i in range(N):
    name,num = raw_input().strip().split(' ')
    phonebook[name]=num

while(True):
    try:
        queryName = raw_input().strip()
        if queryName in phonebook:
            print('{}={}'.format(queryName, phonebook[queryName]))
        else:
            print('Not found')
    except EOFError:
        break
