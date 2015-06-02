#*****************************************************************************************
# CSCI 6651
# Homework 8 Task 1 Guess Animal
#
# YongDeng_HW8_guess_animal.py
# Author: Yong Deng
# Since: 6-1-2015
# This program lets the user guess animals.
#*****************************************************************************************

class Animal:
	#hints
	animals = {"elephant": ("I have exceptional memory", "I am the largest land-living mammal in the world", "I have a very long nose"), 
				"tiger": ("I am the biggest cat", "I come in black and white or orange and black", "My name start with a 't'"), 
				"bat": ("I use echo-location", "I can fly", "I see well in dark")}

	def __init__(self, animal):
		self.animal = animal

	def guess_who_am_i(self):
		count = 0
		print("\n=====================================================")
		print("I will give you 3 hints, guess what animal I am")
		print("=====================================================\n")

		while (True):
			if (count < 3):
				print (Animal.animals[self.animal][count])
				name = input("WHo am I?: ").lower()
				if name != self.animal:
					print ("\nNope, try again!\n")
					count = count + 1
				else:
					print("\n****You got it! I am a", name)
					break
			else:
				print("I'm out of hints! The answer is:", self.animal, "\n")
				break

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()

#===============================================================================
#Below is the sample output:

# Yongs-MBP-5:~ yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/localPython/YongDeng_HW8_guess_animal.py 

# =====================================================
# I will give you 3 hints, guess what animal I am
# =====================================================

# I have exceptional memory
# WHo am I?: dolphin

# Nope, try again!

# I am the largest land-living mammal in the world
# WHo am I?: elephant

# ****You got it! I am a elephant

# =====================================================
# I will give you 3 hints, guess what animal I am
# =====================================================

# I am the biggest cat
# WHo am I?: lion

# Nope, try again!

# I come in black and white or orange and black
# WHo am I?: tiger

# ****You got it! I am a tiger

# =====================================================
# I will give you 3 hints, guess what animal I am
# =====================================================

# I use echo-location
# WHo am I?: human

# Nope, try again!

# I can fly
# WHo am I?: butterfly

# Nope, try again!

# I see well in dark
# WHo am I?: cat

# Nope, try again!

# I'm out of hints! The answer is: bat 

# Yongs-MBP-5:~ yongdeng$ 




