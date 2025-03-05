# Go Big or Go Small - Dice Game

## Overview
Go Big or Go Small is a two-player dice game where players take turns rolling two dice and choosing whether to keep the larger or smaller value to accumulate points. The goal is to score as high as possible without exceeding 15 points in a round.

## How to Play
1. The game starts with Player 1 rolling two dice.
2. The player chooses to keep either the **larger** ("l") or **smaller** ("s") value of the two dice.
3. The chosen value is added to their score.
4. The player can **roll again** ("y") or stop ("n").
5. If the total score exceeds 15, the player's score resets to 0 for the round.
6. Player 2 then takes their turn, following the same process.
7. The game displays the updated scores for both players.

## Rules
- Each player must decide whether to keep the larger or smaller die value **before rolling**.
- Players can continue rolling as long as their score is **15 or less**.
- If a player's score **exceeds 15**, it resets to **0** for the round.
- The game does not determine an overall winner, but players can track scores over multiple rounds.

## Running the Game
To play the game, run the Python script:
```sh
python game.py
```
You can also provide a random seed for consistent rolls:
```sh
python game.py <seed>
```
where `<seed>` is an integer.

## Example Gameplay
```
Welcome to Go Big or Go Small
++++++++++BEGIN ROUND++++++++++
Player 1's turn
Do you want to use the smaller or larger of the dice (s or l)? l
You roll a 2 and 5
Your score for this roll is 5
Your current total for this round is 5
Do you want to roll again (y or n)? y
You roll a 3 and 6
Your score for this roll is 6
Your current total for this round is 11
Do you want to roll again (y or n)? y
You roll a 4 and 5
Your score for this roll is 5
Your current total for this round is 16
Your turn is over -- you scored 0 points for this round

Player 2's turn...
```

## Dependencies
- Python 3.x

## Author
Cezar Pedroso

