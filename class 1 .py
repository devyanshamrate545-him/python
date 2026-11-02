#mkdir-> to create a new folder / directory 
#rmdir -> to rmove a folder / directory


#folders
# import os 
# os.mkdir("hello")
# os.rmdir("hello")








#""""
# FILES 
# x -> this mode will only create the file and if already exists we 
# will get an error back 

# w-> agar file xist nahi karti hai so this mode will create one 
#and insert the content inside the file 

#a


#r



#1 mode1 : just to create the file 
# open("garba.txt,"x")


#mode2 : w 
# file = open("garba.txt","w")
# file.write("khelo garba khub khelo din raat khelo ")
# file.write("enjoy karo job hi job hai ")



#mode3 :a -> add the text at last 

#mode4 : r -> read the content inside  of the file
# file = open("garba.txt","r")
# print(file.read())


# with open("sample.txt","r") as file:
#     print(file.read())



# CRUD -> create read update delete


# os.remove("garba.txt")
# print("press 1 for creating  a file")
# print("press 2 for reading a file")
# print("press 3 for updating a file")
# print("press 4 for deleting a file")