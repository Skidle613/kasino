import random
import time
import pygame
from blackjack.Buttons import *


# b before the variable means it is boolean
class Assets:
    # loading in and converting the application icon and cards
    def __init__(self):
        self.icon = pygame.image.load("blackjack\\Assets/blackjack.png")
        self.Cardback = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Cardback.png").convert(),
                                               (100, 140))
        self.ClubsAce = pygame.transform.scale(pygame.image.load("blackjack\\Assets/ClubsAce.png").convert(),
                                               (100, 140))
        self.Clubs2 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs2.png").convert(), (100, 140))
        self.Clubs3 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs3.png").convert(), (100, 140))
        self.Clubs4 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs4.png").convert(), (100, 140))
        self.Clubs5 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs5.png").convert(), (100, 140))
        self.Clubs6 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs6.png").convert(), (100, 140))
        self.Clubs7 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs7.png").convert(), (100, 140))
        self.Clubs8 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs8.png").convert(), (100, 140))
        self.Clubs9 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs9.png").convert(), (100, 140))
        self.Clubs10 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Clubs10.png").convert(), (100, 140))
        self.ClubsJack = pygame.transform.scale(pygame.image.load("blackjack\\Assets/ClubsJack.png").convert(),
                                                (100, 140))
        self.ClubsQueen = pygame.transform.scale(pygame.image.load("blackjack\\Assets/ClubsQueen.png").convert(),
                                                 (100, 140))
        self.ClubsKing = pygame.transform.scale(pygame.image.load("blackjack\\Assets/ClubsKing.png").convert(),
                                                (100, 140))
        self.DiamondsAce = pygame.transform.scale(pygame.image.load("blackjack\\Assets/DiamondsAce.png").convert(),
                                                  (100, 140))
        self.Diamonds2 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds2.png").convert(),
                                                (100, 140))
        self.Diamonds3 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds3.png").convert(),
                                                (100, 140))
        self.Diamonds4 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds4.png").convert(),
                                                (100, 140))
        self.Diamonds5 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds5.png").convert(),
                                                (100, 140))
        self.Diamonds6 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds6.png").convert(),
                                                (100, 140))
        self.Diamonds7 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds7.png").convert(),
                                                (100, 140))
        self.Diamonds8 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds8.png").convert(),
                                                (100, 140))
        self.Diamonds9 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds9.png").convert(),
                                                (100, 140))
        self.Diamonds10 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Diamonds10.png").convert(),
                                                 (100, 140))
        self.DiamondsJack = pygame.transform.scale(pygame.image.load("blackjack\\Assets/DiamondsJack.png").convert(),
                                                   (100, 140))
        self.DiamondsQueen = pygame.transform.scale(pygame.image.load("blackjack\\Assets/DiamondsQueen.png").convert(),
                                                    (100, 140))
        self.DiamondsKing = pygame.transform.scale(pygame.image.load("blackjack\\Assets/DiamondsKing.png").convert(),
                                                   (100, 140))
        self.HeartsAce = pygame.transform.scale(pygame.image.load("blackjack\\Assets/HeartsAce.png").convert(),
                                                (100, 140))
        self.Hearts2 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts2.png").convert(), (100, 140))
        self.Hearts3 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts3.png").convert(), (100, 140))
        self.Hearts4 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts4.png").convert(), (100, 140))
        self.Hearts5 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts5.png").convert(), (100, 140))
        self.Hearts6 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts6.png").convert(), (100, 140))
        self.Hearts7 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts7.png").convert(), (100, 140))
        self.Hearts8 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts8.png").convert(), (100, 140))
        self.Hearts9 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts9.png").convert(), (100, 140))
        self.Hearts10 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Hearts10.png").convert(),
                                               (100, 140))
        self.HeartsJack = pygame.transform.scale(pygame.image.load("blackjack\\Assets/HeartsJack.png").convert(),
                                                 (100, 140))
        self.HeartsQueen = pygame.transform.scale(pygame.image.load("blackjack\\Assets/HeartsQueen.png").convert(),
                                                  (100, 140))
        self.HeartsKing = pygame.transform.scale(pygame.image.load("blackjack\\Assets/HeartsKing.png").convert(),
                                                 (100, 140))
        self.SpadesAce = pygame.transform.scale(pygame.image.load("blackjack\\Assets/SpadesAce.png").convert(),
                                                (100, 140))
        self.Spades2 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades2.png").convert(), (100, 140))
        self.Spades3 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades3.png").convert(), (100, 140))
        self.Spades4 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades4.png").convert(), (100, 140))
        self.Spades5 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades5.png").convert(), (100, 140))
        self.Spades6 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades6.png").convert(), (100, 140))
        self.Spades7 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades7.png").convert(), (100, 140))
        self.Spades8 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades8.png").convert(), (100, 140))
        self.Spades9 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades9.png").convert(), (100, 140))
        self.Spades10 = pygame.transform.scale(pygame.image.load("blackjack\\Assets/Spades10.png").convert(),
                                               (100, 140))
        self.SpadesJack = pygame.transform.scale(pygame.image.load("blackjack\\Assets/SpadesJack.png").convert(),
                                                 (100, 140))
        self.SpadesQueen = pygame.transform.scale(pygame.image.load("blackjack\\Assets/SpadesQueen.png").convert(),
                                                  (100, 140))
        self.SpadesKing = pygame.transform.scale(pygame.image.load("blackjack\\Assets/SpadesKing.png").convert(),
                                                 (100, 140))


class App:
    def __init__(self):
        # draw on the surface
        self.Surface = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("pygameBlackjack")
        # background is mostly static
        self.Background = pygame.Surface(self.Surface.get_size())
        self.Background.fill((80, 150, 15))

        self.Font = pygame.font.SysFont("arial", 15)

        self.bRun = True
        self.bGameOver = False

        self.Assets = Assets()
        pygame.display.set_icon(self.Assets.icon)

        self.HitButton = HitButton(self, (192, 192, 192), (10, 445, 75, 25))
        self.StandButton = StandButton(self, (192, 192, 192), (95, 445, 75, 25))
        self.RestartButton = RestartButton(self, (192, 192, 192), (270, 225, 75, 25))

        self.WinNum = 0
        self.LoseNum = 0

        # putting all the cards into a list
        self.Cards = [
            self.Assets.ClubsAce, self.Assets.DiamondsAce, self.Assets.HeartsAce, self.Assets.SpadesAce,
            self.Assets.Clubs2, self.Assets.Diamonds2, self.Assets.Hearts2, self.Assets.Spades2,
            self.Assets.Clubs3, self.Assets.Diamonds3, self.Assets.Hearts3, self.Assets.Spades3,
            self.Assets.Clubs4, self.Assets.Diamonds4, self.Assets.Hearts4, self.Assets.Spades4,
            self.Assets.Clubs5, self.Assets.Diamonds5, self.Assets.Hearts5, self.Assets.Spades5,
            self.Assets.Clubs6, self.Assets.Diamonds6, self.Assets.Hearts6, self.Assets.Spades6,
            self.Assets.Clubs7, self.Assets.Diamonds7, self.Assets.Hearts7, self.Assets.Spades7,
            self.Assets.Clubs8, self.Assets.Diamonds8, self.Assets.Hearts8, self.Assets.Spades8,
            self.Assets.Clubs9, self.Assets.Diamonds9, self.Assets.Hearts9, self.Assets.Spades9,
            self.Assets.Clubs10, self.Assets.Diamonds10, self.Assets.Hearts10, self.Assets.Spades10,
            self.Assets.ClubsJack, self.Assets.DiamondsJack, self.Assets.HeartsJack, self.Assets.SpadesJack,
            self.Assets.ClubsQueen, self.Assets.DiamondsQueen, self.Assets.HeartsQueen, self.Assets.SpadesQueen,
            self.Assets.ClubsKing, self.Assets.DiamondsKing, self.Assets.HeartsKing, self.Assets.SpadesKing
        ]

        self.CardPool = []
        self.PlayerHand = []
        self.DealerHand = []

        self.PlayerHandValue = 0
        self.PlayerAces = 0
        self.DealerHandValue = 0
        self.DealerAces = 0

    def InitHands(self):
        # deals 2 cards to player and dealer
        for i in range(2):
            value, bIsAce = self.GetCard(self.PlayerHand)

            self.PlayerHandValue += value
            self.PlayerAces += bIsAce

            value, bIsAce = self.GetCard(self.DealerHand)

            self.DealerHandValue += value
            self.DealerAces += bIsAce

    def ResetHands(self):
        # clears everything and resets CardPool
        self.CardPool = self.Cards.copy()
        self.PlayerHand.clear()
        self.DealerHand.clear()

        self.PlayerHandValue = 0
        self.PlayerAces = 0
        self.DealerHandValue = 0
        self.DealerAces = 0

        self.bGameOver = False

        self.InitHands()

    # rendering method
    def Render(self):
        self.Surface.blit(self.Background, (0, 0))

        winText = self.Font.render(f"{self.WinNum} Wins", 1, (0, 0, 0))
        loseText = self.Font.render(f"{self.LoseNum} Losses", 1, (0, 0, 0))

        for i in range(len(self.PlayerHand)):
            x = 10 + i * 110
            self.Surface.blit(self.PlayerHand[i], (x, 295))

        if self.bGameOver and self.WinNum != 3 and self.LoseNum != 3:
            for i in range(len(self.DealerHand)):
                x = 10 + i * 110
                self.Surface.blit(self.DealerHand[i], (x, 10))

            self.RestartButton.Render()

        if self.WinNum > 2:
            winResult = self.Font.render(f"Вы победили!", 1, (0, 0, 0))
            self.Surface.blit(winResult, (565, 472))

        if self.LoseNum > 2:
            loseResult = self.Font.render(f"Вы проиграли.", 1, (0, 0, 0))
            self.Surface.blit(loseResult, (565, 498))


        else:
            self.Surface.blit(self.DealerHand[0], (10, 10))
            self.Surface.blit(self.Assets.Cardback, (120, 10))

        self.Surface.blit(winText, (565, 423))
        self.Surface.blit(loseText, (565, 448))

        pygame.display.update()

    # event handling
    def PollEvents(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.bRun = False
                return
            self.HitButton.OnEvent(event)
            self.StandButton.OnEvent(event)

    def GetCardValue(self, card):
        index = self.Cards.index(card)

        if (index < 4):
            return 11
        elif (index > 35):
            return 10
        else:
            return int(index / 4) + 1

    # returns the value, and whether the card is an ace or not
    def GetCard(self, hand):

        card = random.choice(self.CardPool)
        self.CardPool.remove(card)

        hand.append(card)

        value = self.GetCardValue(card)

        if (value == 11):
            return value, 1
        else:
            return value, 0


def main(wins, loses):
    # initalize
    pygame.init()
    app = App()

    # deal the hands
    app.ResetHands()

    # main loop
    while (app.bRun):
        if (app.bGameOver):
            # pause here so that the player can see the dealer hand
            while (not app.RestartButton.OnEvent()):
                pass
            app.ResetHands()
        # event handling and rendering method
        app.PollEvents()
        render = app.Render()

        if app.WinNum > 2 or app.LoseNum > 2:
            time.sleep(3)
            if app.WinNum > 2:
                return 1
            else:
                return -1