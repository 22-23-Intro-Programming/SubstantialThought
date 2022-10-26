'''def Factorial(x):
    
    if x == 1:
        return 1
    else:
        return (x * Factorial(x-1))
    
num = int(input("Enter a number: "))

result = Factorial(num)

print("The factorial of" + num + "is" + result + '.')



def Double(x):

    word = int(input("Enter a word bruh: "))

    result = Double(word)

    for i in range(len(x)):
        doubl = ''
        dub = ''
        doubl= x[i] *3
        dub += doubl
        print(dub)'''

def camelCase():

    cC = ''
    print(cC)

newC = int("Enter a file name bro: ")

result = camelCase(newC)
    
print(newC)

for i in range(20):
    print(i)

    print(cC)
       
    i = 0
    while (len(newC > 10)):
            print(newC[i])
            if newC[i] == " ":
                newC.replace(newC[i], '-')
            i = i+1

    i = 0
    while (len(newC > 10)):
            print(newC[i])
            if newC[i] == "-":
                newC.replace(newC[i], '/')
            i = i+1

    newC = newC.capitalize()

    print(newC)

def main():

    '''print(Factorial)'''

    '''print(Double)'''

    print(camelCase)








if __name__ == "__main__":
    main()
