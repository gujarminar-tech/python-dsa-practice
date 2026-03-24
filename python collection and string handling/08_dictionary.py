#initialization of dictionary
dict={}
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