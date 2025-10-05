
# I - Import and Initialize
import mode1
import mode2
import planeSprites
import pygame

pygame.init()


def main():
    """This function defines the 'mainline logic' for our game."""

    # D - Display configuration
    screen = pygame.display.set_mode((1158, 480))
    pygame.display.set_caption("Planes Game")

    # E - Entities
    # import the background screen
    sky = planeSprites.Background(screen)
    allSprites = pygame.sprite.OrderedUpdates(sky)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((191, 239, 255))

    # Text for titles, labels, controls
    mySystemFont = pygame.font.SysFont("Arial", 40)
    GameTitle = mySystemFont.render("Planes", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 20)
    player1ctrl = mySystemFont.render("Player 1 Controls", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 20)
    player2ctrl = mySystemFont.render("Player 2 Controls", True, (0, 0, 0))

    # Text for How to play the game
    mySystemFont = pygame.font.SysFont("Arial", 16)
    rules = mySystemFont.render("How To Play!", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 12)
    playerMode = mySystemFont.render("You can play in a 1 player mode or 2 players", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 12)
    gameEnd = mySystemFont.render("The game ends when lives are lost by hitting a cloud or building", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 12)
    playerEnd = mySystemFont.render(
        "The game ends in 1 player when the player loses. The game ends in 2 players when both players lose", True,
        (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 12)
    play = mySystemFont.render(
        "Achieve a high score by earning points through time or hitting coins for a score booster!", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 12)
    life = mySystemFont.render(
        "You begin with 3 lives. However, you can earn another only if you have one by hitting a heart powerup", True,
        (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 12)
    speed = mySystemFont.render("The game gets faster the further you get", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 16)
    playerSelect = mySystemFont.render("Type '1' for 1 player or '2' for 2 players", True, (0, 0, 0))

    mySystemFont = pygame.font.SysFont("Arial", 16)
    goodLuck = mySystemFont.render("Good Luck!!!", True, (0, 0, 0))

    # Display images for player controls
    keyw = pygame.image.load("wkey.png")

    keys = pygame.image.load("skey.png")

    keyi = pygame.image.load("ikey.png")

    keyk = pygame.image.load("kkey.png")

    # Background music
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    # initialize the clock and keepGoing variable
    clock = pygame.time.Clock()
    keepGoing = True

    # L - Loop
    while keepGoing:

        # T - Timer to set frame rate
        clock.tick(100)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    keepGoing = False
                    mode1.game1()
                elif event.key == pygame.K_2:
                    keepGoing = False
                    mode2.game2()

        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        screen.blit(GameTitle, (40, 40))
        screen.blit(player1ctrl, (715, 60))
        screen.blit(player2ctrl, (950, 60))
        screen.blit(keyw, (750, 125))
        screen.blit(keys, (750, 230))
        screen.blit(keyi, (985, 125))
        screen.blit(keyk, (985, 230))
        screen.blit(rules, (40, 115))
        screen.blit(playerMode, (40, 145))
        screen.blit(gameEnd, (40, 170))
        screen.blit(playerEnd, (40, 195))
        screen.blit(play, (40, 220))
        screen.blit(life, (40, 245))
        screen.blit(speed, (40, 274))
        screen.blit(playerSelect, (40, 310))
        screen.blit(goodLuck, (40, 340))
        pygame.display.flip()
    pygame.quit()


# Call the main function
main()
