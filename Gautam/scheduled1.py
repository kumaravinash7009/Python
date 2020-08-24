import schedule 
import time 
  
def execute(): 
    print("The time to execute this code")
def sudo_placement(): 
    print("Get ready for Sudo Placement at Geeksforgeeks") 
  
def good_luck(): 
    print("Good Luck for Test") 
  
def work(): 
    print("Study and work hard") 
  
def bedtime(): 
    print("It is bed time go rest") 
      
def geeks(): 
    print("Shaurya says Geeksforgeeks") 
  
  
schedule.every(10).seconds.do(geeks) 
schedule.every().hour.do(geeks) 
schedule.every().day.at("14:56").do(execute)
schedule.every(5).to(10).minutes.do(work)
schedule.every().monday.do(good_luck)
schedule.every().tuesday.at("18:00").do(sudo_placement) 
  
while True: 
    schedule.run_pending() 
    time.sleep(1)