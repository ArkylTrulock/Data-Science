# i is the variable and its assigned values ranges from 1 to 4 (excluding 5 of course)
# Start number 1 is INCLUDED, end number 5 is NOT included in the code.
for i in range(1,5): 
# Start number 1, variable value plus 1
    for j in range(1,i+1): # Start number 1, i plus 1
        print('*',end='')
    print()

# 3 (our start number) IS included in the code, 0 (our end number) IS NOT  included in the code and -1 is our step backwards.
for i in range(3,0,-1):
# Start number 1, variable value plus 1
    for j in range(1,i+1): 
        print('*',end='')
    print()
