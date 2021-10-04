from pynotifier import  Notification

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

try :
    c = a / b
    print("a / b = ",c)

    if c == c :
        Notification (
            title = "Python Notification",
            description = 'Hi! Your Code was executed Successfully',
            duration = 20,          # After 20 Seconds - To hide notification automatically
            urgency = 'normal'
        ).send()

except Exception:
    print("Error Not Divisible")
    Notification (
        title = "Error!!!!Python Notification",
        description = 'Hi! Your Code was Not executed',
        duration = 20,
        urgency = 'normal'
        ).send()
    