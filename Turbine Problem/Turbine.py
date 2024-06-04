# Define threshold values
ts = int(input("Enter Turbine Speed: "))
b_temp = int(input("Enter Bearing temperature: "))
wv = int(input("Enter Wind velocity: "))

# Read sensor inputs
if ts <= 1000:
    S = "0"
elif ts > 1000:
    S = "1"
else:
    S = "ALERT! Please enter Turbine Speed, correctly! Thank You."

if b_temp <= 80:
    T = "0"
elif b_temp > 80:
    T = "1"
else:
    T = "ALERT! Please enter Bear temperature, correctly! Thank You."

if wv <= 120:
    W = "0"
elif wv > 120:
    W = "1"
else:
    W = "ALERT! Please enter Wind velocity, correctly! Thank You."


# Calculate binary input values
if S == "1" or "0":
    pass
else:
    print(S)
if T == "1" or "0":
    pass
else:
    print(T)
if W == "1" or "0":
    pass
else:
    print(W)

no_1 = int(S)
no_2 = int(T)
no_3 = int(W)

# Decide whether to turn on or off based on the sum of binary input values
X = no_1 + no_2*no_3
if X == 1:
    turbine_state = "The wind turbine is shutting down (OFF)."
else:
    turbine_state = "Turbine will remain ON."

print(turbine_state)
