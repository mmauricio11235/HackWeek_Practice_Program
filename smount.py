import sys


def findHeight(heights, index):
	increasing = 0
	width = 2
	while increasing < 3 and index < len(heights) - 2:
		if increasing == 0:
			if heights[index + 1] > listHeight[0]:
				width += 1
				index += 1
			elif heights[index+1] == heights[index]:
				increasing += 1;
				index += 1
			if heights[index + 1] < heights[index]:
				increasing += 2
				index += 1
		elif increasing == 1:
			if heights[index + 1] == listHeight[0]:
				width += 1
				index += 1
			elif heights[index + 1] < listHeight[0]:
				increasing += 1
				width += 1
				index += 1
		elif increasing == 2:
			if heights[index + 1] < listHeight[0]:
				width += 1 
				index += 1
			else: 
				increasing += 1
	if (index == len(heights) - 2): 
		index = -1
	return width, index



#Reads in the in file
lines = sys.stdin.readlines()

#Finds the number of measurements
if len(lines) > 0:
	numMeasure = int(lines[0])

listHeight = []
for i in range (1, len(lines)):
	height = int(lines[i])
 	listHeight.append(height)


#Converts all strings in lines to ints
lines = [int(k) for k in lines]
sumOf = sum(lines) - lines[0]

#Creates the mountain representation
mount = lines
mountain = []
mountainView = []
i = 1

while sumOf != 0:
	if i > (len(mount) - 1):
	 	mountainView.append(mountain)
	 	mountain = []
	 	i = 1
	elif mount[i] > 0:
		mountain.append("X")
		mount[i] -= 1
		i += 1
		sumOf -= 1
	else: 
		mountain.append(" ")
		i += 1

mountainView.reverse()
for k in range(0, len(mountainView)):
	print mountainView[k]


increasing = 0
print listHeight
if listHeight[1] > listHeight[0]:
	increasing = 1;
else: 
	increasing = 0;
countCurr = 0
count = 1
widthLists = []
x = 0
y = 0

while y > -1 : 
	if increasing == 1:
		x, y = findHeight(listHeight, y)
		widthLists.append(x);
	else:
		while increasing == 0 and (countCurr < len(listHeight) - 1):
			if listHeight[countCurr + 1] < listHeight[countCurr] or listHeight[countCurr + 1] == listHeight[countCurr] :
				count += 1
				countCurr += 1
			else:
				widthLists.append(count)
				y = countCurr
				increasing = 1
		if countCurr == len(listHeight) - 1:
			y = -1

if increasing == 0:
	widthLists.append(countCurr + 1)
print widthLists

#Calculates the longest mountain	










'''
for i in range(0, len(listHeight) - 1):
	#Case 1
	if increasing == 1: 
		if listHeight[i+1] > listHeight[i]:
			countCurr += 1
		#	print "case 1 increasing"
		elif listHeight[i+1] == listHeight[i]:
		#	print "case 2 peak mount"
			countCurr += 1
		elif listHeight[i+1] < listHeight[i] :
		#	print "case 3 to decrease"
			countCurr += 1
			increasing = 0
			
	else:		#print "case 4 Still decrease"
		if listHeight[i+1] < listHeight[i]:
			countCurr+= 1
			
		elif listHeight[i+1] == listHeight[i]:
			#print "case 5 bottom of mount"
			countCurr += 1
			countNext += 1
		else:
			#print "case 6 Increasing again"
			#print "current count is ", countCurr
			widthLists.append(countCurr)
			countCurr = countNext
			countNext = 1
			increasing = 1


widthLists.append(countCurr)
print "The widths are", widthLists
if len(widthLists) > 0:
	largest = widthLists[0]
else:
	largest = 0
for i in range (0, len(widthLists) - 1):
	if widthLists[i+1] > widthLists[i]:
		largest = widthLists[i+1]

print largest


'''
