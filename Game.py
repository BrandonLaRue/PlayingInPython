from random import randrange;

world = {};
worldWidth = 64;
worldHeight = 32;
spawnPoint = (0, worldHeight);
selected = (0, 0);
charPos = spawnPoint;

def genWorld(world, worldWidth, worldHeight):  
    '''
    world: dictionary that will be defined [(x, y), 'stringValue']
    worldLength: an int that decides the width and height of the world
    '''        
    world = {};
    for x in range(worldWidth):
        for y in range(worldHeight):
            world[(x,y)] = 's';
            if(worldHeight / 2 < y < worldHeight):
                if(chance(3, 5)):
                    world[(x, y)] = ' ';
                else: world[(x, y)] = 's';
    return world;
        
def assembleWorldStringList(world):
    '''
    takes in the world dictionary and returns a list of layers
    '''
    worldStringList = [];
    for y in range(worldHeight):
        worldStringList.append('');
    
    
    for y in range(worldHeight - 1, -1, -1):
        for x in range(worldWidth):
            worldStringList[y] += world[(x,y)];
    return worldStringList;

def drawWorldFromStringList(worldStringList):
    for layer in range(worldHeight - 1 , -1, -1):
        print(worldStringList[layer]);
        
def drawWorld(world):
    drawWorldFromStringList(assembleWorldStringList(world));

def changeBlock(world, pos, to):
    '''
    world: the world dict
    pos: a valid tuple within the range of the world length and width
    to: a character that the block will be changed into
    '''
    #should implement checks for length and type
    
    world[pos] = to;
    return world;
    
def chance(x, y):
    '''
    x: int positive or zer / numerator of chance
    y: int positive / denominator of change
    for x = 3 and y = 5, chance will return true 3 / 5 of the time
    '''
    if (randrange(0, y) in range(0, x)):
        return True;
    else:
        return False;
    
def spawnChar(world):
    return changeBlock(world, spawnPoint, 'M');
    
def testAir(world, coordinate):
    if(world[coordinate] == ' '):
        return True;
    
def moveChar(world, direction):
    global charPos;
    if(direction == 'w'):
        if (testAir(world, (charPos[0], charPos[1] + 1))):
            charPos = (charPos[0], charPos[1] + 1);
            return changeBlock(world, (charPos[0], charPos[1] + 1, 'M'));
        else:
            return world;
    elif(direction == 'a'):
        if (testAir(world, (charPos[0] -1, charPos[1]))):
            charPos = (charPos[0] -1, charPos[1]);
            return changeBlock(world, (charPos[0] -1, charPos[1], 'M'));
        else:
            return world;
    elif(direction == 's'):
        if (testAir(world, (charPos[0], charPos[1] - 1))):
            charPos = (charPos[0], charPos[1] - 1);
            return changeBlock(world, (charPos[0], charPos[1] - 1, 'M'));
        else:
            return world;
    elif(direction == 'd'):
        if (testAir(world, (charPos[0] +1, charPos[1]))):
            charPos = (charPos[0] +1, charPos[1]);
            return changeBlock(world, (charPos[0] + 1, charPos[1], 'M'));
        else:
            return world;
    else: 
        return world;
    
world = genWorld(world, worldWidth, worldHeight);
drawWorld(world);
world = spawnChar(world);
drawWorld(world);

direction = raw_input();
world = moveChar(world, direction);
drawWorld(world);
        
