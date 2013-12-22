#import module argv from system module
from sys import argv
#defintes arguments to run the script, requires 'input_file'
script, input_file = argv
#defines print_all functions which reads all the contents of a file
def print_all(f):
	print f.read()
#Sets the files current position to the start
def rewind(f):
	f.seek(0)
#prints a specific line from a file. Takes the argument 'line_count' which instructs the line 
#positions and 'f' which is the file itself
def print_a_line(line_count, f):
	print "Current Line is:", current_line
	print line_count, f.readline()
#opens the input file and sets it to current_file
current_file = open(input_file)
#print statement
print "First let's print the whole file:\n"
#prints the file
print_all(current_file)
#print statement
print "Now let's rewind, kind of like a tape"
#sets the current position to the beginning of the file
rewind(current_file)
#print statement
print "let's print three lines:"
#prints the first line of the file
current_line =  1
print_a_line(current_line, current_file)
#prints the second line of the file by adding one to the previous location
current_line += current_line
print_a_line(current_line, current_file)
#prints the third line of the file by adding one to the previous location
current_line +=  current_line 
print_a_line(current_line, current_file)