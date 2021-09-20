"""Choose Your Own Adventure: Mack Brown Smackdown"""

__author__ = "730314539"

from random import randint

game_name: str = ""
player_name: str = ""
points: int = 10
opp_team: int = 0

"""Georgia Game Mechanics"""
georgia_run = int(100)
georgia_short = int(80)
georgia_long = int(60)
georgia_hail = int(30)


def greet() -> None:
    """Introduction to the game"""
    print("Welcome to Mack Brown Smackdown Football! ")
    print("You are now hired as UNC’s offensive coordinator, calling the plays and leading the Tar Heels to victory! ")
    print("Your objective is to score the winning touchdown without losing possession of the ball. ")
    name: str = input("What is your name? ")
    player_name = name
    print(f"Great! Welcome to the team { name }. ")

def tutorial() -> None:
    """instructions to the game"""
    tutorial_signature: int = 1 
    while tutorial_signature == 1:
        instructions: str = input("Would you like to see the instructions to the game? (yes or no) ")
        if instructions == "yes":
            print("THIS IS WHERE THE INSTRUCTIONS WOULD GO")
            tutorial_signature = tutorial_signature - 1
        elif instructions == "no":
            print("Okay! We wish you luck!")
            tutorial_signature = tutorial_signature - 1
        else:
            print("invalid input ")
    move_on: str = input("Press enter to continue ")

def game_selection() -> None:
    """Game selection"""
    game_int: int = 0
    print("It's game  time!")
    print("We have three games to play of varying difficulties. Easy: UNC vs Georgia State, Regular Season. Medium: UNC vs Duke, Conference Finals. Hard: UNC vs Alabama, National Championship. ")
    while game_int == 0:
        game: str = input("Enter easy, medium, or hard to play: ")
        if game == "easy":
            print("UNC vs Georgia State")
            game_name = "UNC vs Georgia State"
            game_int = game_int + 1
            opp_team = 1
        elif game == "medium":
            print("UNC vs Duke")
            game_name = "UNC vs Duke"
            game_int = game_int + 1
            opp_team = 2
        elif game == "hard":
            print("UNC vs Alabama")
            game_name = "UNC vs Alabama"
            game_int = game_int + 1
            opp_team = 3
        else:
            print("invalid input" )
    move_on: str = input("Press enter to continue ")

def gs() -> None:
    """Gameplay time"""
    opp_name = str("")
    points = 10
    downs = 0
    if opp_team == 1:
        opp_name = "Georgia State"
    elif opp_team == 2:
        opp_name = "Duke"
    elif opp_team == 3:
        opp_name = "Alabama"
    print(f"It's show time, time to show what you're made of { player_name }. ")
    print(f"We're playing { opp_name }, so play strong. ")
    print(f"UNC is starting { points } yards away from the endzone! ")
    while points > 0:
        play: str = input("What play do you want to run coach? (run, short, long, hail) ")
        if play == "run":
            if randint(0,100) <= georgia_run:
                points = points - 2
                print("Caleb hood runs it for 2 yards! ")
            if downs < 4:
                downs = downs + 1
            else:
                print("You lose! ")
                quit()
        elif play == "short":
            if randint(0,100) <= georgia_short:
                points = points - 4
                print("Sam Howell throws for 4 yards! ")
            if downs < 4:
                downs = downs + 1
            else:
                print("You lose! ")
                quit()
        elif play == "long":
            if randint(0,100) <= georgia_long:
                points = points - 6
                print("Caught by Jeffrey Saturday! ")
            if downs < 4:
                downs = downs + 1
            else:
                print("You lose! ")
                quit()
        elif play == "hail":
            if randint(0,100) <= georgia_hail:
                points = points - 10
                print("SAM HOWELL GOES LONG AND SCORES!!! ")
            if downs < 4:
                downs = downs + 1
            else:
                print("You lose! ")
                quit()
        else:
            print("invalid input ")
        print(points)
        if points <= 0:
            print("TOUCHDOWN!!! ")
            print("UNC wins! ")
            quit()

def main() -> None:
    """The program's entrypoint."""
    greet()
    tutorial()
    game_selection()
    gs()

if __name__ == "__main__":
    main()