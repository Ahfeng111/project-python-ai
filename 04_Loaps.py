# While Loop #

import time

Battery_Robot = int(input("Enter Current Battery:"))

while True:
           if 6 < Battery_Robot < 100:
                  
                  Battery_Robot = Battery_Robot
                  # Battery_Robot + = 1
                  
                  print("Current Battery: %d" %Battery_Robot) # Advance Display

                  time.sleep(1) 


           else:
            print("Battery Full")
            break # --> Stop Loops

print ("Thank You")



import time 

Number = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

for Read_Number in Number:
         print(Read_Number)

         time.sleep(1)