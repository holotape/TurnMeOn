# TurnMeOn

Hello! This is the TurnMeOn remote PC power button pusher script.
https://www.github.com/holotape/TurnMeOn

You may be asking, why?

I bought a motherboard on Aliexpress which does not have the "Boot on Power" option.
I have this computer setup in a remote location, connected to a private VPN.  I use it for AI inferencing, but that's another story.
Sometimes, the power goes out, and when it comes back on, I have no way to turn the PC back on without driving 40km (That's 87 miles. Probably.)
So, my plan is to setup a cheap Raspberry Pi Zero W connected to the same network.
I will connect the Pi's GPIO pins to the PC motherboard's pins used for the power button.
Since the Pi's whole mantra is to boot on power, when I see my PC offline, I will SSH to the Pi and run this script to turn it on.

# Caveats
Note that if the computer is already off, either answer will probably turn it on.
I have 'ON' set to press the button for 1 second, and 'OFF' set to hold the power button for 3 seconds. This version of 'OFF' is the semi-violent version, intended for when your PC is frozen and/or misbehaving.
Depending on your BIOS/OS settings, if the PC is already on and you select 'ON', it may just put your PC to sleep.
Check if your PC is online before running this script.

If you choose to put the Pi INSIDE your PC case, just ensure it has a case and/or doesn't come into contact with anything that could cause a short. I am not responsible for any damages caused by the use of this script, or the hardware configurations I am suggesting. Anyone choosing to use this should already be comfortable with building PCs, and minor jumper wiring. Make sure your PC is turned off at the PSU before attempting to touch the motherboard. Always make sure it is discharged, and so are you.

Depending on how you choose to wire this, your PC's actual power button may no longer work.
