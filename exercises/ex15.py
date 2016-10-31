from sys import argv

script, filename = argv
#this line is for read de file
txt = open(filename)
#this line prints de filename
print "Here's your file %r:" %filename
print txt.read()#this line read the file
txt.close()#this line let close the file
print "Type the filename again:"
file_again = raw_input("> ")#ask for the filename

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
