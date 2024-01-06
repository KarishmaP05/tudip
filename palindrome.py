'''
def palindrome(a):

    for i in a:
        return a == a[::-1]

a="abc"
ans=palindrome(a)
if ans:
    print("yes")
else:
    print("no")
'''



def palindrome(a):
    # rev = ''.join(reversed(a))
    rev=a[::-1]
    print(rev)

    if a==rev:
        return True
    return False

a="aba"
ans=palindrome(a)

if ans:
    print("yes")

else:
    print("no")