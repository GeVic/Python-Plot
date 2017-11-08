import pygame, sys
from pygame import*
pygame.init()
import math
from math import*




#speaking sound



def graphpaper(k):

     # SOME VARIABLE WHICH NEEDS TO BE DEFINED EVERY WHERE
     font = pygame.font.SysFont('Comic Sans MS',20)
     font2 = pygame.font.SysFont('Century',20)
     white = (255,255,255)
     black =(0,0,0)
     point = (51, 102, 153)
     gridcolor = (100, 250, 240) #blue
     graphcolor = (0,150,0)
     purple = (128,0,128) 
     titlecolor = (0,0,128)

     width, height = 500, 500
     extrawidth = 500
     screen=pygame.display.set_mode((width+extrawidth,height))
     screen.fill(white)
     # TILL HERE

     screen.set_clip(0,0, width, height)
     screen.fill(white)

     #draw graph lines
     
     for i in range(int(width/k)):
          
          gridx = k*i
          gridy = k*i
          pygame.draw.aaline(screen, gridcolor, (gridx, 0), (gridx, height), 1)
          pygame.draw.aaline(screen, gridcolor, (0, gridy), (width, gridy), 1)

     #boundary lines
     pygame.draw.line(screen, gridcolor, (width, 0), (width, height), 7)

     #making our axis
     midx = width/(2*k)
     midy = height/(2*k)
     pygame.draw.line(screen, black, (midx*k, 0 ), (midx*k, height), 3)
     pygame.draw.line(screen, black, (0, midy*k), (width, midy*k), 3)
      
     #reset the screen to full
     screen.set_clip(None)

def main():

     # SOME VARIABLE WHICH NEEDS TO BE DEFINED EVERY WHERE
     font = pygame.font.SysFont('Comic Sans MS',20)
     font2 = pygame.font.SysFont('Century',20)
     white = (255,255,255)
     black =(0,0,0)
     point = (51, 102, 153)
     gridcolor = (100, 250, 240) #blue
     graphcolor = (0,150,0)
     purple = (128,0,128) 
     titlecolor = (0,0,128)
     width, height = 500, 500
     extrawidth = 500
     screen=pygame.display.set_mode((width+extrawidth,height))
     pygame.display.set_caption("WANTS TO GRAPH THEN USE THIS")
     screen.fill(white)
     #TILL HERE
     
      

     screen.fill(white)

     #calling graphpaper function 
     k = 25
     graphpaper(k)

     #instruction to give on extra widths
     title = font2.render(" Veeki's Grapher  ;) ", 2, titlecolor)
     screen.blit(title, (width+10, 20))

     instruction = font.render(" Type Your Equation:", 2, black)
     screen.blit(instruction, (width+10, 70))
     
     instruction = font.render(" Press 'Enter' if done or press 'q' to startover :", 2, black)
     screen.blit(instruction, (width+10, 100))

     #list for equation
     equation = []
     done = False
     

     #related with  mouse and keyboard
     active = True
     while active:
         
         
         #here we are overlapping the equation with a white screen
         screen.set_clip(width+10, height-40, width+extrawidth, height)
         screen.fill(white)

         #equation without commas
         eqn = "".join(equation)
         eqn = eqn.replace(" ", "")

         #rendering equation
         eqshow = font.render("Function : y = "+eqn, 1, titlecolor)
         screen.blit(eqshow, (width+10, height-40))
            
         #it updates the screen 
         pygame.display.update()

         for event in pygame.event.get(): 
             if event.type == pygame.QUIT:
                 active = False
                 done = True 

             elif event.type == pygame.KEYDOWN:


                  #for accessing operations
                  if event.unicode == u'*':
                       equation.append("*")
                  elif event.unicode == u'(':
                       equation.append("(")
                  elif event.unicode == u')':
                       equation.append(")")
                  elif event.unicode == u'^':
                       equation.append('**')
                  elif event.unicode == u'/':
                       equation.append("/")
                  elif event.unicode == u'-':
                       equation.append("-")
                  elif event.unicode == u'+':
                       equation.append("+")


                  #for accessing numbers abd backspace
                  elif event.key == K_BACKSPACE:
                       if len(equation)>0:
                            l=len(equation)
                            del(equation[l-1])
                  elif event.key == K_1:
                       equation.append("1")
                  elif event.key == K_2:
                       equation.append("2")
                  elif event.key == K_3:
                       equation.append("3")     
                  elif event.key == K_4:
                       equation.append("4")
                  elif event.key == K_5:
                       equation.append("5")
                  elif event.key == K_6:
                       equation.append("6")
                  elif event.key == K_7:
                       equation.append("7")
                  elif event.key == K_8:
                       equation.append("8")
                  elif event.key == K_9:
                       equation.append("9")
                  elif event.key == K_0:
                       equation.append("0")
                  elif event.key == K_x:
                       equation.append("x")
                  elif event.key == K_RETURN:
                       active = False

                  #trig operations
                  elif event.key == K_s:
                       equation.append("sin(")
                  elif event.key == K_c:
                       equation.append("cos(")
                  elif event.key == K_t:
                       equation.append("tan(")
                  elif event.key == K_a:
                       equation.append("abs(")
                  elif event.key == K_r:
                       equation.append("sqrt(")
                  elif event.key == K_l:
                       equation.append("log10(")
                  elif event.key == K_n:
                       equation.append("log(")
                  elif event.key == K_q:
                       main()
                 
                       
                  
                  
                  
     # to quit the program to to continue
     if done:
              pygame.quit()
     else:
              screen.set_clip(width, 0, width + extrawidth, height - 40)
              screen.fill(white)
              screen.set_clip(None)
                  
              #now a function which contains the algo. to plot graph
              graphnow(eqn, k, screen)

     sys.exit()

#graph now function
def graphnow(eqn, k, screen):

     # SOME VARIABLE WHICH NEEDS TO BE DEFINED EVERY WHERE
     font = pygame.font.SysFont('Comic Sans MS',20)
     white = (255,255,255)
     black =(0,0,0)
     point = (255, 0, 0)
     gridcolor = (100, 250, 240) #blue
     graphcolor = (0,100,0)
     purple = (128,0,128) 
     titlecolor = (0,0,128)
     width, height = 500, 500
     extrawidth = 500
     # TILL HERE 
    


     for i in range(width):
         try :
          
            x = ((width/2)-i)/float(k)
            y = eval(eqn)
            position1 = ((width/2+x*k), (height/2-y*k))

            x1 = x = (width/2-(i+1))/float(k)
            y1 = eval(eqn)
            position2 =((width/2+x1*k), (height/2-y1*k))

            pygame.draw.aaline(screen, purple, position1, position2, 3)
            
         except :
              pass


     #instructions on new screen
     instruction = font.render("Press 'q' to startover !", 2, black)
     screen.blit(instruction, (width+10, 20))


     #calculating y intercept
     x = 0
     try:
        yy = eval(eqn)
        yy = int(yy)
     except:
        yy = 'DNE'  
        print("IT D.N.E !!!!!!")
     


     instruction = font.render(" Y - intercept :: (0,"+str(yy)+")", 2, black)
     screen.blit(instruction, (width+10, 50))

     #condition to plot y - intercept
     if yy != 'DNE':
          instruction = font.render(" Press 'y' to plot it !!!", 2, black)
          screen.blit(instruction, (width+10, 100))

     screen.set_clip(None)

     #for plotting x values in graph
     xx = []
     xenter = '!'
     yenter = '!'
     

     #infinite loop 
     active = True
     while active:
          
          

          screen.set_clip(width+10, 150, width+extrawidth, 200)
          screen.fill(white)
          display_screen = "".join(xx)
          display_screen = display_screen.replace(" ", "")
          instruction = font.render(" x = "+str(display_screen), 2, black)
          screen.blit(instruction, (width+10, 150))
          instruction = font.render("("+str(xenter)+","+str(yenter)+")", 2, black)
          screen.blit(instruction, (width+200, 150))

          screen.set_clip(None)
          #it updates the screen again and again
          pygame.display.update()
          
          
          
          
          

          #again keyboard action
          for event in pygame.event.get():
               # motion of keyboard and mouse
               if event.type == pygame.QUIT:
                    active = False

               elif event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                         main()                         
                    elif event.key == K_y:
                         pygame.draw.circle(screen, point, (int(width/2), int(height/2)-yy*k), 3)

                    #for plotting points on graph
                    elif event.key == K_RETURN:
                         xenter = float(display_screen)
                         yenter = eval(eqn)
                         pygame.draw.circle(screen, graphcolor, (int(width/2+int(xenter)*k), int(height/2)-int(yenter)*k), 3)

                    elif event.key == K_1:
                         xx.append("1")
                    elif event.key == K_2:
                         xx.append("2")
                    elif event.key == K_3:
                         xx.append("3")     
                    elif event.key == K_4:
                         xx.append("4")
                    elif event.key == K_5:
                         xx.append("5")
                    elif event.key == K_6:
                         xx.append("6")
                    elif event.key == K_7:
                         xx.append("7")
                    elif event.key == K_8:
                         xx.append("8")
                    elif event.key == K_9:
                         xx.append("9")
                    elif event.key == K_0:  
                         xx.append("0")
                    elif event.unicode == u'.':
                         xx.append(".")
                    elif event.unicode == u'-':
                         xx.append("-")
                         

     #now to quit
     pygame.quit()
              
     
     
if __name__=='__main__':
    main()
         
