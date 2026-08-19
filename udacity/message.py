names =  input('Input you student names(separate with comma): ')
assignments = input('Input assignments for each student(separate with comma): ') # get and process input for a list of the number of assignments
grades =  input('Input grades for each grades for assignment(separate with comma): ')# get and process input for a list of grades

names = names.split(',')
assignments = assignments.split(',')
grades = grades.split(',')
print(grades)
for i in range(len(names)):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. Your current grade is {} and can increase \
    to 12/01/2027 if you submit all assignments before the due date.\n\n".format(names[i], assignments[i], grades[i])
    print(message);
