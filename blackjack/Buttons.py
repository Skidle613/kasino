import sys

import pygame

class Button:
	# button render code
	def __init__(self, app, color, rect):
		self.Button = pygame.draw.rect(app.Background, color, rect)
		self.App = app

	def OnEvent(self, event):
		pass

class HitButton(Button):
	# HitButton render code
	def __init__(self, app, color, rect):
		Button.__init__(self, app, color, rect)
		
		text = app.Font.render("Hit", 1, (0, 0, 0))

		app.Background.blit(text, (39, 448))
		
	def OnEvent(self, event):
		if (event.type == pygame.MOUSEBUTTONDOWN):
			if (self.Button.collidepoint(pygame.mouse.get_pos())):
				# set value and bIsAce after pressing hit
				value, bIsAce = self.App.GetCard(self.App.PlayerHand)

				# change value of PlayerHandValue and PlayerAces
				self.App.PlayerHandValue += value
				self.App.PlayerAces += bIsAce

				# code to change ace value to 1 instead of 11
				while (self.App.PlayerHandValue > 21 and self.App.PlayerAces):
					self.App.PlayerHandValue -= 10
					self.App.PlayerAces -= 1

			# Handles loss if player busts
			if (self.App.PlayerHandValue > 21):
				self.App.LoseNum += 1
				self.App.bGameOver = True

class StandButton(Button):
	# StandButton render code
	def __init__(self, app, color, rect):
		Button.__init__(self, app, color, rect)
		
		text = app.Font.render("Stand", 1, (0, 0, 0))

		app.Background.blit(text, (114, 448))
	
	def OnEvent(self, event):
		if (event.type == pygame.MOUSEBUTTONDOWN):
			if (self.Button.collidepoint(pygame.mouse.get_pos())):
				# dealer plays
				while (self.App.DealerHandValue <= self.App.PlayerHandValue and self.App.DealerHandValue < 17):
					value, bIsAce = self.App.GetCard(self.App.DealerHand)

					# change value of DealerHandValue and DealerAces
					self.App.DealerHandValue += value
					self.App.DealerAces += bIsAce

					# code to change ace value to 1 instead of 11
					while (self.App.DealerHandValue > 21 and self.App.DealerAces):
						self.App.DealerHandValue -= 10
						self.App.DealerAces -= 1

				# handles win or loss if player didn't already bust
				if (self.App.DealerHandValue > 21):
					self.App.WinNum += 1
				elif (self.App.DealerHandValue > self.App.PlayerHandValue):
					self.App.LoseNum += 1
				elif (self.App.DealerHandValue == self.App.PlayerHandValue):
					pass
				else:
					self.App.WinNum += 1
				self.App.bGameOver = True

class RestartButton(Button):
	# RestartButton render code
	def __init__(self, app, color, rect):
		self.App = app
		self.Button = pygame.draw.rect(app.Surface, color, rect)
		self.Color = color
		self.Rect = rect
		
		text = app.Font.render("Restart", 1, (0, 0, 0))
		app.Surface.blit(text, (285, 228))

	def OnEvent(self):
		for event in pygame.event.get():
			if (event.type == pygame.MOUSEBUTTONDOWN):
				if (self.Button.collidepoint(pygame.mouse.get_pos())):
					return True
			elif (event.type == pygame.QUIT):
				sys.exit()

		return False

	def Render(self):
		pygame.draw.rect(self.App.Surface, self.Color, self.Rect)
		
		text = self.App.Font.render("Restart", 1, (0, 0, 0))
		self.App.Surface.blit(text, (285, 228))