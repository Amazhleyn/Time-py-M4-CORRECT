currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = (currentTimeInt + waitTimeInt) % 24
print("The time after waiting will be:", finalTimeInt)