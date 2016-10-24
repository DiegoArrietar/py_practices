from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')
#It's really just a string with a character in it for the kind of mode for the file.
#If you use 'w' then you're saying "open this file in 'write' mode," thus the 'w' character.
#There's also 'r' for "read," 'a' for append, and modifiers on these.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

##extra
target = open(filename)
print "Now the file contains {0}".format(target.read())
target.close()
