# -*- coding: utf-8 -*-
#Copyright (c) 2010, Walter Bender

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from constants import *
import math

# header
print "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>"
print "<!-- Created with Emacs -->"
print "<svg"
print "   xmlns:svg=\"http://www.w3.org/2000/svg\""
print "   xmlns=\"http://www.w3.org/2000/svg\""
print "   version=\"1.0\""
print "   width=\"" + str(SWIDTH) + "\""
print "   height=\"" + str(SHEIGHT) + "\">"
print "  <g>"

print "   <path"
print "       d=\"M 0.0,30 L 2400,30\""
print "       style=\"fill:none;stroke:#ffffff;stroke-width:60px;stroke-linecap:square;stroke-linejoin:miter;stroke-opacity:1\" />"

print "  <text style=\"font-size:12px;fill:#000000;\">"
print "      <tspan"
print "       x=\"5\""
print "       y=\"32\""
print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">S</tspan></text>"

for i in range(12, 64):
    r = float(i)/2 * math.pi / 180.
    s = math.sin(r)
    ln = str(float(math.log(s*10)*SCALE + OFFSET))
    if int(i/2) == i/2.0:
        h1 = "0"; h2 = "19"; h3 = "32"	
        print "  <text style=\"font-size:12px;fill:#000000;\">"
        print "      <tspan"
        print "       x=\"" + ln + "\""
        print "       y=\"" + h3 + "\""
        print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(int(i/2)) + "</tspan></text>"
        h4 = "47"
        print "  <text style=\"font-size:12px;fill:#ff0000;\">"
        print "      <tspan"
        print "       x=\"" + ln + "\""
        print "       y=\"" + h4 + "\""
        print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(int(180-(i/2))) + "</tspan></text>"
    else:
        h1 = "0"; h2 = "17";
    print "   <path"
    print "       d=\"M " + ln + "," + h1 + " L " + ln + "," + h2 + "\""
    print "       style=\"fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:square;stroke-linejoin:miter;stroke-opacity:1\" />"
for i in range(32, 63, 2):
    r = float(i) * math.pi / 180.
    s = math.sin(r)
    ln = str(float(math.log(s*10)*SCALE + OFFSET))
    h1 = "0"; h2 = "19"; h3 = "32"	
    print "  <text style=\"font-size:12px;fill:#000000;\">"
    print "      <tspan"
    print "       x=\"" + ln + "\""
    print "       y=\"" + h3 + "\""
    print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(i) + "</tspan></text>"
    if i/4*4 == i:
        h4 = "47"
        print "  <text style=\"font-size:12px;fill:#ff0000;\">"
        print "      <tspan"
        print "       x=\"" + ln + "\""
        print "       y=\"" + h4 + "\""
        print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(int(180-i)) + "</tspan></text>"
    print "   <path"
    print "       d=\"M " + ln + "," + h1 + " L " + ln + "," + h2 + "\""
    print "       style=\"fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:square;stroke-linejoin:miter;stroke-opacity:1\" />"
for i in range(64, 83, 4):
    r = float(i) * math.pi / 180.
    s = math.sin(r)
    ln = str(float(math.log(s*10)*SCALE + OFFSET))
    if int(i/4*4) == i:
        h1 = "0"; h2 = "19"; h3 = "32"	
        print "  <text style=\"font-size:12px;fill:#000000;\">"
        print "      <tspan"
        print "       x=\"" + ln + "\""
        print "       y=\"" + h3 + "\""
        print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(i) + "</tspan></text>"
        if i/8*8 == i:
            h4 = "47"
            print "  <text style=\"font-size:12px;fill:#ff0000;\">"
            print "      <tspan"
            print "       x=\"" + ln + "\""
            print "       y=\"" + h4 + "\""
            print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(int(180-i)) + "</tspan></text>"
    elif int((i/2)*2) == i:
        h1 = "0"; h2 = "17";
    else:
        h1 = "0"; h2 = "15";
    print "   <path"
    print "       d=\"M " + ln + "," + h1 + " L " + ln + "," + h2 + "\""
    print "       style=\"fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:square;stroke-linejoin:miter;stroke-opacity:1\" />"

i = 90
r = float(i) * math.pi / 180.
s = math.sin(r)
ln = str(float(math.log(s*10)*SCALE + OFFSET))
h1 = "0"; h2 = "19"; h3 = "32"	
print "  <text style=\"font-size:12px;fill:#000000;\">"
print "      <tspan"
print "       x=\"" + ln + "\""
print "       y=\"" + h3 + "\""
print "       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;\">" + str(i) + "</tspan></text>"
print "   <path"
print "       d=\"M " + ln + "," + h1 + " L " + ln + "," + h2 + "\""
print "       style=\"fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:square;stroke-linejoin:miter;stroke-opacity:1\" />"

# footer
print "  </g>"
print "</svg>"
