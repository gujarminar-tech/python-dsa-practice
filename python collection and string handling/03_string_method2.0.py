str1="Abc"
print(str1.lower())#"abc"
print(str1.upper())#"ABC"
print(str1.isupper())#False
print(str1.islower()) #False
print(str1.swapcase()) #aBC

str2="abc"
print(str2.capitalize())#Abc
str3="hello world"
print(str3.capitalize())#Hello world
str4="hEyy"
print(str4.capitalize()) #Heyy 
# capitalize converts 1st element into upper and rest all into lower

#title()
print(str3.title())#Hello World
str5="hey it's  minar   gujar"
print(str5.title()) #Hey It's Minar Gujar

#isalpha(),isnumeric(),isalnum()
str1="hello world"
print(str1.isalpha())# False because " " is not alphabet
str2="Hello"
print(str2.isalpha())#True
str3="10"
print(str3.isnumeric())#True
str4="GATE2027"
print(str4.isalnum())#True
print(str4.isalpha())#False
print(str4.isnumeric())#False
print(str2.isalnum())#True
print(str3.isalnum())#True

#count
str1="My name is Minar"
print(str1.count("M"))
print(str1.count("m"))
print(str1.count(""))
print(len(str1)==str1.count("")-1)

#find() method
str1="Hello World"
print(str1.find("ll")) #2
print(str1.find("xy")) #-1
str2="Banana"
print(str2.find("na")) #2 bacause find bydefault start from left

#rfind
print(str2.rfind("na")) #4 start from right but index count from left 
