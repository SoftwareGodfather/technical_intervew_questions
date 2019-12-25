from collections import namedtuple

def getKey(meet):
    return meet.hours

def SortByHours(meetings):
    return sorted(meetings, key=getKey)

########### MAIN ###########

meeting = namedtuple('Meeting', ['name', 'hours'])
meetings = [meeting('first',2), meeting('second',1), meeting('third',3)]
print(meetings)
sortMeetings = SortByHours(meetings)
print(sortMeetings)
