#create the list of items

tasks = ["do laundry", "clean the house", "pay bills"]

#print out the list
print(tasks)    

#prompt the user to add an item to the list, save the response in "new_task"add an item to the list
new_task = input("What task would you like to add to the list? ")   
#append "new_task"
tasks.append("new_task")
#print out the list again to show the new item has been added
print(tasks)    