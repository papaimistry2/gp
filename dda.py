import matplotlib.pyplot as plt

def dda(x1,y1,x2,y2):
    points_x=[]
    points_y=[]

    dx=x2-x1
    dy=y2-y1

    steps = int(max(abs(dx),abs(dy)))

    x_inc=dx/steps
    y_inc=dy/steps

    x=x1
    y=y1

    for _ in range(steps+1):
        points_x.append(round(x))
        points_y.append(round(y))
        x=x+x_inc
        y=y+y_inc

    return points_x,points_y

# x1 = int(input("Enter starting x-coordinate: "))
# y1 = int(input("Enter starting y-coordinate: "))
# x2 = int(input("Enter ending x-coordinate: "))
# y2 = int(input("Enter ending y-coordinate: "))

x_points,y_points = dda(1,1,5,5)

print(x_points,y_points)


plt.figure()
plt.plot(x_points,y_points,marker='o',color="green")
plt.title("DDA Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()