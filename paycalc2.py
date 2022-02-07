def computepay(h, r):
    if h > 40:
        overtime = h - 40.0
        result = (40.0 * r) + (overtime * r * 1.5)
    else:
        result = h * r
    return result


hrs = input("Enter Hours:")
rate = input("Enter hourly rate:")
p = computepay(float(hrs), float(rate))
print("Pay", p)
