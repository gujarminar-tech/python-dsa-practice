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
print(".")
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

