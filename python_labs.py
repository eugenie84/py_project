
msg1 = "welcome to aws python 101 class: strings"
msg2 = "The instructor here is Claudio"

# Capitalize all first character of each word of msg1
print (msg1.title())

# reverse msg2
print (msg2[:: -1])

#write msg1 in lower case
print (msg1.lower())

# write mgs2 in upper case
print (msg2.upper())

# find how many "e" in msg2
print (msg2.count("e"))

# replace a value
print(msg1.replace("python","java"))

# create a new message "python is great" using msg1 characters
new_msg1 = msg1[15:21] + " " + msg1[-4] + msg1[-1] + " " + msg1[-2] + msg1[-5] + msg1[1] + msg1[-12] + msg1[-6]
print (new_msg1)

# create a new message "java is well done" using msg1 and msg2 characters
msg3 = msg1.replace("python","java")
new_msg3 = msg3[15:19] + " " + msg3[-4] + msg3[-1] + " " + msg3[0:3] + msg3[-13] + " " + msg2[-3] + msg3[4] + msg3[-3] + msg3[1]
print(new_msg3)