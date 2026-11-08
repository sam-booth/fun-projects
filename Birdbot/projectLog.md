# 08/11/2026 Project outline

My goal is to better monitor the birds at the bottom of the garden.
I saw a blackcap there yesterday but the birdnet at the house couldn't pick up the audio and the birds blend in with the leaf litter too well to get a good view with the binoculars. 

I want to stream audio and video back to aid in identification, this is pretty heavy so rules out the smaller teensy or rp2040 based microcontrollers. Just from what I have in my drawer the options are an early (underpowered) or later ( overkill) raspberry pi or a pi zero 1 or 2. The pi zero 2 seems just right, it's small and appropriately powered for my use case and has wireless built in.
The requirements will be pan/tilt for the camera, remote motor control, audio in and out, and video streaming. 

I chose to cannibalise an rc car rather than build my own chassis because it already has its own suspension system and it was sitting in a drawer doing nothing. The motor controller is an inventor hat mini, I chose this because it was cheap and has the IO I need.

For camouflage I have borrowed a toy squirrel from my dog, he won't notice.

The rc car has no charger so I'm starting with prototyping jump leads to a usb plug i had laying around, not permanent but working for now.

![A squirrel duct taped to a car](images/test-fit.png)

## 08/11/2026 11:08 AM - Test 01

The first official test run of Agent Acorns sees him duct taped to the stripped down chassis of the car and charging down the hill towards two other (real) squirrels.

While the squirrels did run away, and Agent Acorn ran out of battery and got stuck in the long grass, initial testing has been very successful.

Next steps are to work on the charging system, setup the pi zero, further strip down the car, increase antenna range, and investigate replacing the motors with more powerful ones I have in inventory. 

![A very realistic squirrel in the grass](images/field-test-01.png)

## 08/11/2026 - 14:32 Post nap clarity

I tried disassembling the 'axles' to access the motors in the toy car this morning but they are impressively glued shut and potentially breaking them is not a priority.

Agent Acorns now has sunglasses, because all good agents have them.

The zero is up and running and I'm learning about flask, this is surprisingly relevant and i'm getting a peek into how all those developers I used to work with set up their web applications - I'm sure we're using the same flawed tutorials.

I debated a good while between using a physical controller or building a web interface to control Agent Acorns; both are good but I already have too many things to hold while birding and a web app would save using lipo batteries.
