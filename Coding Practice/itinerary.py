#Find Itinerary from a given list of tickets

def startPoint(m):
    start = None
    rev  = dict()
    for i in m:
        rev[m[i]] = i
    # print rev
    
    for i in m:
        if i not in rev.keys():
            print "Starting POINT"
            start =  i
            
    print start
    
    to = m[start]
    while (to):
        print start , " --> ", to 
        start = to 
        if m[start] not in m.keys():
            break
        else:
            to = m[start]
    
m=dict()
m["Chennai"] = "Bangalore"
m["bombay"] = "delhi"
m["goa"] = "Chennai"
m["delhi"] = "goa"
print m
startPoint(m)
