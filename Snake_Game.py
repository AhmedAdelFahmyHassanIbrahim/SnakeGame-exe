#Snake Game Developed by Ahmed Adel

#All Copyrights are reserved


#Importing Modules

import pygame , sys , random, time


#initilizing game
check_errors = pygame.init()

#Checking errors
if check_errors[1] > 0:
    print ("(!)Had {0} initilizaing errors ,"
           " Exiting...".format(check_errors))
    sys.exit(-1)
else:
    print("(+) PyGame Successfully initilized")

#Creating A player Surface
#Play Surface

playSurface = pygame.display.set_mode((720 , 460))
pygame.display.set_caption("Snake Game!")


#Colors
red = pygame.Color(255 , 0 ,0) #GameOver
green = pygame.Color(0 , 255 , 0) #Snake
black = pygame.Color(0 , 0 , 0) #Score
white = pygame.Color(255 ,255 ,255) #Background
brown = pygame.Color(165 , 42 , 42) #Food


#FPS Controlling
fbsController = pygame.time.Clock()

#Important Variables
snakePos = [100,50] # Snake Position (Where he will start)
snakeBody = [[100,50] ,[90,50] ,[80,50]] #Snake Body(the dimenstions of the body)

#food position
foodPos = [random.randrange(1,72)*10 ,
           random.randrange(1,46)*10]
foodSpawn = True

#Directions

direction = 'RIGHT'
changeto = direction


score = 0


#GameOver Functions

def gameOver():
    myFont = pygame.font.SysFont('monaco' , 72)
    gameOverSurf = myFont.render('Game Over!' , True , red)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (360 , 15)
    playSurface.blit(gameOverSurf , gameOverRect)
    pygame.display.flip()
    showScore(0)
    time.sleep(4)
    pygame.quit() #Exit
    sys.exit() #console


def showScore(choice = 1):
    sFont = pygame.font.SysFont('monaco', 24)
    scoreSurf = sFont.render('Score : {0}' .format(score), True, black)
    scoreRect = scoreSurf.get_rect()
    if choice == 1:
        scoreRect.midtop = (80 ,10)
    else:
        scoreRect.midtop = (360, 120)

    playSurface.blit(scoreSurf, scoreRect)
    pygame.display.flip()



#Main Logic of the Game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_RIGHT or event.type == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.type == ord('a'):
                changeto = 'LEFT'
            if event.key ==  pygame.K_UP or event.type == ord('w'):
                changeto = 'UP'
            if event.key ==  pygame.K_DOWN or event.type == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))



    #Validation of directions
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #Body Mechanism
    snakeBody.insert(0 , list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score +=1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1,72)* 10 , random.randrange(1,46) * 10]
    foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playSurface , green ,
        pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(playSurface, brown,
        pygame.Rect(foodPos[0], foodPos[1], 10, 10))


        #Bound
        if snakePos[0] > 710 or snakePos[0] < 0:
            gameOver()
        if snakePos[1] > 450 or snakePos[1] < 0:
            gameOver()


        # for snake hitting itself
        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                gameOver()


    #Calling the functions
    pygame.display.flip()
    showScore()
    fbsController.tick(50)

#implement Menu
#adding sounds and background sound
#adding settings
#adding game to the head of the sank
#Changing the icon of the game
#pyinstaller
