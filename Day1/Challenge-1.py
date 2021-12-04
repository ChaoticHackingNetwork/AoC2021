#!/usr/bin/env python3

"""
--- Day 1: Sonar Sweep ---

You're minding your own business on a ship at sea when the overboard alarm goes off! 
You rush to see if you can help. Apparently, one of the Elves tripped and accidentally 
sent the sleigh keys flying into the ocean!

As the submarine drops below the surface of the ocean, it automatically performs a sonar 
sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) 
appears: each line is a measurement of the sea floor depth as the sweep looks further and 
further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 
199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know 
what you're dealing with - you never know if the keys will get carried into deeper water by an 
ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement.
"""


def partOne():
	solver = open('nums.txt').readlines() #Open file and read in lines
	count = 0 #Set counter to 0
	last_num = solver[0] #Set previous number
	for num in solver[1:]: #Loop in numbers after first number
		if num > last_num: #If the number is Greater than last 
			count += 1 #Increase count by 1
		last_num = num  #Reset previous last number
	ans = int(count + 1) #Add one for last index
	answer = str(ans) #Change to string

	#return count
	print(f"{answer} larger measurements...")


def partTwo():
	solver = open('nums.txt').readlines()
	count = 0
	for num in range(len(solver)-3):
		slide_one = int(solver[num]) + int(solver[num+1]) + int(solver[num+2])
		slide_two = int(solver[num+1]) + int(solver[num+2]) + int(solver[num+3])
		if slide_two > slide_one:
			count += 1

	#return count
	print(f"{count} sums are larger...")

partOne()
partTwo()
