import random, time

item_cards = []
player_cards = []

##### INITIALIZATION (card setup)
trogdor = { 'name': 'Trogdor',
            'type': 'player',
            'meta': { 'hp': 50,
                      'attack': -(random.randrange(5,10)) }
          }
                
dog = {'name': 'Dog',
       'type': 'player',
       'meta': {
              'hp': 25,
              'attack': -(3*random.randrange(3)) }
      }

tazer = {'name': 'tazer',
         'type': 'item',
         'meta': { 'multiplier': '-20',
                   'operand':'plus',
                   'attr':'hp',
                   'target':'player'}  # Items usually involve multipliers, and attributes,
        }
             # so above lets define the number we want to use (multiplier),
             # the operand (+-/*), and the affected hp (oh, and probably a target?)

staff = {'name': 'staff',
         'type': 'item',
         'meta': { 'multiplier': '-10',
                   'operand': 'plus',
                   'attr': 'hp',
                   'target': 'player' }
        }

# Fill our decks

item_cards.append(staff)
item_cards.append(tazer)
player_cards.append(dog)
player_cards.append(trogdor)



##### CLASSES

class Player():
    def __init__(self,name,health):
      self.name = name
      self.hp = health
      self.cards = []
    
"""
Matt = Player("Matt",100)
  Matt.name -> "Matt"
  Matt.hp -> 100


Matt.hp = 100

Matt.hp - 40
60

Matt.hp = 100

Matt.hp -= 50

Matt.hp = 50


Name, HP
__init__(self, name, health)

(self) - The object itself

self.hp == Matt.hp 
"""
    
class Card():
    def __init__(self,name,type,meta):
        self.name = name
        self.type = type
        self.meta = meta
        
##### FUNCTIONS

def deal(player,player_cards,item_cards):
    # Let's take our cards, and draw them out to two players.
    # Let's create a die
    player_die = random.randrange(len(player_cards))
    item_die = random.randrange(len(item_cards))

    player.cards.append(player_cards.pop(player_die)) # This is our player object defined on 102, we're appending to self.cards
    print("Dealing to player: %s" % player.name)
    player.cards.append(item_cards.pop(item_die))
    
def turn(player,opponent):
    card_at_play = player.cards.pop(0)
    print("%s draws %s\n\n" % (player.name,card_at_play['name']))
    if card_at_play['type'] == "item":
      print("%s hit for %s damage" % (opponent.name, card_at_play['meta']['multiplier']))
      # item card play
      opponent.hp += int(card_at_play['meta']['multiplier'])
    elif card_at_play['type'] == "player":
      print("%s hit for %s damage" % (opponent.name, card_at_play['meta']['attack']))
      # player card play
      opponent.hp += int(card_at_play['meta']['attack'])

    print("%s: %s\n%s: %s\n\n" % (player.name,player.hp,opponent.name,opponent.hp))


# Assume there are 2 players
def game():
    # init players
    player1 = Player('FireFox40',random.randrange(50,60))
    player2 = Player('ChromeCast1milli-on',random.randrange(50,60))
    
    
    # See who goes first
    coin_toss = random.randrange(2)
    
    if coin_toss == 1:
        deal(player1,player_cards,item_cards) # this is calling def deal(player) line 115
        deal(player2,player_cards,item_cards)
        #print("Player %s hand: %s" % (player1.name,player1.cards))
    else:
        deal(player2,player_cards,item_cards)
        deal(player1,player_cards,item_cards) # this is calling def deal(player) line 115
        #print("Player %s hand: %s" % (player2.name,player2.cards))

    #Game Loop
    while player1.hp > 0 and player2.hp > 0:
      if len(player1.cards) == 0 or len(player2.cards) == 0:
        item_cards.append(staff)
        item_cards.append(tazer)
        player_cards.append(dog)
        player_cards.append(trogdor)


        if coin_toss == 1:
          deal(player1,player_cards,item_cards) # this is calling def deal(player) line 115
          deal(player2,player_cards,item_cards)
          #print("Player %s hand: %s" % (player1.name,player1.cards))
        else:
          deal(player2,player_cards,item_cards)
          deal(player1,player_cards,item_cards) # this is calling def deal(player) line 115

        
      if coin_toss == 0:
        #checking first player's health
        #health has to > 0
        #if > 0 take turn
        if player1.hp > 0:
          
          turn(player1,player2) # Our definition assumes 
          time.sleep(2)
        #checking second player's health
        if player2.hp > 0:

          turn(player2,player1)
          time.sleep(2)
      else:
        if player2.hp > 0:
          turn(player2,player1)
          time.sleep(2)
        if player1.hp > 0:
          turn(player1,player2) # Our definition assumes 
          time.sleep(2)
      
    if player1.hp >= 1:
      print("%s wins!" % player1.name)
    else:
      print("%s wins!" % player2.name)



if __name__ == "__main__":
  game()
