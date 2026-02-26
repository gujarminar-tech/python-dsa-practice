# operator Concatenation (+)
str1 = "Hello" + "World"
print(str1)

# repetition operator (*)
str2="Minar"
print(str2*2)

print(str2*0) #""
print(str2*-1) #""
#print(str2*2.5) #error

#string comparison
print("GATE"=="GATE")#True
print("GATE"=="gATE")#False
print("GATE"!="GATE")#False
print("GATE"<"gate")#True
print("Gate"<"gATE")#True
print("GATE"<="gate") #True
print("x">"azbc") #True
print("x">"xy") #False

#membership operator
str1="python"
print("py" in str1) #True
print("yto" in str1) #False

#Escape sequence characters
str2="Today's match is \"India vs England \""
print(str2)
str3='Today\'s match is "India vs Austrilia"'
print(str3)
str3=("Hello \nWorld")
print(str3)
print("Hello World!\b?") #Hello World?


#important to remember
print("\141") #change octal to decimal then decimal to str 
# eg. 141 => 97 => "a"
print("\141ab") #aab
print("\x61") #change hex to decimal then decimal to str

#string formation
#%formation
subject ="Python"
print("Class is %s"%subject)
name="Minar"
age=21
print("My name is %s and my age is %d"%(name,age))
#.format() method
print("my name is {} and i am {}years old".format(name,age))
print("i am {1}years old and my name is {0}".format(name,age))
print("i am {n}years old and my name is {m}".format(m=name,n=age))
#f-string method
print(f"my name is {name} and i am {age}")
print(f"next year i will be {age+1}")

#slicing
str1="Hello World"
print(str1[2:5]) #llo
print(str1[2:]) #bydefault end=-1 #llo World
print(str1[:5]) #bydefault start=0 #Hello
print(str1[:]) # =>print(str1)=>Hello World
print(str1[-10:-5]) #=>print(str[1:6])=>(ello )
print(str1[::-1]) #here bydefault start=-1,end=0
