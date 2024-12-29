# Types of String

name = "Fahad Chowdhury"
city = "Cabuyao"
country = "Philippines"

text = "I am Filipino!"
text1 = "I am also 'a Bangladeshi citizen' "
text2 = '''

ওস্তাদ-এর MERN কোর্সটি স্কিল ডেভেলপমেন্টের জন্য অনেক হেল্পফুল একটি কোর্স। আমার প্রতিটি প্রবলেমই তারা লাইভ ক্লাসেই সলভ করার চেষ্টা করেছে। এছাড়াও সাপোর্ট ইন্সট্রাক্টররাও অনেক ভালো। এসব কারণেই MERN এর লার্নিং জার্নিটা আমার জন্য ছিল অসাধারণ।

'''

# print(text)
# print(text1)
# print(text2)

# String Indexing
text = "FAHAD"
# print(text[0]) # Positive Indexing
# print(text[-1]) # Negative Indexing

# String Slicing
text = "Python Django Batch 02"
# print(text[0:6])
# print(text[:6])
# print(text[7:])
# print(text[::2])

# String Concatenation
firstName = "Fahad"
lastName = "Chowdhury"
age = "30"

fullName = firstName + " " + lastName
fullName1 = f"{firstName} {lastName}"
fullName2 = "{} {} {}".format(lastName, firstName, age)
fullName3 = "%s %s %s" %(lastName, firstName, age)

# print(fullName)
# print(fullName1)
# print(fullName2)
# print(fullName3)

# Repeatation
text = "OSTAD "
#text = text.replace(_old:"OSTAD", _new:"WORLD")
text = text.replace("OSTAD", "WORLD")
# print(text * 10)

# Split
text = "Hello-World"
words = text.split("-")
# print(words)

# String Occurrence
text = "Hello Word"
print(text.count("o"))

# Method Chaining
text = " hello python, hello python "
cleanText = text.strip().title()
print(cleanText)

# Validation
text = "123"
result = text.isdigit()

print(result)

# Numbers
x = 10
y = 20
z = 30

result = x + y * z

print(result)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# Mutable (Modification) | list set dictionaries
# Immutable (Unable to Modify) | int float string tuples frozen

a = 10
print(id(a))
a = 20
print(id(a))

myList = [1, 2, 3, 4]
print(id(myList))
myList.append(5)
print(id(myList))

print(myList)