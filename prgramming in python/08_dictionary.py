players={"Virat":101,"Rohit":120,"Sachin":110}
players.update({"Virat":105}) # virat is already in keys so value is updated
players.update({"Dhoni":200}) # dhoni is not in keys so new element is added

print(players)

print(players["Rohit"])

a={1:4,(4,5,"hello"):8,"hey":list[range(0,5)]}
print(a) # key should be immutable ,value can be anything