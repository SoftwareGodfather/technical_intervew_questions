from collections import namedtuple

def getKey(meet):
    return meet.hours

def SortByHours(meetings):
    return sorted(meetings, key=getKey)

def MaximizeByMeetingNumber(meetings, totalHours):
    meetHours = 0
    meetingList = []
    sortMeetings = SortByHours(meetings)
    for elem in sortMeetings:
        if(meetHours + elem.hours <= totalHours):
            meetingList.append(elem)
            meetHours += elem.hours
        else:
            break
    return meetingList

def MaximizeByMeetingNumber(meetings, totalHours):
    pass
    
########### MAIN ###########

meeting = namedtuple('Meeting', ['name', 'hours'])
meetings = [meeting('first',2), meeting('second',1), meeting('third',3)]

meetingList = MaximizeByMeetingNumber(meetings, 4)
print(meetingList)

meetingList = MaximizeByMeetingHours(meetings, 4)
print(meetingList)

########### STDOUT ###########

#[Meeting(name='second', hours=1), Meeting(name='first', hours=2)]
