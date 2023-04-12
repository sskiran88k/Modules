import datetime   
now=datetime.datetime.now()
date=now.strftime("%d-%m-%Y")
print(f"Today's date is {date}")
time=now.strftime("%H:%M:%S")
print(f"Now the time  is {time}")


