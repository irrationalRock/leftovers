#with open("test_file.dat", "rb") as binary_file:
    # Read the whole file at once
#    data = binary_file.read()
#    print(len(data))
import sys

#open with universial 
with open("sorted_stuff.json", "U") as f:
	data = f.readline()
	print sys.getsizeof(data)
	#print len(data)
	
	
#write out json file
with open('myfile.txt', 'w') as outfile:
    outfile.write(text) 