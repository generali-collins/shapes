#Collins Wanga

#Area of a circle
def circleArea(radius):
    area = (22/7*(radius**2))

    return area

#Circumference of a circle
def circleCircumference(radius):
    circumference = (22/7*2*radius)

    return circumference

'''
Area of a trapezoid
#a = base, b = base h= height
'''
def trapezoidArea(a,b,h):
    area = ((a+b)/2*h)
    return area

'''
Perimeter of a trapezoid
#a = side, b = side, c = side, d = side
'''
def trapezoidPerimeter(a,b,c,d):
    perimeter = (a+b+c+d)
    return perimeter

#Surface area of a cylinder
def cylinderArea(radius, height):
    area = ((22/7*(radius**2)*2)+ (2*22/7*radius*height))
    return area

#Volume of a cylinder
def cylinderVolume(radius,height):
    volume = (22/7*(radius**2)*height)
    return volume

#Area of a sphere
def sphereArea(radius):
    area = (4*22/7*(radius**2))
    return area

#Volume of a sphere
def sphereVolume(radius):
    volume = (4/3*22/7*(radius**3))
    return volume

'''
Other dimensional figure
Surface area of a cone
'''
def coneArea(radius,length):
    area = (22/7*(radius**2))+(22/7*radius*length)
    return area

#Volume of a cone
def coneVolume(radius, height):
    volume = (1/3*22/7*(radius**2)*height)
    return volume
