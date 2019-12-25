
def getKey(meet):
    return meet.hours

def SortByHours(meetings):
    return sorted(meetings, key=getKey)

########### MAIN ###########

meeting = namedtuple('Meeting', ['name', 'hours'])
meetings = [meeting('first',2), meeting('second',1), meeting('third',3)]
sortMeetings = SortByHours(meetings)

totalHours = 3
meetHours = 0
meetingList = []
for elem in sortMeetings:
    if(meetHours + elem.hours <= totalHours):
        meetingList.append(elem)
        meetHours += elem.hours
    else:
        break

print(meetingList)
