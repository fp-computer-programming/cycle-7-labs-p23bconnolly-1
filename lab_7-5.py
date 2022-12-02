#lab 6-5
numbers = [2, 6, 4, 9, 3]
maxnumber = max(numbers)
minnumber = min(numbers)  
print(maxnumber)
print(minnumber)
#prints the max and the min of the list of numbers 
if len(numbers) < 2:
    print("error: list does not meet specifications")
#when there is less than 2 unique numbers, prints the message

print(numbers(12, 3, 7, 22, 1) == "the lowest value is 3 and the highest value is 22.")
#test case one, comes out as true
print(numbers(2, 8, 19, 0, 20) == "the lowest value is 0 and the highes value is 20")
#test case two, comes out as true 
print(numbers(16, 4, 5, 25, 21) == "the lowest value is 3 and the highest value is 25")
#test case three, comes out as true
print(numbers(1, 11, 28, 27, 26) == "the lowest value is 1 and the highest value is 28")
#test case four, comes out as true

# lab 6-6
word_1 = input("please input your first word")
word_2 = input("please input your second word")
word_3 = input("please input your third word") 
word_4 = input("please input your fourth word")
word_5 = input("please input your fifth word")
# after each word is inputted, a list is printed listing each word in the order they were put in
ordered_list = (word_1, word_2, word_3, word_4, word_5) 
print(ordered_list) 

len1 = len(word_1)
len2 = len(word_2)
len3 = len(word_3)
len4 = len(word_4)
len5 = len(word_5)

list = [len1, len2, len3, len4, len5]
print(list)

print(ordered_list("phone, keyboard, mouse, hoodie, computer") == (['mouse, phone, hoodie, computer, keyboard'])), [5, 5, 6, 7, 8] 
#first test case, should come back as true
print(ordered_list("four, fiver, monitor, one, cheese") == (['one, four, fiver, cheese, monitor'])), [3, 4, 5, 6, 7]
#second test case, should come back as true
print(ordered_list("desk, pie, fries, numlock, invalid") == (['pie, desk, fries, invalid, numlock'])), [3, 4, 5, 7, 7]
#third test case, should come back as true
print(ordered_list("social, ethics, calc, the, to") == (['to, the, calc, ethics, social'])), [2, 3, 4, 6, 6]
#fourth test case, should come back as treu

#lab 6-7
value_1 = int(input("please input your first numeric value")) 
value_2 = int(input("please input your second numeric value")) 
value_3 = int(input("please input your third numeric value"))
# asks the user to input the 3 numeric values
#value_1 = int 
#value_2 = int
#value_3 = int
#makes each value an int
#doubled_value_1 = int
#doubled_value_2 = int
#doubled_value_3 = int
doubled_value_1 = value_1 * 2 
doubled_value_2 = value_2 * 2
doubled_value_3 = value_3 * 2

doubled_value_list = (doubled_value_1, doubled_value_2, doubled_value_3)
 
print(doubled_value_list)
# first test case, should return as true 
print(doubled_value_list(1, 2, 3) == [2, 4, 6])
#second test case, should return as true
print(doubled_value_list(2, 3, 4) == [4, 6, 8])
#third test case, should return as true
print(doubled_value_list(5, 10, 15) == [10, 20, 30])
# fourth test case, should return as true
print(doubled_value_list(6, 7, 8) == [12, 14, 16])


#lab_6=8
value_1 = int(input("please input your first numeric value")) 
value_2 = int(input("please input your second numeric value")) 
value_3 = int(input("please input your third numeric value"))
#prompts the user to input 3 numeric values
list_2 = [value_1, value_2, value_3]
#creates a list in the order they were inputted
if value_1 %2 == 0 and value_2 %2 == 0 and value_3 %2 == 0:
    print("the numbers are all even")
elif value_1 %2 != 0 and value_2 %2 != 0 and value_3 %2 != 0:
    print("the numbers are odd")
else:
    print("numbers are both even and odd") 
#detects if the numbers are even, odd, or a mix of the two

#test case 1, should return true
print(list_2(2, 3, 4) == "numbers are both even and odd")
#test case 2, should return true
print(list_2(2, 4, 6) == "numbers are all even")
#test case 3, should return true
print(list_2(3, 5, 7) == "numbers are all odd") 
#test case4, should return true
print(list_2(4, 6, 7) == "numbers are both even and odd") 
