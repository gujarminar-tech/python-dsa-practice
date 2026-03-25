#initialization of dictionary
dict1={}
dict2={"a":1,"b":2,"c":3}
dict3={"a":9,"b":[2,3,4],(2,3):{2,3,4}}
#key always immutable 
#list,set,dict are not allowed at key
#duplicate key not allowed
#value can be anything even repetition is allowed


#indexing in dictionary
d1={"a":1,"b":[3,4,2],(3,4):{3,4,5}}
print(d1["b"])
print(d1["b"][0])
print(d1[(3,4)])

#key should not be duplicate
d1={1:"A",0:"x",1.0:"ab",True:"Y",False:"G","1":"r","0":"F"}
print(d1) #{1: 'Y', 0: 'G', '1': 'r', '0': 'F'

#creating dict methods 
d1=dict(a=1,b=2,c=3,d="a")
print(d1) #{'a': 1, 'b': 2, 'c': 3, 'd': 'a'}

d1={"a":1,"b":2,"c":3}
d2=d1
d3=dict(d1)
d4=d1.copy()
d1["a"]=4
print(d1) #{'a': 4, 'b': 2, 'c': 3}
print(d2) #{'a': 4, 'b': 2, 'c': 3} change with d1
print(d3) #{'a': 1, 'b': 2, 'c': 3} create copy
print(d4) #{'a': 1, 'b': 2, 'c': 3}

students=["Minar","Nimish","Vivek","Om","Adi"]
d1=dict.fromkeys(students)
print(d1)
#{'Minar': None, 'Nimish': None, 'Vivek': None, 'Om': None, 'Adi': None}
d2=dict.fromkeys(students,0)
print(d2)
#{'Minar': 0, 'Nimish': 0, 'Vivek': 0, 'Om': 0, 'Adi': 0}  
