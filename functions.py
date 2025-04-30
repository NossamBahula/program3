#Define a function
def ispalindrome(string):
                  if string==string[::-1]:
                    return"The string is a palindrome."

#Enter input string
string=input("Enter string:")
print(ispalindrome(string))
