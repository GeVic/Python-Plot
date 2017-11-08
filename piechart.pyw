from tkinter import *
import matplotlib.pyplot as plt


def main():
                        
    
                        slices = []
                        activities = []
                        cols = []

                        #instructions command
                        print("Please use these codes for colours :\n"
                              "r for red\n"
                              "b for blue\n"
                              "k for black\n"
                              "y for yellow\n"
                              "m for magneta\n"
                              "c for cynan\n"
                              "g for green\n")
                        
                        tlt = input("Enter the title to your pie chart :")
                        slice_no = int(input("Enter number of divisions :"))
                        for i in range(slice_no):
                                
                                act = input("Enter the name of the division :")
                                activities.append(act)
                                sl = input("Enter the fraction to be given to  the division :")
                                slices.append(sl)
                                colour = input("Enter the colour of your slices :")
                                cols.append(colour)
                                
                                
                                  
                                       
                         #drwaing the pie chart               
                        plt.pie(slices,
                            labels = activities,
                            colors = cols,
                            startangle = 90,
                            shadow = True,
                            
                            autopct = '%1.1f%%')

                        plt.title(tlt)
                        plt.show()
                        root.mainloop()

#callong main function
if __name__ == '__main__':
        main()

