animals = ['bear', 'python', 'peacock','kangaroo','whale', 'platypus']

print "The animal is at %s in the index, and is a %s" % (animals.index(animals[0]), animals[0])
print "The animal is at %s in the index, and is a %s" % (animals.index(animals[2]), animals[2])
print "The animal is at %s in the index, and is a %s" % (animals.index(animals[1]), animals[1])
print "The animal is at %s in the index, and is a %s" % (animals.index(animals[3]), animals[3])
print "The animal is at %s in the index, and is a %s" % (animals.index(animals[4]), animals[4])
print "The animal is at %s in the index, and is a %s" % (animals.index(animals[5]), animals[5])

def print_with_for_loop(animals):
    for index, value in enumerate(animals):
        print "The animal is at %s in the index, and is a %s" % (index, animals[index])

print "\n"
print_with_for_loop(animals)
