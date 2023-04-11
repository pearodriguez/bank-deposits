GLOBAL_SUM = 0

def main():
    num = int(input('How many deposits would you like to make? '))
    global GLOBAL_SUM
    for num_deposit in range(num):
        deposit = float(input('Enter amount to deposit: $'))
        add(deposit)
    print('your total is: $', format(GLOBAL_SUM, ',.2f'), sep='')

def add (deposit): 
    global GLOBAL_SUM
    GLOBAL_SUM = deposit + GLOBAL_SUM 

main() 
