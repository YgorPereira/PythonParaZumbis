state = ('''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.''').lower()
state = state.replace(',', '')
state = state.replace('.', '')
state = state.split()
python = []

for x in state:
    if x[0] == 'p' or x[0] == 'y' or x[0] == 't' or x[0] == 'h' or x[0] == 'o' or x[0] == 'n':
            python.append(x)
    if x[-1] == 'p' or x[-1] == 'y' or x[-1] == 't' or x[-1] == 'h' or x[-1] == 'o' or x[-1] == 'n':
            python.append(x)
print(python)
