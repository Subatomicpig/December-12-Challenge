#daily challenge 12-12-2013
#hardware pricing
#my goal for this is to create two lists order them compare and output the discrepcy

PRICELIST = 'prices.txt'


if __name__ == '__main__':
	#saves the items from the file into a list to work with
	list = open(PRICELIST).readlines()
	#pop the number off the list so we can split the rest up into a dictionary
	listSize = list.pop(0)
	inputList = {}

	#loops through each value in the input list and places them into a dictionary	
	for line in list:
		item, price = line.split()
		#if the item is in the input list we want to add it as the new value otherwise 
		#it's the old value
		if item in inputList:
			inputList[item]['new'] = int(price)
		else:
			inputList[item] = {'old' : int(price)}

	#for each item in our itemlist we want to iterate through and compare the prices at the end of the values
	#if they are different we calculate the difference between the items and add them to an ouput
	for item in inputList.keys():
		#if the items are different
		if inputList[item]['old'] != inputList[item]['new']:
			output = inputList[item]['new'] - inputList[item]['old']
		print "%s,%+d" % (item,output)