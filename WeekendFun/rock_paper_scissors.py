#rock paper scissors game 
#
#ask first player to enter rock, paper scissors
#
#ask second player to enter rock, paper scissors
#
#if player one wins
#
#display player one wins
#
#if player two wins
#
#display player two wins
#
#if its a tie
#
#display tie
#
#game rules
#
#rock beats scisscors
#
#paper beats rock
#
#scissors beat paper


player_one = input('Enter (rock,paper,scissors): ')

player_two = input('Enter (rock,paper,scissors): ')

if player_one.lower() == 'rock' and player_two.lower() == 'scissors':

    print('player 1 wins - rock beats scissors')

elif player_one.lower() == 'paper' and player_two.lower() == 'rock':

    print('player 1 wins - paper beats rock')

elif player_one.lower() == 'scissors' and player_two.lower() == 'paper':

    print('player 1 wins - scissors beats paper')

elif player_two.lower() == 'rock' and player_one.lower() == 'scissors':

    print('player 2 wins - rock beats scissors')

elif player_two.lower() == 'paper' and player_one.lower() == 'rock':

    print('player 2 wins - paper beats rock')

elif player_two.lower() == 'scissors' and player_one.lower() == 'paper':

    print('player 2 wins - scissors beats paper')

elif player_one.lower() == 'rock' and player_two.lower() == 'rock':
    
    print('Tie')
else:
    print('Tie')
    

