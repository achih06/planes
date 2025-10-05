"""
Author:Aaron, Jayden, Timothy
Date: 01-20-2023
Purpose:Culminating Project; Module with all sprites
"""
# import necessary modules
import pygame
import random

# initialize pygame
pygame.init()


class User(pygame.sprite.Sprite):
    """ This class manages the users' sprite. It loads the appropriate plane image. The plane is
    a sprite and requires the desired height, the image needed and the screen as parameters """

    def __init__(self, top, image, screen):
        """
        This function initialize the plane.
        It requires the desired height, the image needed and the screen as parameters
        It does not return anything
        """
        pygame.sprite.Sprite.__init__(self)
        # load the image
        self.image = pygame.image.load(image)
        self.image.convert()
        self.rect = self.image.get_rect()
        # initialize the position
        self.rect.left = 50
        self.rect.top = top
        # start the direction as none
        self.__direction = 0
        # set starting lives as 3"
        self.__lives = 3
        # have the screen as an attribute
        self.__screen = screen

    def dirUp(self):
        """
        This function moves the plane up when called
        No parameters or return
        """
        # move up
        self.__direction = -5

    def dirDown(self):
        """
        This function moves the plane down when called
        No parameters or return
        """
        # move down
        self.__direction = 5

    def dirStop(self):
        """
        This function stops the plane when the button is lifted
        No parameters or return
        """
        # make direction as none
        self.__direction = 0

    def setLives(self, gain):
        """
        This function either adds a life or removes depending on what is hit
        Parameters: Gain, this determines if you should gain or lose a life
        Return: None
        """
        # if gain is true and there is not 3 lives, add a life
        if gain and self.__lives != 3:
            self.__lives += 1
        # if gain is false, lose a life
        elif not gain:
            self.__lives -= 1

    def getLives(self):
        """
        This function gives the amount of lives that the user has
        Parameter: None
        Return: The users amount of lives
        """
        # return the amount of lives
        return self.__lives

    def update(self):
        """
        This function updates the position of the sprite
        Parameters and Return: None
        """
        # update the position
        if self.rect.top + self.__direction > 0 and self.rect.bottom < self.__screen.get_height() - self.__direction:
            self.rect.top += self.__direction


class Cloud(pygame.sprite.Sprite):
    """
    This class creates the cloud, the cloud takes away a life if hit
    """

    def __init__(self):
        """
        Purpose: initialize the clouds image, rect and position
        Parameters: None
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        # import the image
        self.image = pygame.image.load("cloud.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        # set the initial position at a random height
        self.rect.left = 1158
        self.rect.top = random.randint(0, 150)

        self.__active = True

    def move(self):
        """
        Purpose: Move the cloud left
        Parameters: None
        Return: None
        """
        # move the sprite left
        self.rect.left -= 5

    def setActive(self, active):
        """
        Purpose: Activate or deactivate the cloud
        Parameters: Active
        Return: None
        """
        #  active parameter is true then set attribute as true
        if active:
            self.__active = True
        else:
            # if active parameter is false then set attribute to false and reset the position
            self.__active = False
            self.rect.right = 0

    def getActive(self):
        """
        Purpose: Return the active condition when called on
        Parameters: None
        Return: Active as a boolean
        """
        # get the active attribute
        return self.__active

    def getRight(self):
        """
        Purpose: Identify the objects position
        Parameters: None
        Return: The position of the object
        """
        # get the position
        return self.rect.right


class Background(pygame.sprite.Sprite):
    """
    Purpose: Create the moving background
    Parameters: None
    Return:None
    """

    def __init__(self, screen):
        """
        Purpose: Create the moving background
        Parameters: screen size
        Return: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.window = screen
        # import the image
        self.image = pygame.image.load('sky.png')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

    def update(self):
        """
        Purpose:Update the position of the object
        Parameters: none
        Return:none
        """
        # move the image
        self.rect.left -= 1
        # reset the position if it is out of the screen
        if self.rect.right <= self.window.get_width():
            self.rect.left = 0


class Scorekeep(pygame.sprite.Sprite):
    """
    Purpose:Create the scorekeeping sprite
    Parameters:none
    Return:none
    """

    def __init__(self):
        """
        Purpose:Initialize the score
        Parameters:none
        Return:none
        """
        pygame.sprite.Sprite.__init__(self)
        # initialize the font
        self.__font = pygame.font.SysFont("Arial", 30)
        # set the scores as 0
        self.__score1 = 0
        self.__score2 = 0

    def user1Score(self):
        """
        Purpose:Add 1 to user1 score
        Parameters:none
        Return:none
        """
        # add to the score
        self.__score1 += 1

    def user2Score(self):
        """
        Purpose: Add 1 to user 2 score
        Parameters:none
        Return:none
        """
        # add to the score
        self.__score2 += 1

    def user1Coin(self):
        """
        Purpose:Add 250 when user 1 hits a coin
        Parameters:none
        Return:none
        """
        # add to the score
        self.__score1 += 250

    def user2Coin(self):
        """
        Purpose:Add 250 when user 2 hits a coin
        Parameters:none
        Return:none
        """
        # add to the score
        self.__score2 += 250

    def update(self):
        """
        Purpose:Update the users scores
        Parameters:None
        Return:None
        """
        # if the score 2 is not 0, update with 2 player mode scores
        if self.__score2 != 0:
            message = "Player 1 Score: %d | Player 2 Score: %d" % (self.__score1, self.__score2)
            self.image = self.__font.render(message, True, (0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.midright = (1115, 75)
        # else, update 1 player mode scores
        else:
            message = "Player 1 Score: %d" % self.__score1
            self.image = self.__font.render(message, True, (0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.midright = (1115, 75)

    def getUser1(self):
        """
        Purpose:Retrieve the user1 score
        Parameters:none
        Return:user 1 score
        """
        # return the score
        return self.__score1

    def getUser2(self):
        """
        Purpose: Retrieve the user 2 score
        Parameters: None
        Return:user 2 score
        """
        # return the score
        return self.__score2


class Building(pygame.sprite.Sprite):
    """
    Purpose: Create the class for the buildings
    Parameters:None
    Return:None
    """

    def __init__(self):
        """
        Purpose:initialize the building
        Parameters:None
        Return:None
        """
        pygame.sprite.Sprite.__init__(self)
        # load the image
        self.image = pygame.image.load("building.png")
        self.image.convert()
        # randomize the size of the building
        self.__scale = random.randrange(3, 7)
        self.image = pygame.transform.scale(self.image,
                                            (32 * self.__scale, 55 * self.__scale))
        self.rect = self.image.get_rect()
        # initialize the starting position
        self.rect.left = 1158
        self.rect.bottom = 480
        self.__active = True

    def move(self):
        """
        Purpose: Move the cloud
        Parameters:none
        Return:none
        """
        # move the sprite
        self.rect.left -= 5

    def setActive(self, active):
        """
        Purpose:Activate or deactivate the sprite
        Parameters:active
        Return:none
        """
        # if active is true set the attribute to true
        if active:
            self.__active = True
        else:
            # if active is false set the attribute to false and reset the position
            self.__active = False
            self.rect.right = 0

    def getActive(self):
        """
        Purpose:Retrieve the state of the sprite
        Parameters:none
        Return:active
        """
        # get the active state
        return self.__active

    def getRight(self):
        """
        Purpose:Retrieve the position of the sprite
        Parameters:none
        Return:Right
        """
        # get the position
        return self.rect.right


class Coin(pygame.sprite.Sprite):
    """
    Purpose:Create the coin sprite
    Parameters:None
    Return:None
    """

    def __init__(self):
        """
        Purpose:Initialize the coin
        Parameters:None
        Return:None
        """
        pygame.sprite.Sprite.__init__(self)
        # load the image
        self.image = pygame.image.load("coin.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        # initialize the position at a random height
        self.rect.left = 1158
        self.rect.top = random.randint(0, 400)
        self.__active = True

    def move(self):
        """
        Purpose:Move the coin
        Parameters: None
        Return: None
        """
        # move the sprite
        self.rect.left -= 5

    def setActive(self, active):
        """
        Purpose:Set the active attribute as true or false
        Parameters:Active
        Return:None
        """
        # set the active attribute to true
        if active:
            self.__active = True
        else:
            # set the active attribute to false and reset the position
            self.__active = False
            self.rect.right = 0

    def getActive(self):
        """
        Purpose: Retrieve the attribute: active
        Parameters: None
        Return: active attribute as bool
        """
        # get the active attribute
        return self.__active

    def getRight(self):
        """
        Purpose: Retrieve the position
        Parameters: None
        Return: Right
        """
        # get the position
        return self.rect.right


class OneUp(pygame.sprite.Sprite):
    """
    Purpose: Create the one up sprite
    Parameters: None
    Return: None
    """

    def __init__(self):
        """
        Purpose:Initialize the sprite
        Parameters:None
        Return:None
        """
        pygame.sprite.Sprite.__init__(self)
        # load the image
        self.image = pygame.image.load("oneUp.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        # set the position at a random height
        self.rect.left = 1158
        self.rect.top = random.randint(0, 400)
        self.__active = True

    def move(self):
        """
        Purpose:Move the sprite
        Parameters: None
        Return: None
        """
        # move the sprite
        self.rect.left -= 5

    def setActive(self, active):
        """
        Purpose: Set the active attribute as true or false
        Parameters: None
        Return: None
        """
        # set the active attribute to true
        if active:
            self.__active = True
        else:
            # set the active attribute to false and reset the position
            self.__active = False
            self.rect.right = 0

    def getActive(self):
        """
        Purpose:Retrieve the active attribute
        Parameters:None
        Return: Active as bool
        """
        # get the active attribute
        return self.__active

    def getRight(self):
        """
        Purpose:Retrieve the position
        Parameters:None
        Return:None
        """
        # get the position
        return self.rect.right


class Rocket(pygame.sprite.Sprite):
    """
    Purpose:Create the rocket class
    Parameters:None
    Return:None
    """

    def __init__(self):
        """
        Purpose:Initialize the rocket class
        Parameters:None
        Return:None
        """
        pygame.sprite.Sprite.__init__(self)
        # load the image
        self.image = pygame.image.load("rocket.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        # set the position to a random height
        self.rect.left = 1158
        self.rect.top = random.randint(0, 400)
        self.__active = True

    def move(self):
        """
        Purpose:Move the rocket
        Parameters:None
        Return:None
        """
        # move the sprite
        self.rect.left -= 10

    def setActive(self, active):
        """
        Purpose:Set the active attribute as true or false
        Parameters:Active 
        Return:None
        """
        # set the active attribute to true
        if active:
            self.__active = True
        else:
            # set the active attribute to false and reset the position
            self.__active = False
            self.rect.right = 0

    def getActive(self):
        """
        Purpose:Retrieve the active attribute
        Parameters:None
        Return:Active as bool
        """
        # get the active attribute
        return self.__active

    def getRight(self):
        """
        Purpose:Retrieve the position
        Parameters:None
        Return:Right as bool
        """
        return self.rect.right
