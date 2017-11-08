
import tkinter as tk
import tkinter.constants as constants
import tkinter.messagebox as mbox


#importing files to execute with tkinter
import histograms
import grapherr
import bargraph
import piechart



version='2.0'
class application():
    def __init__(self):
       
        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.wm_iconbitmap("favicon.ico")
        self.root.wm_title("YOUR OWN OPTIONS TO GRAPH")
        button_opt = {'fill': constants.BOTH, 'padx':0, 'pady': 20}
        self.root.configure(background = "gray19")
        
        global version
       
      #Text
        self.l1 = tk.Label(text="Get Started",font=("comic sans", 16), bg ="gray19" ,fg = "floralwhite")
        self.l1.pack(**button_opt)
        self.l2 = tk.Label(text="Version 2.0 "+version,font=("comic sans", 12), bg = "gray19",fg = "floralwhite")
        self.l2.pack(**button_opt)
        
        #2D  GRAPH OPTION
        self.grapherr = tk.Button(self.root, text = '2D Grapher',  fg = "purple1", bg = "ivory2",command = self.callgrapherr)
        self.grapherr.pack(**button_opt)
        self.grapherr.config(width=10, height=3)
        
        #3D GRAPH OPTION
        self.histogram = tk.Button(self.root, text = 'Histogram',fg = "purple1", bg = "ivory2", command=self.callhistogram, bd = 0)
        self.histogram.pack(**button_opt)
        self.histogram.config(width=10, height=3)

        #3D HISTOGRAMS
        self.bargraph = tk.Button(self.root, text = 'Bargraph', fg = "purple1", bg = "ivory2",command=self.callbargraph)
        self.bargraph.pack(**button_opt)
        self.bargraph.config(width=10, height=3)
        
        #calling the pie chart
        self.piechart = tk.Button(self.root, text = 'Piecharts',fg = "purple1", bg = "ivory2", command=self.callpie, bd = 0)
        self.piechart.pack(**button_opt)
        self.piechart.config(width=10, height=3)


        #QUIT BUTTON
        self.quit = tk.Button(self.root, text = 'Quit', fg = "purple1", bg = "ivory2",command=self.quit)
        self.quit.pack(**button_opt)
        self.quit.config(width=10, height=3)

        #Start the frame
        self.root.mainloop()

    
    def callgrapherr(self):

        self.root.destroy()
        grapherr.main()
        
        
    
    def callhistogram(self):
        self.root.destroy()
        histograms.main()
        

    
    def callbargraph(self):
        self.root.destroy()
        bargraph.main()
        

    def callpie(self):
        self.root.destroy()
        piechart.main()
        
    #Quit Application
    def quit(self):
        self.root.destroy()
        
if __name__=="__main__":
    fullapp = application()
def main():
    fullapp = application()

