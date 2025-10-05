"""
Author: Aaron, Jayden, Timothy
Date: 01-20-2023
Purpose:Culminating Project; 2 player mode
"""
# I
import endScreen2
import planeSprites
import pygame
import random

pygame.init()
pygame.mixer.init()


def game2():
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
    active1 = True
    # initialize user 2
    user2 = planeSprites.User(200, "planeTwo.png", screen)
    active2 = True
    systemFont = pygame.font.SysFont("Arial", 30)
    # create the labels for the lives
    labelLife1 = systemFont.render("Player 1 Lives:", True, (0, 0, 0))
    labelLife2 = systemFont.render("Player 2 Lives:", True, (0, 0, 0))
    # load life images
    lifeImage = pygame.image.load("life.png")
    emptyLife = pygame.image.load("empty.png")
    # load the needed classes/sprites
    sky = planeSprites.Background(screen)
    score = planeSprites.Scorekeep()
    cloud = planeSprites.Cloud()
    cloud.setActive(False)
    clouds = [cloud]
    cloudGroup = pygame.sprite.Group(clouds)
    building = planeSprites.Building()
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
    rocket.setActive(False)
    rockets = [rocket]
    rocketGroup = pygame.sprite.Group(rocket)
    # group all sprites
    allSprites = pygame.sprite.Group(sky, user1, user2, score, coins, oneUps, rockets, clouds, buildings)
    # initialize the speed
    speed = 150
    # initialize a counter to help increase speed
    speedCounter = 0
    # initialize a frequency that helps with spawns
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
            # if the x in top right is hit, quit
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                # if w is hit call the user 1 up function
                if event.key == pygame.K_w:
                    user1.dirUp()
                # if s is hit call the user 1 down function
                elif event.key == pygame.K_s:
                    user1.dirDown()
                # if i is hit call the user 2 up function
                if event.key == pygame.K_i:
                    user2.dirUp()
                # if k is hit call the user 2 down function
                elif event.key == pygame.K_k:
                    user2.dirDown()
            elif event.type == pygame.KEYUP:
                # if w or s is let go of, stop user 1 movement
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    user1.dirStop()
                # if i or k is let go of, stop user 2 movement
                if event.key == pygame.K_i or event.key == pygame.K_k:
                    user2.dirStop()

        # update the speed
        labelSpeed = systemFont.render("Speed: %s" % speed, True, (0, 0, 0))

        # if there is no cloud, and no building near the same x coordinate start a randomizer
        if not cloud.getActive() and building.rect.right < 1080 - building.rect.height:
            if random.randrange(frequency) == 0:
                # reactivate the cloud class
                cloud = planeSprites.Cloud()
                if (coin.rect.right or oneUp.rect.right) < 1080 - cloud.rect.height:
                    clouds = [cloud]
                    cloudGroup = pygame.sprite.Group(clouds)

                    # if both users are active, group all sprites
                    if active1 and active2:
                        allSprites = pygame.sprite.Group(sky, user1, user2, score, coins, oneUps, rockets, clouds,
                                                         buildings)
                    # if user 2 is not active, group all sprites except for user 2
                    elif active1 and not active2:
                        allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                    # if user 1 is not active, group all sprites except for user 1
                    elif not active1 and active2:
                        allSprites = pygame.sprite.Group(sky, user2, score, coins, oneUps, rockets, clouds, buildings)
                    # change the most recent to cloud
                    recent = cloud
                else:
                    # set active to false
                    cloud.setActive(False)

        # if there is no building and no cloud near the same x coordinate start a randomizer
        if not building.getActive() and cloud.rect.right < 1080 - cloud.rect.height:
            if random.randrange(frequency) == 0:
                # reactivate the building class
                building = planeSprites.Building()
                # if there are no power ups near the spawn, spawn a building
                if (coin.rect.right or oneUp.rect.right) < 1080 - building.rect.height:
                    buildings = [building]
                    buildingGroup = pygame.sprite.Group(buildings)

                    # if both users are active, group all sprites
                    if active1 and active2:
                        allSprites = pygame.sprite.Group(sky, user1, user2, score, coins, oneUps, rockets, clouds,
                                                         buildings)
                    # if user 2 is not active, group all sprites except for user 2
                    elif active1 and not active2:
                        allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                    # if user 1 is not active, group all sprites except for user 1
                    elif not active1 and active2:
                        allSprites = pygame.sprite.Group(sky, user2, score, coins, oneUps, rockets, clouds, buildings)
                    # change the most recent spawn point to building
                    recent = building
                else:
                    # set building active to false
                    building.setActive(False)

        # if there is no coin and nothing near the spawn, start a randomizer
        if not coin.getActive():
            if recent.rect.right < 1080 - recent.rect.height:
                number = random.randint(0, 500)
                # If the random number is 1 reactivate the coin class
                if number == 1:
                    coin = planeSprites.Coin()
                    coins = [coin]
                    coinGroup = pygame.sprite.Group(coin)
                    # if both users are active, group all sprites
                    if active1 and active2:
                        allSprites = pygame.sprite.Group(sky, user1, user2, score, coins, oneUps, rockets, clouds,
                                                         buildings)
                    # if user 2 is not active, group all sprites except for user 2
                    elif active1 and not active2:
                        allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                    # if user 1 is not active, group all sprites except for user 1
                    elif not active1 and active2:
                        allSprites = pygame.sprite.Group(sky, user2, score, coins, oneUps, rockets, clouds, buildings)

        # If there is no one up start a randomizer
        if not oneUp.getActive():
            number = random.randint(0, 500)
            # if the number is 1 and both users have an empty life reactivate the oneup class
            if number == 1 and (user1.getLives() != 3 and user2.getLives() != 3):
                oneUp = planeSprites.OneUp()
                oneUps = [oneUp]
                oneUp.setActive(True)
                oneUpGroup = pygame.sprite.Group(oneUp)
                # if both users are active, group all sprites
                if active1 and active2:
                    allSprites = pygame.sprite.Group(sky, user1, user2, score, coins, oneUps, rockets, clouds,
                                                     buildings)
                # if user 2 is not active, group all sprites except for user 2
                elif active1 and not active2:
                    allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                # if user 1 is not active, group all sprites except for user 1
                elif not active1 and active2:
                    allSprites = pygame.sprite.Group(sky, user2, score, coins, oneUps, rockets, clouds, buildings)

        # if there is no rocket, start a randomizer
        if not rocket.getActive():
            number = random.randint(0, 50)
            # if the random number is one, reactivate the rocket class
            if number == 1:
                rocket = planeSprites.Rocket()
                rocket.setActive(True)
                rockets = [rocket]
                rocketGroup = pygame.sprite.Group(rocket)
                # if both users are active, group all sprites
                if active1 and active2:
                    allSprites = pygame.sprite.Group(sky, user1, user2, score, coins, oneUps, rockets, clouds,
                                                     buildings)
                # if user 2 is not active, group all sprites except for user 2
                elif active1 and not active2:
                    allSprites = pygame.sprite.Group(sky, user1, score, coins, oneUps, rockets, clouds, buildings)
                # if user 1 is not active, group all sprites except for user 1
                elif not active1 and active2:
                    allSprites = pygame.sprite.Group(sky, user2, score, coins, oneUps, rockets, clouds, buildings)

        # if the sprite is off the screen, set it to false
        if cloud.getRight() <= 0:
            cloud.setActive(False)

        # if the sprite is off the screen, set it to false
        if building.getRight() <= 0:
            building.setActive(False)

        # if the sprite is off the screen, set it to false
        if coin.getRight() <= 0:
            coin.setActive(False)

        # if the sprite is off the screen, set it to false
        if oneUp.getRight() <= 0:
            oneUp.setActive(False)

        # if the sprite is off the screen, set it to false
        if rocket.getRight() <= 0:
            rocket.setActive(False)

        # Add score and check collisions for user 1
        if active1:

            # if the user is still alive add to their score
            score.user1Score()

            # if hit a rocket, lose a life,set to false and play the noise
            if pygame.sprite.spritecollide(user1, rocketGroup, True):
                user1.setLives(False)
                rocket.setActive(False)
                hit.play()

            # if hit a oneup and the user has an empty life, add one to the life, set to false and play the noise
            if pygame.sprite.spritecollide(user1, oneUpGroup, True) and user1.getLives() != 3:
                oneUp.setActive(False)
                user1.setLives(True)
                lifeSound.play()

            # if hit a coin, add to score,set to false and play the noise
            if pygame.sprite.spritecollide(user1, coinGroup, True):
                coin.setActive(False)
                score.user1Coin()
                coinSound.play()

            # if hit a building, lose a life,set to false and play the noise
            if pygame.sprite.spritecollide(user1, buildingGroup, True):
                user1.setLives(False)
                building.setActive(False)
                hit.play()

            # if hit a cloud, lose a life,set to false and play the noise
            if pygame.sprite.spritecollide(user1, cloudGroup, True):
                user1.setLives(False)
                cloud.setActive(False)
                hit.play()

        # Add score and check collisions for user 2
        if active2:

            # if the user is still alive add to their score
            score.user2Score()

            # if hit a rocket, lose a life,set to false and play the noise
            if pygame.sprite.spritecollide(user2, rocketGroup, True):
                user2.setLives(False)
                rocket.setActive(False)
                hit.play()

            # if hit a oneup and the user has an empty life, add one to the life, set to false and play the noise
            if pygame.sprite.spritecollide(user2, oneUpGroup, True) and user2.getLives() != 3:
                oneUp.setActive(False)
                user2.setLives(True)
                lifeSound.play()

            # if hit a coin, add to score,set to false and play the noise
            if pygame.sprite.spritecollide(user2, coinGroup, True):
                coin.setActive(False)
                score.user2Coin()
                coinSound.play()

            # if hit a building, lose a life,set to false and play the noise
            if pygame.sprite.spritecollide(user2, buildingGroup, True):
                user2.setLives(False)
                building.setActive(False)
                hit.play()

            # if hit a cloud, lose a life,set to false and play the noise
            if pygame.sprite.spritecollide(user2, cloudGroup, True):
                user2.setLives(False)
                cloud.setActive(False)
                hit.play()

        # move all sprites
        cloud.move()
        building.move()
        coin.move()
        oneUp.move()
        rocket.move()

        # add one to the counter
        speedCounter += 1

        # if the counter is divisible by 1000, add 10 to speed, reset counter and change frequency
        if speedCounter % 1000 == 0:
            speed += 10
            speedCounter = 0
            if frequency > 1:
                frequency -= 2

        # R

        # refresh sprites
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        # Display correct speed
        screen.blit(labelSpeed, (1000, 450))

        # display appropriate amounts of lives
        screen.blit(labelLife1, (550, 20))
        if user1.getLives() == 3:
            screen.blit(lifeImage, (760, 25))
            screen.blit(lifeImage, (785, 25))
            screen.blit(lifeImage, (810, 25))
        elif user1.getLives() == 2:
            screen.blit(lifeImage, (760, 25))
            screen.blit(lifeImage, (785, 25))
            screen.blit(emptyLife, (810, 25))
        elif user1.getLives() == 1:
            screen.blit(lifeImage, (760, 25))
            screen.blit(emptyLife, (785, 25))
            screen.blit(emptyLife, (810, 25))
        elif user1.getLives() <= 0:
            screen.blit(emptyLife, (750, 25))
            screen.blit(emptyLife, (775, 25))
            screen.blit(emptyLife, (800, 25))
            active1 = False
            user1.rect.right = 0

        # display appropriate amounts of lives
        screen.blit(labelLife2, (847, 20))
        if user2.getLives() == 3:
            screen.blit(lifeImage, (1050, 25))
            screen.blit(lifeImage, (1075, 25))
            screen.blit(lifeImage, (1100, 25))
        elif user2.getLives() == 2:
            screen.blit(lifeImage, (1050, 25))
            screen.blit(lifeImage, (1075, 25))
            screen.blit(emptyLife, (1100, 25))
        elif user2.getLives() == 1:
            screen.blit(lifeImage, (1050, 25))
            screen.blit(emptyLife, (1075, 25))
            screen.blit(emptyLife, (1100, 25))
        elif user2.getLives() <= 0:
            screen.blit(emptyLife, (1050, 25))
            screen.blit(emptyLife, (1075, 25))
            screen.blit(emptyLife, (1100, 25))
            active2 = False
            user2.rect.right = 0

        # end game if both users have no lives
        if not active1 and not active2:
            keepGoing = False
            endScreen2.end(score.getUser1(), score.getUser2())

        pygame.display.flip()
