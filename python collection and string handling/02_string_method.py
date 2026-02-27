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