



num = input("Give me a number:\t")
print(num)


print( float(num))

print( int(num))

year = input("Year:")

if len(year) != 4 or not year.isdigit():
    print("not a year")



time = "morning"
name = "Tony"
greeting = "Good {}, {}"
print(greeting.format(time, name))
print(greeting)
greeting = greeting.format(time, name)
print(greeting)



time = "afternoon"
name = "Luna"
greeting2 = greeting = "Good {ltime}, {lname}"
print(greeting.format(ltime=time, lname=name))

