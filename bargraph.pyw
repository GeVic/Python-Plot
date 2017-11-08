import numpy as np
import matplotlib.pyplot as plt


def main():
    

                x_axis = [] 
                y1 = []
                y2 = []
                # taking the input from the user
                label_x_axis = input("Enter the label for your x- axis :")
                label_y_axis = input("Enter the label for your 1st y - axis :")
                label_y2_axis = input("Enter the label for your 2nd y- axis :")
                n = int(input("Enter the number of inuts for x_axis :"))

                for i in range(n):
                    xx = int(input("Data for x - axis :"))
                    x_axis.append(xx)
                    yy1 = int(input("Enter the data for y 1 axis :"))
                    y1.append(yy1)
                    yy2 =int(input("Enter the data for y 2 axis: "))
                    y2.append(yy2)
                    
                #setting up the bar graph
                bar_width= 0.4 
                x = np.arange(len(x_axis)) 
                opacity = 0.5 

                                     
                plt.bar(x, y1,  bar_width,  color='blue',  label=label_y_axis,  alpha=opacity)

                plt.bar(x, y2,  bar_width,  color='green', label=label_y2_axis,  alpha=opacity,  bottom=y2)
                plt.legend()
                plt.xlabel(label_x_axis)
                plt.ylabel(label_y_axis)
                plt.title(label_y2_axis)
                plt.xticks(x + bar_width, x_axis) 

               # showing the graph
                plt.tight_layout() 
                plt.show()
if __name__ == '__main__':
    main()
