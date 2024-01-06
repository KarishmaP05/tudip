def divisibility(number):
    result=""

    if number % 11==0:
        result+="Foo"

    if number % 17==0:
         result+="Bar"

    return result




number=int(input("enter a number"))
divisibile=divisibility(number)

if divisibile:
    print(divisibile)

else:
    print("not by 11 or 17")