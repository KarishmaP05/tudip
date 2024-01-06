def count_words(sen):
    count=0
    sen1=sen.split()
    print(sen1)

    for i in sen1:

        count+=1
    return count


sen="i am very beautiful"
result=count_words(sen)
print(result)