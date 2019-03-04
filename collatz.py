#Type in a number,and this program will call the Collatz function until the number is 1
def collatz(number):
    while number!=1:
        if number%2==0:
            number=number//2
            print(number)

        else:
            number=3*number+1
            print(number)


num=int(input('Insert number: '))
collatz(num)
        
