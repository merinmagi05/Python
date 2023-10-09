#Create a list of colors from comma-separated color names entered by user. Display first
#and last colors.

color=input("Enter the name of colours separated by comas:")
color_list=color.split(",")
print(color_list)
print("First Colour:",color_list[0])
print("Last Colour:",color_list[-1])