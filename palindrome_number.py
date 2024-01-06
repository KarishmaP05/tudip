def palindrome(number):
    number=str(number)
    # print(number)

    for i in number:

        rev = ''.join(reversed(number))
    

        if number==rev:
            return True
    return False

number=106
ans=palindrome(number)

if ans:
    print("yes")

else:
    print("no")