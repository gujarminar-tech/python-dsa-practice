#strip() function
str1="    Hello World  "
print(str1.strip())
str2=".....Virat.Kohli......"
print(str2.strip("."))
str3="...?,..MInar.. <.."
print(str3.strip("."))#only last consicutive "." will removed

#star example
print(str2.strip("V.i"))

#lstrip() leftstrip
print(str2.lstrip("."))

#rstrip() rightstrip
print(str2.rstrip("."))

#split() method
str4="I am preparing for GATE 2027"
print(str4.split()) #by default parameter is " " 
# by default it print string into list after split

print(str4.split(maxsplit=3)) #first 3 split from left
str5="1,2,3,4,5"
print(str5.split(",")) #['1', '2', '3', '4', '5']
print(str5.split(",",maxsplit=2))#split bydefault start from right

#rsplit() 
# it only difer from the split when maxsplit applied
print(str5.rsplit(",",maxsplit=3))


#join() method
l="12345"
print(" ".join(l))
print("_".join("GATE"))