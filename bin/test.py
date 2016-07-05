from bikelight import BikeLight
from time import sleep

light = BikeLight()
print("swiping right")
light.swipeArrow("right")
sleep(1)
print("swiping left")
light.swipeArrow("left")
sleep(1)
print("saying Thank You")
light.smiley()

light.clear()
