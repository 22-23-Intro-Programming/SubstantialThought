Python 3.11.0a5 (v3.11.0a5:c4e4b91557, Feb  3 2022, 14:54:01) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def name():
    nameInput = input('What is your name?')
    if nameInput == ('Mr. Considine'):
        print('Nice to meet you! Give me an A.')
    else: print('Nice to meet you! Have a nice day!')

    
def isMultiple(x,y):
    
    x = int(x)
    y = int(y)
    result = x / y
    if x mod y = 0:
        print(x + "is a multiple of" + y)
    else: print(x + "is not a multiple of" + y)
    

def palindrome(word)

    return word == word[::-1]

    word = "Racecar"
    res = isPalindrome(word)
 
if res:
    print("Congratulations! Your word is a palindrome!")
else:
    print("Sorry! Your word is not a palindrome!")


def main():

    name()

    isMultiple(42,7)

    palindrome()

 if __name__ == "__main__":
main()
