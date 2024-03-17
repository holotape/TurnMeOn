from gpiozero import LED
from time import sleep

def toggle_power(duration):
    power_switch.on()
    sleep(duration)
    power_switch.off()

# Replace "17" if you're using a different pin. Note that this is the BCM number, not the BOARD number.
# In this scenario, I'm using GPIO17, which is on board pin 11.
# For more info, check the official donkumentation https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
power_switch = LED(17)

print("==============================================================================")    
print("Hello! This is the TURN ME ON remote PC button pusher script.")
print("https://www.github.com/holotape/TurnMeOn")
print("Note that if the computer is already off, either answer will turn it on.")
print("And, depending on how you've setup your power button to behave, setting 'ON' when the computer is on may put your PC to sleep.")
print("Check if your PC is online before running this script.")
print("Type your favourite colour to exit without toggling.")
print("==============================================================================")

user_input = input("So, would you like to turn the computer ON or OFF? Please type 'ON' or 'OFF': ")

if user_input == "ON":
    print("Turning the computer on...")
    toggle_power(1)
elif user_input == "OFF":
    print("Turning the computer off...")
    toggle_power(3)
else:
    print("Invalid input. Please type 'ON' or 'OFF'.")

print("Operation completed.")

