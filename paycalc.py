hrs = input("Enter Hours:")
h = float(hrs)
hrate = input("Enter hourly rate:")
rate = float(hrate)
if h > 40.0:
    overtime = h - 40.0
    payment = (40.0 * rate) + (overtime * 1.5 * rate)
else:
    payment = h * rate
print(payment)
