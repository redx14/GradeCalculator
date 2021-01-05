#Andrey Ilkiv Assignment 2 problem 3 9/30/2020 section 01

#asks user to enter assignment 1 grade
assign1 = float(input('Enter assignment #1 grade:   '))

#asks user to enter assignment 2 grade
assign2 = float(input('Enter assignmnet #2 grade:   '))

#asks user to enter assignment 3 grade
assign3 = float(input('Enter assignment #3 gradae:  '))

#asks user to enter weekly quizzes grade
WQ = float(input('Enter weekly quizzes grade:  '))

#asks user to enter midterm grade
Midterm = float(input('Enter midterm grade:         '))

#asks user to enter final grade
Final = float(input('Enter final exam grade:      '))

#takes the average of 3 assignments all weighing the same amount
AvgAssign = (assign1 + assign2 + assign3)/3

#we multiply the final grades by their coresponding percentiles and then add them together round to
#the tenths place
FinalGrade = (AvgAssign*0.25) + (WQ*0.05) + (Midterm*0.25) + (Final*0.45)

#if the final grade is above 90% isgradeA string is set to True
#if the final grade is NOT above 90% isgradeA string is set to False
isgradeA = FinalGrade > 90

#prints final grade
print('' , 'Final Grade:                 ' + format(FinalGrade, '.1f') , sep='\n')

#prints if the grade = an A or not
print('Is an A?                    ' , isgradeA)
