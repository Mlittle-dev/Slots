"""
program labeldemo.py
author mike 4/26/2021
"""

from breezypythongui import EasyFrame
import random

class slot(EasyFrame):
	"""Displays a greeting in a window"""

	def __init__(self):
		"""Sets up window and the label"""
		EasyFrame.__init__(self, width = 200, height = 200, background = "yellow")
		
		self.numPanel = self.addPanel(row = 2, column = 0, background = "lightblue")
		self.addLabel(text = "Slot machine", row = 0, column = 0, columnspan = 3)
		self.field1 = self.numPanel.addIntegerField(value = 0, row = 1, column = 1, width = 3)
		self.field2 = self.numPanel.addIntegerField(value = 0, row = 1, column = 2, width = 3)
		self.field3 = self.numPanel.addIntegerField(value = 0, row = 1, column = 3, width = 3)

		self.button = self.addButton(text = "Spin!!!", row = 4, column = 0, command = self.spin)

		self.addLabel(text = "Points", row = 5, column = 0, sticky = "NSEW")
		self.pointsField = self.addIntegerField(value = 100, row = 6, column = 0)
		self.resultArea = self.addLabel(text = "",row = 7, column = 0)




	def spin(self):
		num1 = random.randint(1, 9)
		num2 = random.randint(1, 9)
		num3 = random.randint(1, 9)
		result = ""
		points = self.pointsField.getNumber()

		if num1 == num2 and num3:
			result = "JACKPOT"
			points += 30
		elif num1 == num2 or num2 == num3 or num1 == num3:
			result = "two of a kind!"
			points += 10
		else:
			result = "no combantion"
			points -= 10

		if points == 0:
			result = "GAME OVER"
			self.button["state"] = "disabled"




		self.field1.setNumber(num1)
		self.field2.setNumber(num2)
		self.field3.setNumber(num3)
		self.resultArea["text"] = result
		self.pointsField.setNumber(points)







#definition of the main() function for program entry
def main():
	"""Instanciates and pops up window"""
	slot().mainloop()

# Global call to main()
main()