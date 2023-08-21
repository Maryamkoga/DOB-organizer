#Open and read the contents in the text file
#File is opened using the open() function and the location of the file to be opened is specified
file_name = "DOB.txt"
file = open(file_name, "r", encoding = "utf-8")
#By using the .readlines() function, all the lines will be returned in the format of a list
to_read = file.readlines()
#This is to print the heading name and "\n" to print on a new line 
print("\nName")
#Using a for loop to get rid of extra lines and also split the lines into lists/sub-strings
for line in to_read:
    line = line.replace("\n","")
    name = line.split()
    #To print the names from the txt file
    #The join function is used to join selected elements and " " is used as a separator
    #The [0:2] is used to select elements from the initial index till the 2nd index
    print(" ".join(name[0:2]))

#To print the Birth Date heading
print("\nBirthdate")
#For loop to get rid of extra lines and split into lists
for line in to_read:
    line = line.replace("\n","")   
    birth_date = line.split()
    #To join selected elements that have been sliced 
    print(" ".join(birth_date[2:]))
file.close() #To close the file



