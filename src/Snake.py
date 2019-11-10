import pygame
from random import *
pygame.init()

dimWidth = 70
dimHeight = 40
width = 15

yOffset = 3 * width
xMargin = 30

score = 0
highscore = 0
deaths = 0

window = pygame.display.set_mode((dimWidth * width + width + 2 * xMargin, dimHeight * width + 3 * width + yOffset)) #Dimensions of window
pygame.display.set_caption("Snake")

x = [20, 19, 18]
y = [20, 20, 20]

direction = 3

appleX = randint(1, dimWidth - 1)
appleY = randint(1, dimHeight - 1)
    
run = True
alive = True
printed = False

borderX = [0]
borderY = [0]
for i in range(1, dimWidth + 1):
    borderX.append(i)
    borderY.append(0)
    borderX.append(i)
    borderY.append(dimHeight)
for i in range(1, dimHeight + 1):
    borderX.append(0)
    borderY.append(i)
    borderX.append(dimWidth)
    borderY.append(i)

def isAlive():
    if x[0] == 0 or x[0] == dimWidth or y[0] == 0 or y[0] == dimHeight:
        return False
    for i in range(1, len(x)):
        if x[0] == x[i] and y[0] == y[i]:
            return False
    return True
    
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

while run:
    pygame.time.delay(80)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if not alive:
        x = [20, 19, 18]
        y = [20, 20, 20]
        direction = 3
        appleX = randint(1, dimWidth - 1)
        appleY = randint(1, dimHeight - 1)
        
        if highscore < score:
            highscore = score
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            alive = True
            score = 0
    else:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and direction != 3:
            direction = 1
        if keys[pygame.K_RIGHT] and direction != 1:
            direction = 3
        if keys[pygame.K_UP] and direction != 4:
            direction = 2
        if keys[pygame.K_DOWN] and direction != 2:
            direction = 4
            
        i = len(x) - 1
        while i > 0:
            x[i] = x[i-1]
            y[i] = y[i-1]
            i = i - 1
        
            
        if direction == 1:
            x[0] = x[0] - 1
        if direction == 2:
            y[0] = y[0] - 1
        if direction == 3:
            x[0] = x[0] + 1
        if direction == 4:
            y[0] = y[0] + 1
        
        
        if x[0] == appleX and y[0] == appleY:
            x.append(x[len(x) - 1])
            y.append(y[len(y) - 1])
            appleX = randint(1, dimWidth - 1)
            appleY = randint(1, dimHeight - 1)
            score += 1
        
        alive = isAlive()
        if not alive:
            deaths += 1
            
        
        window.fill((255,255,255))
        for i in range(len(x)): 
            pygame.draw.rect(window, (0, 0, 200), (width * x[i] + xMargin, width * y[i] + yOffset, width, width))
        
        for i in range(len(borderX)):
            pygame.draw.rect(window, (0,0,0), (width * borderX[i] + xMargin, width * borderY[i] + yOffset, width, width))
        
        pygame.draw.rect(window, (200,0,0), (width * appleX + xMargin, width * appleY + yOffset, width, width))
        
        text = "Deaths: " + str(deaths) + "    High Score: " + str(highscore) + "   Score: " + str(score)   
        font = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects(text, font)
        TextRect.center = ((width * dimWidth/2), width * 2)
        window.blit(TextSurf, TextRect)
        
        pygame.display.update()
        
pygame.quit()