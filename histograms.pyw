import numpy as np
import matplotlib.pyplot as plt


def main():

                    # taking the input from the user 
                    label_x = input("Enter the name of  x - axis :")
                    label_y = input("Enter the name of y  - axis :")
                    hist_topic = input("Enter the topic of your histogram :")
                    #list
                    x_values = []
                    y_values = []

                    n = int(input("Enter the no of readings :"))

                    for i in range(n):
                        x_val = int(input("Enter x value :"))
                        x_values.append(x_val)
                        y_val = int(input("Enter y value :"))
                        y_values.append(y_val)
                        

                    #setting the histogram                    
                    plt.hist(x_values,  bins = 10,  alpha=0.4,  label='low')
                    plt.hist(y_values,  bins = 10,  alpha=0.4,  label='high')


                    # making the histogram interactive
                    plt.xlabel(label_x)
                    plt.ylabel(label_y)
                    plt.title(hist_topic)
                    # stoping it to overlap
                    plt.legend(loc='left') 

                    plt.show()

if __name__ == '__main__':
    main()

