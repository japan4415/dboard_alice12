from solid import *
from solid.utils import *
import numpy as np

def inch(n):
    return 25.4 * n

def top_plate_hole():
    sq = square(19.05)
    sq2 = square(inch(0.551))
    sq2 = translate([(19.05-inch(0.551))/2,(19.05-inch(0.551))/2,0])(sq2)
    return sq - sq2

def top_plate_hole4():
    hole = top_plate_hole()
    result = hole
    for i in range(3):
        hole = translate([19.05,0,0])(hole)
        result += hole
    return result

def top_plate_hole4_4_left():
    hole4 = top_plate_hole4()
    result = hole4
    result += translate([-19.05*0.25,19.05,0])(hole4)
    result += translate([19.05*0.25,19.05*2,0])(hole4)
    result += translate([19.05*0.5,-19.05])(hole4)
    result = rotate([0,0,-12])(result)
    return result

scad_render_to_file(top_plate_hole4_4_left()+translate([-19.05,0,0])(top_plate_hole()), "output.scad")