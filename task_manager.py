

# Using the template provided to complete task 1 as follows:

# Importing the two files user.txt and tasks.txt as r for reading and w for writing txt to:
Contents = " "
with open("user.txt", 'r') as fuser:

	user_name = input("Enter your username:")
	user_password = input("Enter your password: ")

	while True:
		for lines in fuser:  # reading each line
			login = lines.split(",")  # splitting lines into words
			login = user_name, user_password
		if user_name == login[0] and user_password == login[1]:
			print("Welcome back", user_name)
			break
		else:
			print("Not registered, Goodbye")
			break

### here it recognises when the user logging in is not in user.txt but i do not know how to stop the
		# loop and exit as everything else i tried is either looping forever or not doing what i want.

# Options if user is admin user:
menu = ""
while True:
	if user_password and user_name == 'admin':  # user choices for admin user
		menu = input('Select one of the following:\n'
		             'r - Register new user\n'
		             't - View tasks completed \n'
		             'u - View all users \n'
		             'q - Quit\n')
	if menu == 'r':  # register a new user
		new_name = input("Enter new username\t ")
		new_password = input("Enter new password \t")
		first_name = input("Enter your First name \t")
		confirm_password = input("Confirm your password \t")
		if confirm_password != new_password and len(new_password) == 0:
			input("Sorry password confirmation failed: ")
		with open("user.txt", 'a') as fuser:  # saving new user to user.txt
			fuser.writelines(f" {new_name}, {new_password},")
			fuser.writelines('\n')
	elif menu == 'u':
		with open("user.txt", "r") as fuser:
			for contents in fuser:
				print(contents, "\n")
			break
	elif menu == 't':
		with open("tasks.txt", "r") as ftasks:
			for contents in ftasks:
				print(contents, "\n")
			break
	elif menu == 'q':
		print('Goodbye Admin')
		break

	else:

		break

# Options for user that is not an admin

while True:
	if user_password and user_name != 'admin':  # i.e. other login details entered than 'admin'
		menu = input('Select one of the following\n'
		             'a - Adding a task\n'
		             'va - View all tasks\n'
		             'vm - view my task\n'
		             'e - Exit\n')
	if menu == 'a':  # adding a new task to tasks.txt
		first_name = input("Enter username of user to assign a task: ")
		title = input("Enter title of task: ")
		description = input("Enter description of task:")
		due_date = input("Enter the due date in dd/mm/yy format:")
		current_date = input("Enter today's date:")
		task_complete = input('Is task already complete?  (yes/no)')
		if due_date == current_date:
			print("Task already completed:")

		with open("tasks.txt", "a") as ftasks:
			ftasks.writelines(f" {first_name}, {title}, {description},{current_date}, {due_date}, {task_complete},\n")
			ftasks.writelines('\n')


	elif menu == 'va':  # viewing all tasks in tasks.txt.
		with open("tasks.txt", "r") as ftasks:
			for contents in ftasks:
				print(contents, "\n")
	elif menu == 'vm':
		with open("tasks.txt", "r") as ftasks:
			lines = ftasks.readlines( )
			word = input("Enter name ")  # enter the name of the person's task you are looking for
			for line in lines:
				if line.find(word) == 1:  # if that persons name is in tasks the person's tasks will print
					print(line)
	elif menu == 'e':
		print("Goodbye",user_name, "have a nice day!!")
		exit( )

	else:
		break
