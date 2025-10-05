"""
Author: Aaron, Jayden, Timothy
Date: 01-20-2023
Purpose: Culminating Project; 1 Player mode
"""

# I
import planeSprites
import pygame
import random
import endScreen1

pygame.init()
pygame.mixer.init()


def game1():
    # D
    screen = pygame.display.set_mode((1158, 480))
    pygame.display.set_caption("Planes")

    # E

    # initialize needed variables
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    # initialize user 1
    user1 = planeSprites.User(100, "planeOne.png", screen)
    # load life images
    lifeImage = pygame.image.load("life.png")
    emptyLife = pygame.image.load("empty.png")
    # load font and label
    systemFont = pygame.font.SysFont("Arial", 30)
    labelLife1 = systemFont.render("Player 1 Lives:", True, (0, 0, 0))
    # load the needed classes/sprites
    sky = planeSprites.Background(screen)
    score = planeSprites.Scorekeep()
    cloud = planeSprites.Cloud()
    cloud.setActive(False)
    cloud.rect.right = 0
    clouds = []
    cloudGroup = pygame.sprite.Group(clouds)
    building = planeSprites.Building()
    building.setActive(True)
    buildings = [building]
    buildingGroup = pygame.sprite.Group(building)
    coin = planeSprites.Coin()
    coins = []
    coin.setActive(False)
    coinGroup = pygame.sprite.Group(coin)
    oneUp = planeSprites.OneUp()
    oneUps = []
    oneUp.setActive(False)
    oneUpGroup = pygame.sprite.Group(oneUp)
    rocket = planeSprites.Rocket()
    rockets = []
    rocket.setActive(False)
    rocketGroup = pygame.sprite.Group(rocket)
    # group all the sprites
    allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
    # initialize the speed
    speed = 165
    # initialize a counter that helps increase speed
    speedCounter = 0
    # initialize a variable that helps with spawns
    frequency = 50
    # initialize the variable that sets the most recent sprite to be created
    recent = building

    # Background music
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Load sounds
    hit = pygame.mixer.Sound("hit.wav")
    hit.set_volume(0.2)
    lifeSound = pygame.mixer.Sound("1UP.wav")
    lifeSound.set_volume(0.2)
    coinSound = pygame.mixer.Sound("coin.wav")
    coinSound.set_volume(0.2)

    # A
    # a
    clock = pygame.time.Clock()
    keepGoing = True
    # l
    while keepGoing:
        # t
        clock.tick(speed)
        # e
        for event in pygame.event.get():
            # if x is hit in top right, quit
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # call user up module if w is hit
                    user1.dirUp()
                elif event.key == pygame.K_s:
                    # call user down module if s is hit
                    user1.dirDown()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    # if w or s key is let go, stop moving
                    user1.dirStop()

        # update the speed
        labelSpeed = systemFont.render("Speed: %s" % speed, True, (0, 0, 0))

        # if there is no cloud, and no building at the same x coordinate, start a randomizer
        if not cloud.getActive() and building.rect.right < 1080 - building.rect.height:
            # randomize if a cloud spawns
            if random.randrange(frequency) == 0:
                # reactivate the cloud class
                cloud = planeSprites.Cloud()
                cloud.setActive(True)
                clouds = [cloud]
                cloudGroup = pygame.sprite.Group(clouds)
                allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                # set recent to cloud
                recent = cloud
            else:
                cloud.setActive(False)
        # if there is no building and no cloud at the same x coordinate, start a randomizer
        if not building.getActive() and cloud.rect.right < 1080 - cloud.rect.height:
            # randomize if a building spawns
            if random.randrange(frequency) == 0:
                building = planeSprites.Building()
                building.setActive(True)
                buildings = [building]
                buildingGroup = pygame.sprite.Group(buildings)
                allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                # set recent to building
                recent = building
            else:
                building.setActive(False)
        # if a collision with a cloud occurs, play the hit sound, take away a life and set cloud to false
        if pygame.sprite.spritecollide(user1, cloudGroup, True):
            user1.setLives(False)
            cloud.setActive(False)
            hit.play()

        # if the cloud is at the right, set cloud to false
        if cloud.getRight() <= 0:
            cloud.setActive(False)

        # if a collision with a building occurs, play the hit sound, take away a life and set building to false
        if pygame.sprite.spritecollide(user1, buildingGroup, True):
            user1.setLives(False)
            building.setActive(False)
            hit.play()

        # if the building is at the right, set building to false
        if building.getRight() <= 0:
            building.setActive(False)

        # if a collision with a coin occurs, play the coin sound, add to user score and set coin to false
        if pygame.sprite.spritecollide(user1, coinGroup, True):
            coin.setActive(False)
            score.user1Coin()
            coinSound.play()

        # if the coin is at the right, set coin to false
        if coin.getRight() <= 0:
            coin.setActive(False)

        # if there is no coin and nothing is at the same x coordinate randomize a number
        if not coin.getActive():
            if recent.rect.right > 1080 - recent.rect.height:
                number = random.randint(0, 500)
                # if that number is 1, spawn a coin
                if number == 1:
                    coin = planeSprites.Coin()
                    coins = [coin]
                    coin.setActive(True)
                    coinGroup = pygame.sprite.Group(coin)
                    allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)

        # if a collision with a oneUp occurs, play the oneUp sound, add a life and set oneUp to false
        if pygame.sprite.spritecollide(user1, oneUpGroup, True):
            oneUp.setActive(False)
            user1.setLives(True)
            lifeSound.play()

        # if oneup is at the right, set oneup to false
        if oneUp.getRight() <= 0:
            oneUp.setActive(False)

        # if there is no oneup and nothing is at the same x coordinate randomize a number
        if not oneUp.getActive():
            if recent.rect.right > 1080 - recent.rect.height:
                number = random.randint(0, 500)
                # if the number is 1 and the user does not have full lives spawn a one up
                if number == 1 and user1.getLives() != 3:
                    oneUp = planeSprites.OneUp()
                    oneUps = [oneUp]
                    oneUp.setActive(True)
                    oneUpGroup = pygame.sprite.Group(oneUp)
                    allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)

        # if a collision with a rocket occurs, play the hit sound, take away a life and set rocket to false
        if pygame.sprite.spritecollide(user1, rocketGroup, True):
            user1.setLives(False)
            rocket.setActive(False)
            hit.play()

        # if rocket is at the right, set rocket to false
        if rocket.getRight() <= 0:
            rocket.setActive(False)

        # if there is no rocket and nothing is at the same x coordinate randomize a number
        if not rocket.getActive():
            number = random.randint(0, 50)
            # if the number is 1, spawn a rocket
            if number == 1:
                rocket = planeSprites.Rocket()
                rocket.setActive(True)
                rockets = [rocket]
                rocketGroup = pygame.sprite.Group(rocket)
                allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)

        # add to user score
        score.user1Score()

        # move all sprites
        cloud.move()
        building.move()
        coin.move()
        oneUp.move()
        rocket.move()

        # add to the counter
        speedCounter += 1

        # if the counter is divisible by 1000, increase the speed, reset the counter and change the frequency of spawns
        if speedCounter % 1000 == 0:
            speed += 10
            speedCounter = 0
            if frequency > 1:
                frequency -= 2

        # r
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        screen.blit(labelLife1, (847, 20))
        screen.blit(labelSpeed, (1000, 450))

        # if the user has 3 lives spawn all life images
        if user1.getLives() == 3:
            screen.blit(lifeImage, (1050, 25))
            screen.blit(lifeImage, (1075, 25))
            screen.blit(lifeImage, (1100, 25))
            pygame.display.flip()

        # if the user has 2 lives, spawn 2 life and 1 no life image
        elif user1.getLives() == 2:
            screen.blit(lifeImage, (1050, 25))
            screen.blit(lifeImage, (1075, 25))
            screen.blit(emptyLife, (1100, 25))
            pygame.display.flip()

        # if the user has 1 life, spawn 1 life and 2 no life images
        elif user1.getLives() == 1:
            screen.blit(lifeImage, (1050, 25))
            screen.blit(emptyLife, (1075, 25))
            screen.blit(emptyLife, (1100, 25))
            pygame.display.flip()

        # if the user has no lives, go to the end screen
        elif user1.getLives() <= 0:
            keepGoing = False
            endScreen1.end(score.getUser1())
