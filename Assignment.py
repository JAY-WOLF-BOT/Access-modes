
file = open('sample1.txt','r')
print("---FIRST FILE READ---")
print(file.read())
file.close()

file1 = open('sample2.txt','r')
print("---SECOND FILE READ---")
print(file1.read())
file1.close()

file2 = open('sample1.txt','w')
print("!!!!!Updating The Text File!!!!!")
file2.write("-----Hello New Editing Line-----")
file2.close()

file3 = open('sample2.txt','a')
print("------Appended Update------")
file3.write('sample1.txt')
file3.close()

