string = "Strings tuples and lists are all different data types used in programming. Strings are very commonly used and probably more so than either of the others. This is because strings are a very basic data type. They hold data in the form of characters in a semi sealed fashion. What I mean by this is mutability. Strings are somewhat mutable in the way that one can change them. However if one is really looking for mutability one is more likely to use a list. A list can hold a number of different data types under one name. However on the other hand of the spectrum if one really wanted not to be able to change it one would use tuples. Tuples are very much like lists excluding one important factor being mutability. Tuples aren’t mutable. These are the main differences between these core data types."

def replace(original, remove, insert):
    print(original.replace(remove, insert))

print(string)

remove = input("What would you like to remove from the string?")
insert = input("What would you like to put instead?")

replace(string, remove, insert)
