def reverse_string(str):
    str1=""  #Declaring to empty to store the reversed string
    for i in str:
        str1 = i + str1
    return str1 #it will return the reverse string to the caller
str = input("Enter a string : ")
print("The original string is : ", str)
print("The reverse string is :", reverse_string(str))




