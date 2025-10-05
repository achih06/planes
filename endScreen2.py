"""
Author: Aaron, Jayden, Timothy
Date: 01-20-2023
Purpose: Culminating Project; End screen for 2 player mode
"""

# I - Import and Initialize
import pygame
import mode2
import planeSprites

pygame.init()
pygame.mixer.init()


def end(score1, score2):
    # D - Display configuration
    screen = pygame.display.set_mode((1158, 480))
    pygame.display.set_caption("Game Over")

    # E - Entities
    # Background and score
    sky = planeSprites.Background(screen)
    allSprites = pygame.sprite.OrderedUpdates(sky)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((191, 239, 255))

    # sound effect
    highSound = pygame.mixer.Sound("highscore.wav")
    highSound.set_volume(0.2)

    # highscore
    highscore = open("highscore.txt", 'r')
    # read the highscore and turn into an integer
    line = highscore.readline()
    line = int(line)

    # close the file
    highscore.close()

    # if score 1 is a high score and bigger than score2, rewrite the file to have the new high score
    if (score1 > score2 and score1 > line) or (score1 == score2 and score1 > line):
        highscore = open("highscore.txt", 'w')
        highscore.write(str(score1))
        highscore.close()
        highSound.play()
    # if score 2 is a high score and bigger than score 1, rewrite the file to have the new high score
    elif score2 > score1 and score2 > line:
        highscore = open("highscore.txt", 'w')
        highscore.write(str(score2))
        highscore.close()
        highSound.play()

    # reread the highscore in case it was updated
    highscore = open("highscore.txt", 'r')
    high = highscore.readline()
    high = int(high)
    highscore.close()

    # create the label for highscore
    mySystemFont = pygame.font.SysFont("Arial", 25)
    labelHigh = mySystemFont.render("Highscore: %d" % high, True, (0, 0, 0))

    # Text
    mySystemFont = pygame.font.SysFont("Arial", 80)
    gameOver = mySystemFont.render("GAME OVER", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 25)
    goodGame = mySystemFont.render("Good Game!", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 18)
    player1Score = mySystemFont.render(("Player 1 Score: %s" % score1), True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 18)
    player2Score = mySystemFont.render(("Player 2 Score: %s" % score2), True, (0, 0, 0))

    # display appropriate message for winner
    if score1 > score2:
        mySystemFont = pygame.font.SysFont("Arial", 30)
        winner = mySystemFont.render("Player 1 wins!", True, (0, 0, 0))
    elif score2 > score1:
        mySystemFont = pygame.font.SysFont("Arial", 30)
        winner = mySystemFont.render("Player 2 wins!", True, (0, 0, 0))
    else:
        mySystemFont = pygame.font.SysFont("Arial", 30)
        winner = mySystemFont.render("   Tie game   ", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 20)
    play = mySystemFont.render("Type 'P' to play again!", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 20)
    end = mySystemFont.render("Type 'Q' to quit", True, (0, 0, 0))

    # Background music
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True

    # L - Loop
    while keepGoing:

        # T - Timer to set frame rate
        clock.tick(30)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    keepGoing = False
                    mode2.game2()
                elif event.key == pygame.K_q:
                    keepGoing = False

        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        screen.blit(gameOver, (380, 80))
        screen.blit(goodGame, (535, 170))
        screen.blit(player1Score, (530, 250))
        screen.blit(player2Score, (530, 280))
        screen.blit(play, (515, 380))
        screen.blit(end, (542, 410))
        screen.blit(winner, (520, 320))
        screen.blit(labelHigh, (510, 220))
        pygame.display.flip()
