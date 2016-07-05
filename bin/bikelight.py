from sense_hat import SenseHat
import time as timer

sense = SenseHat()

O = (0,0,0)     #black
X = (255,0,0)   #red
time = 0.05

########################################################
######  Arrow from left to right #######################
########################################################
right_arrow0 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
right_arrow1 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
right_arrow2 = [
    O, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    O, X, X, O, O, O, O, O,
    O, X, X, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
right_arrow3 = [
    X, O, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    O, X, X, O, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, X, X, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O
]
right_arrow4 = [
    O, X, O, O, O, O, O, O,
    O, X, X, O, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, O, O, O, O,
    O, X, X, O, O, O, O, O,
    O, X, O, O, O, O, O, O
]
right_arrow5 = [
    O, O, X, O, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, X, O, O, O, O, O
]
right_arrow6 = [
    O, O, O, X, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, X, X, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, O, O, O, O
]
right_arrow7 = [
    O, O, O, O, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, X, X, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, X, O, O, O
]
right_arrow8 = [
    O, O, O, O, O, X, O, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, X, O, O
]
right_arrow9 = [
    O, O, O, O, O, O, X, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, O
]
right_arrow10 = [
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, X
]

right_arrow11 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
left_arrow0 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
########################################################
##### Arrow from right to left #########################
########################################################
left_arrow1 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
left_arrow2 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, O, O
]
left_arrow3 = [
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, X, X, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, X
]
left_arrow4 = [
    O, O, O, O, O, O, X, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, X, X, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, X, O,
    O, O, O, O, O, O, X, O
]
left_arrow5 = [
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, O, O
]
left_arrow6 = [
  O, O, O, O, X, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, X, X, O, O, O, O,
  O, X, X, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  O, O, X, X, O, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, O, X, O, O, O
]
left_arrow7 = [
  O, O, O, X, O, O, O, O,
  O, O, X, X, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  O, O, X, X, O, O, O, O,
  O, O, O, X, O, O, O, O
]
left_arrow8 = [
  O, O, X, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  O, O, X, O, O, O, O, O
]
left_arrow9 = [
  O, X, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  O, X, O, O, O, O, O, O
]
left_arrow10 = [
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O
]
left_arrow11 = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O
]
########################################################
#######  Thank you smiley ##############################
########################################################
thank_you = [
  O, O, X, X, X, X, O, O,
  O, X, X, X, X, X, X, O,
  X, X, O, X, X, O, X, X,
  X, X, O, X, X, O, X, X,
  X, O, X, X, X, X, O, X,
  X, X, O, X, X, O, X, X,
  O, X, X, O, O, X, X, O,
  O, O, X, X, X, X, O, O
]

class BikeLight:
    def clear(self):
        sense.clear()
    def blink_pic(self, pic):
        local_time=time+0.05
        for i in range(3):
            sense.set_pixels(pic)
            timer.sleep(local_time)
	    self.clear()
	    timer.sleep(time)
    def swipeArrow(self, direction):
        for i in range (3):
            for i in range(0,11):
                tmp = globals()[str(direction)+"_arrow"+str(i)]
                #tmp = diretion+getattr(self, '_arrow%' % i)
		sense.set_pixels(tmp)
                timer.sleep(time)
    def smiley (self):
        self.blink_pic(thank_you)
