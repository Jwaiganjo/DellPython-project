# Data type

number = 100 # int
second = 56.78 # float
text = "Hello there" # str
ispythoninteresting = True # bool

# storing multiple values in a variable
cars = ["toyota","nissan","vw"] # list
fruits = ("banana","oranges", "apple") #Tuplet
countries = {"Kenya","Tanzania", "tunisia","Algeria"}
details = {
    "firstname": "Jeff",
    "age": 34,
   "course": "web development",
    "nationality": "kenyan",
}   #dictionary
print(details["firstname"])
print(details["age"])
print(text)
print(cars)
print(countries)

#determine data type
print(type(text))
print(type(countries))
print(type(details))

#Typecasting - converting one data type to another
print(float(number))