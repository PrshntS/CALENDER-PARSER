from icalendar import Calendar, Event
from datetime import datetime
import sys
from dateutil.rrule import *
def reyna(recur_rule,start,end):

    """ Find all reoccuring events """
    rules = rruleset()
    first_rule = rrulestr(recur_rule, dtstart=start)
    rules.rrule(first_rule)
    dates = []
    for rule in rules.between(start, end):
        dates.append(rule.strftime("%B %d, %Y (%a)"))
       
    return dates

def phoenix(d1,d2,f):
    g=open(f,'rb')
    gcal = Calendar.from_ical(g.read())
    for component in gcal.walk():
        if component.name == "VEVENT":
            today=component.get('dtstart').dt
            #print(today)
            if(d1<=today<=d2):
                summary = component.get('summary')
                location = component.get('location')
                startdt = component.get('dtstart').dt
                # print(startdt)
                # print(d1)
                # print(d2)
                enddt = component.get('dtend').dt
                #print(enddt)
                if component.get('rrule'):
                    reoccur = component.get('rrule').to_ical().decode('utf-8')
                    for item in reyna(reoccur,d1,d2):
                        print(item)
                        print("-------------------------------")
                        print("{0} to {1}: {2} {{{{{3}}}}}".format(startdt.strftime("%I:%M %p"),enddt.strftime('%I:%M %p'),summary,location))
                        print()
                            
                else:
                    print(startdt.strftime("%B %d, %Y (%a)"))
                    print("-------------------------------")
                    print("{0} to {1}: {2} {{{{{3}}}}}".format(startdt.strftime("%I:%M %p"),enddt.strftime('%I:%M %p'),summary,location))
                    print()
    g.close()
                

def sage():
    start=str(sys.argv[1]).split('=')[1]
    end=str(sys.argv[2]).split('=')[1]
    filen=str(sys.argv[3]).split('=')[1]
    start=start.split('/')
    start_date = datetime(int(start[0]),int(start[1]),int(start[2]))
    end=end.split('/')
    end_date=datetime(int(end[0]),int(end[1]),int(end[2]))
    #start_date=datetime.strptime(start[1],'%Y/%m/%d')
    #print(start_date)
    #end_date=datetime.strptime(end[1],'%Y/%m/%d')
    #print(end_date)
    phoenix(start_date,end_date,filen)
  
sage()  

