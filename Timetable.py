from datetime import datetime
from FRIDAY import speak
fiveto6="its wake up time"
sixto7="fresh up time"
sevento10="tution time"
tento12="hindu analysis"
thirteento14="lunch"
fifteento16="Entertainment"
sixteento18="gym time"
l=["its wake up time","fresh up time","tution time","hindu analysis","lunch","Entertainment","gym time","coding time","free time"]
l1=["5 to 6","6 to 7","7 to 10","10 to 12","1 to 2","2 to 4","4 to 6", "6 to 9","after 9"]
l2=[]
r=list(zip(l1,l))
for i in r:
    l2.append(list(i))
def time():
    hour=int(datetime.now().strftime("%H"))
    if hour>=5 and hour<6:
        return fiveto6
    elif hour>=6 and hour<7:
        return sixto7
    elif hour>=7 and hour<10:
        return sevento10
    elif hour>=10 and hour<12:
        return tento12
    elif hour>=13 and hour<14:
        return thirteento14
    elif hour>=15 and hour<16:
        return fifteento16
    elif hour>=16 and hour<18:
        return sixteento18 
    else:
        return "sleep"
def tell():
    for i in l2:
        speak(i[0])
        speak(i[1])