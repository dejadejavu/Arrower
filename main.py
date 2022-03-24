#General setup
import pygame
pygame.init()
#Player setup
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
itemsList = ["basic sword", "basic chestplate"]
inventory = []
#Asset loading & scaling
playerImg = pygame.image.load("archer.png")
playerImg= pygame.transform.smoothscale(playerImg, (100, 100))

class Player:
    def __init__(self, character="swordsman", coins=0,HP=100, mainXP=0, ingameXP=0, attackStrength=1, projectileType=1):
        self.coins = coins #primary currency
        self.character = character #multiple different ones with unique buffs
        self.HP = HP #health points
        self.ingameXP = ingameXP #experience points
        self.attackStrength = attackStrength #how much damage an attack does
        self.projectileType = projectileType #projectile types vary in speed and path
    def changeCharacter(self, difCharacter):
        self.character = difCharacter
    def changeCoins(self, amount):
        self.coins += amount
    def gainMainXP(self, amount):
        self.mainXP += amount
    def gainIngameXP(self, amount):
        self.ingameXP += amount
    def changeAttackStrength(self, amount):
        self.attackStrength += amount
    def changeProjectileType(self, newType):
        self.ProjectileType = newType

class Monster:
    def __init__(self, monsterType=1, monsterHP=1, monsterAttack=0, projectileType=1):
        self.monsterType = monsterType #various ones with variable attack speeds
        self.monsterHP = monsterHP
        self.monsterAttack = monsterAttack
        self.projectileType = projectileType
    def changeAttack(self, amount):
        self.monsterAttack += amount
    def changeProjectileType(self, newType):
        self.projectileType = newType
    def changeHP(self, amount):
        self.monsterHP += amount

def Shop():
    print("Welcome to the shop!")
    print(f"You have {playerObj.coins} coins.")
    print("The items available in the shop today are:")
    if len(itemsList) < 2:
         print(f"A {itemsList[0]}.")
    else:
        print(f"A {itemsList[0]} and a {itemsList[1]}.")
    userInput = input("Type the name of what you want to buy. If you don't want to buy anything, type 'exit'. ")
    if userInput.lower() in itemsList:
        itemBought = userInput
        if playerObj.coins > 99:
            playerObj.changeCoins(100)
            print(f"You bought a {itemBought}!")
            inventory.append(itemBought)
        else:
            print("You don't have enough coins!")
    elif userInput.lower == "'exit'" or "exit":
        print("Thank you, come again soon!")

def Character():
    print("You're currently playing as a swordsman.")
    for i in range(0, len(inventory)):             
        print(f"You're wearing {inventory[i]}")
        i + 1

def player(x,y):
    screen.blit(playerImg, (x, y))
                        

        
running = True
while running:
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Arrower")
    icon = pygame.image.load("bow-and-arrow.png")
    pygame.display.set_icon(icon)
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                print(f"X: {playerX} Y: {playerY}")
                
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                print(f"X: {playerX} Y: {playerY}")

            if event.key == pygame.K_DOWN:
                playerY_change = 5
                print(f"X: {playerX} Y: {playerY}")

            if event.key == pygame.K_UP:
                playerY_change = -5
                print(f"X: {playerX} Y: {playerY}")

            if event.key == pygame.K_r: #kill command
                running = False
                
                if playerX > 700:
                    playerX = 700
                    playerX -= 5
                    
                elif playerX < 0:
                    playerX = 0
                    playerX -= 5

                #elif playerY > 390:
                    #playerY = 390
                    #playerY -= 5

                #if playerY < 100:
                    #playerY = 100
                    #playerY -= 5

            if event.type == pygame.KEYUP:
                if event.type == pygame.K_UP or event.type == pygame.K_DOWN:
                    playerY_change = 0

                if event.type == pygame.K_LEFT or event.type == pygame. K_RIGHT:
                    playerX_change = 0

    ##         if event.type == pygame.KEYUP:           
    ##            if event.type == pygame.K_UP or event.type == pygame.K_DOWN or event.type == pygame.K_LEFT or event.type == pygame. K_RIGHT:
    ##                playerY_change = 0
    ##                playerX_change = 0
                    
                
        playerX += playerX_change
        playerY += playerY_change
        player(playerX, playerY)
        pygame.display.update()

        #playerObj = Player(0, 0, 0, 1, 1)
        #playerObj.changeCoins(100)

##    goTo = input("Shop, Character, Runes, PvP, or Play? ")
##    if goTo == "shop": 
##        Shop()
##    elif goTo == "character":
##        print("This feature is still being worked on, check back later!")
##    elif goTo == "runes":
##        print("This feature is still being worked on, check back later!")
##    elif goTo == "pvp":
##        print("This feature is still being worked on, check back later!")
##    elif goTo == "play":
##        print("This feature is still being worked on, check back later!")

    ##Game loop - maybe use a class?##

    ##print("Starting game...")
    ##time.sleep(0.5)
    ##if monsterObj1.monsterType == 1:
    ##    print("A zombie appeared!")
    ##    print(f"You attack the zombie with your sword! It does {str(playerObj.attackStrength)} damage!")
    ##    monsterObj1.changeHP(-1)
    ##    print(monsterObj1.monsterHP)
    ##    if monsterObj1.monsterHP <= 0:
    ##        print("You killed the zombie!")

pygame.quit()
