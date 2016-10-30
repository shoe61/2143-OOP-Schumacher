"""
@ Scott Schumacher
@ game_part1.py

This is part two of the Pig Game project. Now, different strategies are available:
in addition to Random, there are Aggressive and Cautious. Bob is Aggressive; Ann
is Cautious; and Sue and Dax use the Random strategy. Any player that reaches
eighty percent of the target score switches to the Sprint to Finish strategy, 
in which he or she rolls until reaching target or losing turn.

Random: roll some number of times between 1 and 7
Cautious: roll some number of times between 1 and 3
Aggressive: roll some number of times between 1 and 10
Sprint to Finish: roll until target score or crash and burn.

Under this regime, with a sample size of 50 games,
Bob (aggressive) won 25
Sue (random) won 14
Dax (random) won 11
Ann (cautous) won 0

"""

############################################################################

import random
import abc

"""
@Class: Dice
@Description: 
    Represents a single "die" with X number of sides.
@Methods:
    Roll - Rolls the dice and returns a value between 1 and "number of sides" 
"""
class Dice(object):
    def __init__(self,num_sides=6):
        self.NumSides = num_sides

    def Roll(self):
        return random.randint(1,self.NumSides)  

##############################################################################
##############################################################################

"""
@Class: Pig
@Description: 
    Represents the game of pig (dice game)
@Methods:
    Roll - Rolls the "die" or "dice" and returns a list of rolled values
"""
class Pig(object):
    def __init__(self,num_dice=1,dice_sides=6,skunk_value=1):
        self.NumDice = num_dice
        self.DiceSides = dice_sides
        self.DiceList = []
        self.SkunkValue = skunk_value
        for i in range(self.NumDice):
            self.DiceList.append(Dice(self.DiceSides))
    """
    @Method: Roll
    @Description: 
        One roll in a pig game, with 1 to NumDice per roll
    @Returns: int: [0=skunk value occured, total of all dice otherwise]
    """ 
    def Roll(self):
        scores = []
        for d in self.DiceList:
            scores.append(d.Roll())
            if self.SkunkValue in scores:
                return 0 
        return sum(scores)

##############################################################################
##############################################################################

class Player(object):
    def __init__(self,name,winning_score,num_dice=1,strategy=('Random',7)):
        self.Name = name        # My name
        self.TotalScore = 0     # Total score
        self.LastScore = 0      # Score on last turn
        self.LastNumRolls = 0   # Last number of rolls
        self.Opponents = {}     # Dict of opponents
        self.NumDice = num_dice
        self.Strategy = strategy[0]
        self.pig = Pig(num_dice)# init pig game 
        self.winning_score = winning_score
        self.Strategies = {
                'Random':7,
                'Aggressive':10,
                'Cautious':3,
                'Robust':0,
                'Copycat':0,
                'SprintToFinish':12
            }
        #self.Strategies[strategy[0]] = strategy[1]

   



    """
    @Method: AddOpponents
    @Description: Adds an opponent, or list of opponents (as long as it's not me) to a dictionary with name and score.
        Example: {
                   'bob':0.
                   'sue':0
                 }
    
    @Params: [] - Opponents
    @Returns: None
    """
    def AddOpponents(self,opponent):
        """if not type(opponent) == list and not opponent.Name == self.Name:
            self.Opponents[opponent.Name] = opponent
        else:"""
        for op in opponent:
            if not op.Name == self.Name:
                self.Opponents[op.Name] = op

    """
    @Method: __str__
    @Description: Prints out a nice version of self
    @Returns: string representation
    """
    def __str__(self):
        tmp = " "
        for k,v in self.Opponents.items():
            tmp = tmp + "[" + k + " "  + str(v.TotalScore) + "," + str(v.LastScore) + "," + str(v.LastNumRolls) + "] "
        return "Name: %s, TotScore: %s, LastScore: %s, LastNumRolls: %s, Opponents: %s" % (self.Name,self.TotalScore,self.LastScore,self.LastNumRolls,tmp)
        
    """
    @Method: __repr__
    @Description: Calls __str__
    @Returns: a call to __str__
    """
    def __repr__(self):
        return self.__str__()
        

    """
    @Method: SetStrategy
    @Description: Sets the current strategy for the player
    @Params:
        strategy: string 
        value: int    
    @Returns: None
    @Usage:
            SetStrategy('Target_Score',20)
            SetStrategy('Target_Rolls',5)     
            SetStrategy('Sprint_To_Finish',72)    
    """
    def SetStrategy(self,strategy,value):
        if strategy in self.Strategies:
            self.Strategy = strategy            
        else:
            raise ValueError('The strategy does not exist!')

    """
    @Method: PlayerRoll
    @Description: Implements a turn for a player. If the player rolls a 1 at any time zero is returned, 
                  otherwise the total of the rolls is returned.
    @Params:
        string: player
        int: max rolls 
    @Returns: int: total
    """
    def Roll(self):
        if self.Strategy == 'Random':
            Score,NumRolls = self.RandomRoll()
        elif self.Strategy == 'Aggressive':
            Score,NumRolls = self.Aggressive()
        elif self.Strategy == 'Cautious':
            Score,NumRolls = self.Cautious()
        elif self.Strategy == 'Robust':
            pass
        elif self.Strategy == 'CopyCat':
            pass
        elif self.Strategy == 'SprintToFinish':
            Score,NumRolls = self.SprintToFinish()
        
        self.TotalScore += Score
        self.LastScore = Score
        self.LastNumRolls = NumRolls
        
    
    """
    @Method: RandomRoll
    @Description: Rolls some number of times between 1 and 7; declares victory and stops
    @rolling if reaches target (winning) score.
    @Params: None
    @Returns: int: Score, NumRolls

    """

    def RandomRoll(self):
        Score = 0
        Needed = self.winning_score - self.TotalScore # how do I know when to quit?
        NumRolls = 0
        for i in range(random.randint(1,7)):
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            if Score >= Needed: # if I have made the points I needed to win, I say so and quit rolling
                print(self.Name, 'has just reached ', self.winning_score, ' points and is stopping.')
                return(Score,NumRolls)
                break          
        return (Score,NumRolls)
    
    """
    @Method: Aggressive
    @Description: Rolls some number of times between 1 and 10; declares victory and stops
    @rolling if reaches target (winning) score.
    @Params: None
    @Returns: int: Score, NumRolls
    
    """
    
    def Aggressive(self):
        Score = 0
        Needed = self.winning_score - self.TotalScore # how do I know when to quit?
        NumRolls = 0
        for i in range(random.randint(1,10)):
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            if Score >= Needed: # if I have made the points I needed to win, I say so and quit rolling
                print(self.Name, 'has just reached ', self.winning_score, ' points and is stopping.')
                return(Score,NumRolls)
                break          
        return (Score,NumRolls)
         
    """
    @Method: Cautious
    @Description: Rolls some number of times between 1 and 3; declares victory and stops
    @rolling if reaches target (winning) score.
    @Params: None
    @Returns: int: Score, NumRolls
    
    """
   
    def Cautious(self):
        Score = 0
        Needed = self.winning_score - self.TotalScore # how do I know when to quit?
        NumRolls = 0
        for i in range(random.randint(1,3)):
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            if Score >= Needed: # if I have made the points I needed to win, I say so and quit rolling
                print(self.Name, 'has just reached ', self.winning_score, ' points and is stopping.')
                return(Score,NumRolls)
                break          
        return (Score,NumRolls)

    def Robust(self):
        pass
        
    def Copycat(self):
        pass
    
    """
    @Method: SprintToFinish
    @Description: Rolls until target score reached or rolls a 1.
    @Params: None
    @Returns: int: Score, NumRolls
    
    """

    def SprintToFinish(self):
        Score = 0
        Needed = self.winning_score - self.TotalScore # how do I know when to quit?
        NumRolls = 0
        while self.TotalScore < self.winning_score: # roll until you win...
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            if Score >= Needed: # if I have made the points I needed to win, I say so and quit rolling
                print(self.Name, 'has just reached ', self.winning_score, ' points and is stopping.')
                return(Score,NumRolls)
                break          
        return (Score,NumRolls)
        
   


##############################################################################
##############################################################################

"""
This Class represents one instance of a game with X players rolling X dice playing to a score of X.
"""
class Game(object):
    """
    @Method: Init
    @Description: Initializes a pig game instance
    @Params:
        list: Players - A list of player names
        int: NumDice - Number of dice per roll
        int: RandomRolls - Top value of random range for rolls
        int: TargetScore - Target score to trigger a winner
    @Returns: None
    """
    def __init__(self, **kwargs):
        self.Players = {}                           # player dictionary
        self.NumDice = kwargs['num_dice']           # number of dice per roll
        self.RandomRolls = kwargs['random_roles']   # max num random rolls
        self.TargetScore = kwargs['target_score']   # game winning score
        self.WinnerName = None                      # no winner yet
        
        # initialize all players
        self.AddPlayers(kwargs['players'])
            
        self.StartGame()
        
    def __str__(self):
        string = ""
        for name,obj in self.Players.items():
            string += obj.__str__() + "\n"
        return string
        
    """
    @Method: AddPlayers
    @Description: Adds a new player or players to the game
        Example: {
                   'bob':<player_object>
                   'sue':<player_object>
                 }
    
    @Params: [] - players
    @Returns: None
    """
    def AddPlayers(self,players):
        if not type(players) == list:
            self.Players[players.Name] = players
        else:
            for p in players:
                self.Players[p.Name] = p
                    
    """
    @Method: StartGame
    @Description: Loops through the list of players, calling each to roll. If, at the beginning
    @of the turn, the player has 80% percent or more of the winning score, changes player's 
    @strategy to Sprint to Finish.
    @Params:None
    @Returns: None
    """         
    def StartGame(self):

        self.UpdatePlayerOpponents()
        
        # Main game loop
        while not self.WinnerExists():
            print(self)
            for name,PlayerObj in self.Players.items():
                # If player is within 20% of winning, switch to SprintToFinish
                if PlayerObj.TotalScore >=  self.TargetScore * .80:
                    PlayerObj.SetStrategy('SprintToFinish', 12)
                    # all the spectators cheer for the big push for victory...
                    print(PlayerObj.Name,', go for it using the ', PlayerObj.Strategy, 'strategy!')
                    
                PlayerObj.Roll()
       
    """
    @Method: WinnerExists
    @Description: Checks to see if a player has acheived the target score.
    @Params:None
    @Returns: bool
    """
    def WinnerExists(self):
        for name,PlayerObj in self.Players.items():
            if PlayerObj.TotalScore >= self.TargetScore:
                self.WinnerName = PlayerObj.Name
                print (self.WinnerName, 'is the winner.')
                return True
        self.WinnerName = None
        return False

        

    """
    @Method: Winner
    @Description: Returns the winner, if there is one.
    @Params:None
    @Returns: [string,None]: Players name or None
    """
    def Winner(self):
        return self.WinnerName
        
    """
    @Method: UpdatePlayerOpponents
    @Description: Gives a copy of each player in the game, to every other player in the game. 
    @Params:None
    @Returns: None
    """   
    def UpdatePlayerOpponents(self):

        for name,PlayerObj in self.Players.items():
            PlayerObj.AddOpponents(self.Players.values())

##############################################################################
##############################################################################



def main():
    """
    I added this variable, winning_score, so game object and player objects could share the same target.
    It is passed to Player as an additional argument and to Game as a value in kwargs. Because AllPlayers
    is a list of the Players and is included in kwargs, it was not otherwise possible.
    """
    winning_score = 100

    """
    Players are assigned different strategies; regardless of the strategy assigned,
    all players switch to Sprint to Finish upon reaching eighty percent of goal.
    
    """
    
    p1 = Player('ann' , winning_score, 1, ('Cautious',3) )
    p2 = Player('bob' , winning_score, 1, ('Aggressive', 9))
    p3 = Player('sue' , winning_score)
    p4 = Player('dax' , winning_score)
    
    AllPlayers = [p1,p2,p3,p4]
    
    # Param values to initialize a pig game instance
    kwargs = {'num_dice':1,'random_roles':9,'target_score':winning_score,'players':AllPlayers}

    g = Game(**kwargs)

    print(g)

    
main()
