RED = 'red'
BLUE = 'blue'
YELLOW = 'yellow'
color1, color2=input().split(" ")
list_of_colors = (RED,BLUE,YELLOW)

if color1 == color2:
    print("Error: The two colors you entered are the same.")
elif color1 not in list_of_colors :
    print("Error: The first color you entered is invalid.")
elif color2 not in list_of_colors:
    print("Error: The second color you entered is invalid.")
else:
    if (color1 == RED and color2 == BLUE) or color1 == BLUE and color2 == RED:
        print("purple")
    elif (color1 == BLUE and color2 == YELLOW) or (color1 == YELLOW and color2 == BLUE):
        print("green")
    else: 
        print("orange")