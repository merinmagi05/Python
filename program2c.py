vowels=['a','e','i','o','u','A','E','I','O','U']
word=str(input("Enter the Word:"))
result=[i for i in word if i in vowels]
print(result)