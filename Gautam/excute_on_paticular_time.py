from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
print("x is equal to" , x)
y = x.replace(day=x.day, hour=19, minute=0, second=0, microsecond=0) + timedelta(days=1)
print("y is equal to", y)
deltaTime=y-x

seconds=deltaTime.total_seconds()


def Greet():
    print("Hello Gautam, Its" ,x, "now. Time to excute your program")

t = Timer(seconds, Greet)
t.start()
