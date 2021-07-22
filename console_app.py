import os
import platform #The Platform module is used to retrieve as much possible information 
				#about the platform on which the program is being currently executed. 

global studentlist
studentlist = ["Anchor", "Blake", "Cassy", "Dillan"]

def studentmanagement():

	print("\n Student Management System \n")
	print("[Choice 1: Showing the List of Student]")
	print("[Choice 2: Add New Student]")
	print("]Choice 3: Searching Student]")
	print("[Choice 4: Deleting a Student]\n")

	try:
		x = int(input("Enter a choice: "))
	except ValueError:
		exit("\n ! Enter a valid number !")
	else:
		print("\n")

	if(x==1):
		print("Student List\n")
		for students in studentlist:
			print(" {} ".format(students))

	elif(x==2):
		studentnew = input("Enter New Student: ")
		if(studentnew in studentlist):
			print("\nThis Student {} Already In The Table".format(studentnew))
		else:
			studentlist.append(studentnew)
			print("\nNew Student {} Added Successfully \n".format(studentnew))
			for students in studentlist:
				print("++ {} ++".format(students))

	elif(x==3):
		studentsearching = input("Choose a Student Name To Search: ")
		if(studentsearching in studentlist):
			print("\n There is a Record Found of this Student {} ".format(studentsearching))
		else:
			print("\n There is No Record Found Of this Student {} ".format(studentsearching))

	elif(x==4):
		studentdelete = input("Choose a Student Name To Delete: ")
		if(studentdelete in studentlist):
			studentlist.remove(studentdelete)
			for students in studentlist:
				print(" {} ".format(students))
		else:
			print("\n There is No Record Found of This Student {} ".format(studentdelete))

	elif(x < 1 or x > 4):
		print("Please Enter Valid Choice")

studentmanagement()

def continueAgain():
	runningagain = input("\nWant to continue the process yes/no?: ")
	if(runningagain.lower() == 'yes'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentmanagement()
		continueAgain()
	else:
		quit()

continueAgain()
