import glob

#Root folder you want the script to start searching from
file = 'E:/Repository/Master'

# Prep counters
count = 0
count1 = 0
count2 = 0
count3 = 0

# Prep lists to be filled
list1 = []
list2 = []
list3 = []



# High level search - Adjust appended directory parameters and include wildcards to refine search
for f in glob.glob(file + "/**/AR/*.dwg", recursive=True):
    count += 1
    #print(f)

#Gives a basic count of all dwg files contained within a 'Master' folder below the root folder
print('There are ' + str(count) + ' .dwg files in the ' + file + '/**/AR/ subdirectories')
print("")



# Category 1 search - Adjust appended directory parameters and include wildcards to refine search
for f in glob.glob(file + "/**/AR/" + "*" + "progress 1.dwg", recursive=True):
    count1 += 1
    f2 = f.replace("\\", "/")
    list1.append(f2)
    #print(f)

# Gives a basic count of how many dwg files have 'progress 1' in their filename & returns their folder locations
print('There are ' + str(count1) + ' .dwg files ready to start')
print(list1)
print("")



# Category 2 search - Adjust appended directory parameters and include wildcards to refine search
for f in glob.glob(file + "/**/AR/" + "*" + "progress 2.dwg", recursive=True):
    count2 += 1
    f2 = f.replace("\\", "/")
    list2.append(f2)
    #print(f)

# Gives a basic count of how many dwg files have 'progress 2' in their filename & returns their folder locations
print('There are ' + str(count2) + ' .dwg files in progress')
print(list2)
print("")



# Category 3 search - #Adjust appended directory parameters and include wildcards to refine search
for f in glob.glob(file + "/**/AR/" + "*" + "progress 3.dwg", recursive=True):
    count3 += 1
    f2 = f.replace("\\", "/")
    list3.append(f2)
    #print(f)

# Gives a basic count of how many dwg files have 'progress 3' in their filename & returns their folder locations
print('There are ' + str(count3) + ' .dwg files ready for review')
print(list3)
print("")