# condtion --> เงื่อนไข --> if, elif, else

battery_Robot = int(inputZ=("Enter your current battery:"))

if 0 <battery_Robot < 30:
         print("Turn off robot now!!")

elif 38 < battery_Robot < 100:
        print("Keep Runing")

elif battery_Robot == 0:
        print("Ran out of battery")

else:
        print("can not detect battery. Please try again")