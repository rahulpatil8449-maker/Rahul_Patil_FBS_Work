## With passing parameters  (w input)
## Without returning values  (w/o output)  -  not using return keyword to return value/data 

def circle_area(r):
    area = 3.14 * r * r
    print(f"The Area of the Circle having radius {r} wiil bee: {area}.")       # using print function to return area instead of return keyword

r = float(input("Enter the radius of thr circle: "))
circle_area(r)