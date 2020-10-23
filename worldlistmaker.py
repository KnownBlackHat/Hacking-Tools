class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

def generate(arr, i, s, len): 

	# base case 
	if (i == 0): # when len has 
				# been reached 
	
		# print it out 
		print(color.BLUE,s)
		f = open("WORD_LIST.txt", "a")
		f.write(f"{s}\n")
		f.close()
		return
	
	# iterate through the array 
	for j in range(0, len): 

		# Create new string with 
		# next character Call 
		# generate again until 
		# string has reached its len 
		appended = s + arr[j] 
		generate(arr, i - 1, appended, len) 

	return

# function to generate 
# all possible passwords 
def crack(arr, len): 

	# call for all required lengths 
	for i in range(1 , len + 1): 
		generate(arr, i, "", len) 
	
# Driver Code 
inp=input("Enter Characters: ")
inp=inp.split(" ")
arr = inp 
print(color.YELLOW+"The Characters To Use Are: ",arr )
f = open("WORD_LIST.txt", "w")
f.write(f"The Characters To Use Are: {arr}\n")
f.close()
len = len(arr) 
crack(arr, len) 
