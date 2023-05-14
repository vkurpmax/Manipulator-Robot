import math

def Formulasi():
    global X, Y, Z
    global theta1, theta2, theta3
    global T1a, T2a, T3a
    global T1, T2, T3
    global yperx, c3, c3a, c3b, c3c, yperx2, c3d, c3e, Xa

    L1 = 85     # mm
    L2 = 165    # mm
    L3 = 155    # mm
    
    h = 0
    
    T1a = (T1 / 3.41) - 150
    T2a = (T2 / 3.41) - 60
    T3a = (T3 / 3.41) - 150
    
    theta1 = T1a# * math.pi / 180.0	# Radian
    theta2 = T2a * math.pi / 180.0
    theta3 = T3a * math.pi / 180.0
    
    yperx = math.tan(theta1 * math.pi / 180.0)# * 180.0 / math.pi
    
    
    c3 = math.cos(theta3)# * 180.0 / math.pi
    
    yperx2 = yperx * yperx
    c3c = 1 + yperx2
    
    X = math.sqrt(((c3*2*L2*L3) - (h*h - L2*L2 - L3*L3)) / (1 + yperx*yperx))
    
    c3a = 2*L2*L3
    c3e = c3*c3a
    c3b = h*h - L2*L2 - L3*L3
    c3c = 1 + yperx2
    c3d = c3e - c3b
    Xa = math.sqrt(c3d / c3c)
    
    Y = yperx * X
    
    Z = h + L1

T1 = 613
T2 = 190
T3 = 408

Formulasi()

print("T1a : %f" % (T1a)) 
print("T2a : %f" % (T2a))
print("T3a : %f" % (T3a))

print("theta1 : %f" % (theta1))
print("yperx : %f" % (yperx))
print("c3 : %f" % (c3))
print("c3a : %f" % (c3a))
print("c3e : %f" % (c3e))
print("c3b : %f" % (c3b))
print("c3c : %f" % (c3c))
print("c3d : %f" % (c3d))
print("yperx2 : %f" % (yperx2))
print("Xa : %f" % (Xa))
print("")
print("X : %.f" % (X))
print("Y : %.f" % (Y))
print("Z : %.f" % (Z))

