'''
Homework 1
Marcos Hernandez
CS344
Exercise 3
'''

#imports
from tools.aima.csp import CSP, \
    min_conflicts

#lists for courses, professors, time, room, day
classes = ["CS108", "CS112","CS212","CS214" ,"CS232","CS262","CS344"]
professors = ["Norman", "Adams", "Vander Linden", "Plantinga"]
timeSchedule = ["MWF_900", "MWF_1130", "TTH_1030", "MWF_230"]
roomNumber = ["SB_282", "NH_253"]
assignments = {"CS108" : "Norman", "CS112" : "Adams", "CS212" : "Plantinga", "CS214" : "Adams", "CS232" : "Norman", "CS262" : "Vander Linden", "CS344" : "Vander Linden"}


#class chedule for each professor, room, and time
def class_schedule(class1, slot1, class2, slot2):
    professor1 = slot1[0]
    time1 = slot1[1]
    room1 = slot1[2]
    professor2 = slot2[0]
    time2 = slot2[1]
    room2 = slot2[2]

#stops the program to overlap with other sessions
    noRoomOverlap = (time1 != time2) or (room1 != room2)
    noProfessorOverlap = (professor1 != professor2) or (time1 != time2)
    return (noRoomOverlap and noProfessorOverlap)

#definition for time
def time_slots(slot, time):
    classTimeSlots = []
    for slots in slot:
        for times in time:
             classTimeSlots.append((slots, times))
    return classTimeSlots

#definition for assignments, courses, schedule
def course_schedule_assignment(course, assignment, classTimeSlots):
    scheduleAssignment = {}
    for courses in course:
        schedule = []
        professor = assignment[courses]
        for slot in classTimeSlots:
            schedule.append((professor, slot[0], slot[1]))
        scheduleAssignment[courses] = schedule
    return scheduleAssignment

#definition for CS courses
def schedule_CS(classes):
    CS = {}
    classTotal = len(classes)
    for classSchedule in range(classTotal):
        classTime = []
        for timeSchedule in range( classSchedule + 1, classTotal):
            classTime.append(classes[timeSchedule])
        CS[classes[classSchedule]] = classTime
    return CS

#assigns all the data entered
slots = time_slots(timeSchedule, roomNumber)
courseAssignments = course_schedule_assignment(classes, assignments, slots)
CSSchedule = schedule_CS(classes)

#stores results from data stored
scheduleResult = min_conflicts(CSP(classes, courseAssignments, CSSchedule, class_schedule))

#prints the schedule
print('Schedule: ' + str(classes))
print("CS Schedule: ")
for i in courseAssignments:
    print("{0}: {1}".format(i, courseAssignments[i]))
print("Results: ")
for r in scheduleResult:
    print("{0}: {1}".format(r, scheduleResult[r]))