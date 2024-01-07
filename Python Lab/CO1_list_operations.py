#Generate positive numbers from a list
list1=[2,4,-6,-8,9,7]
list2=[i for i in list1 if (i>0)]
print(f"Positive list {list2}")


#square of n numbers
list3=[2,3,4,5]
list4=[i**2 for i in list3]
print(f"The square of the numbers are {list4}")

#list of vowels from given word
word=input("Enter a word : ")
listvowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are {listvowel}")

#To get ordinal values
text=input("Enter any characters : ")
ordinals=[ord(i) for i in text]
print(ordinals)
