
# I - Import and Initialize
import mode1
import planeSprites
import pygame

pygame.init()
pygame.mixer.init()


def end(score):
    # D - Display configuration
    screen = pygame.display.set_mode((1158, 480))
    pygame.display.set_caption("game over")

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

    # Highscore
    highscore = open("highscore.txt", 'r')
    line = highscore.readline()
    line = int(line)
    highscore.close()
    if score > line:
        highscore = open("highscore.txt", 'w')
        highscore.write(str(score))
        highscore.close()
        highSound.play()
    highscore = open("highscore.txt", 'r')
    high = highscore.readline()
    high = int(high)

    mySystemFont = pygame.font.SysFont("Arial", 25)
    labelHigh = mySystemFont.render("Highscore: %d" % high, True, (0, 0, 0))

    # Text display
    mySystemFont = pygame.font.SysFont("Arial", 60)
    gameOver = mySystemFont.render("GAME OVER", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 25)
    goodGame = mySystemFont.render("Good Game!", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 25)
    playerScore = mySystemFont.render(("Player Score: %s" % score), True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 20)
    play = mySystemFont.render("Type 'P' to play again!", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 20)
    end = mySystemFont.render("Type 'Q' to quit", True, (0, 0, 0))

    # Background music
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # A - Action
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
                    mode1.game1()
                elif event.key == pygame.K_q:
                    keepGoing = False

        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        screen.blit(gameOver, (435, 80))
        screen.blit(goodGame, (535, 153))
        screen.blit(playerScore, (512, 275))
        screen.blit(play, (515, 380))
        screen.blit(end, (542, 410))
        screen.blit(labelHigh, (510, 225))
        pygame.display.flip()
