
def permutation(string ,i=0):

    if i==len(string):
        print("".join(string))
    for j in range(i,len(string)):
        words= [c for c in string]
        words[i],words[j]=words[j],words[i]
        permutation(words,i+1)

print(permutation("abc"))
