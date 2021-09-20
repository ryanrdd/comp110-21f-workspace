"""Choose Your Own Adventure: Mack Brown Smackdown"""

__author__ = "730314539"

from random import randint

game_name: str = ""
player: str = ""
points: int = 10
opp_team: int = 0

"""Game Mechanics Percentages"""
run = int(100)
short = int(80)
long = int(60)
hail = int(30)


def greet() -> None:
    """Introduction to the game"""
    print("Welcome to Mack Brown Smackdown Football! ")
    print("You are now hired as UNC’s offensive coordinator, calling the plays and leading the Tar Heels to victory! ")
    print("Your objective is to score the winning touchdown without losing possession of the ball. ")
    name: str = input("What is your name? ")
    global player
    player = name
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
    global opp_team
    global game_name
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
    global opp_team
    global player
    global points
    global run
    global short
    global long
    global hail
    opp_name: str = ""
    downs = 0
    if opp_team == 1:
        opp_name = "Georgia State"
    elif opp_team == 2:
        opp_name = "Duke"
        run = run - 10
        short = short - 10
        long = long - 5
        hail = hail - 5
    elif opp_team == 3:
        opp_name = "Alabama"
        run = run - 20
        short = short - 15
        long = long - 10
        hail = hail - 20
    print(f"It's show time, time to show what you're made of { player }. ")
    print(f"We're playing { opp_name }, so play strong. ")
    print(f"UNC is starting { points } yards away from the endzone! ")
    while points > 0:
        play: str = input("What play do you want to run coach? (run, short, long, hail) ")
        c: int = randint(0,100)
        if play == "run":
            if c <= run:
                points = points - 2
                print("Caleb hood runs it for 2 yards! ")
            if c > run:
                print("The defense got us this time. Run another play. ")
            if downs < 4:
                downs = downs + 1
                if downs == 4:
                    print("You lose! ")
                    quit()
            else:
                print("You lose! ")
                quit()
        elif play == "short":
            if c <= short:
                points = points - 4
                print("Sam Howell throws for 4 yards! ")
            if c > short:
                print("The defense got us this time. Run another play. ")
            if downs < 4:
                downs = downs + 1
                if downs == 4:
                    print("You lose! ")
                    quit()
            else:
                print("You lose! ")
                quit()
        elif play == "long":
            if c <= long:
                points = points - 6
                print("Caught by Jeffrey Saturday! ")
            if c > long:
                print("The defense got us this time. Run another play. ")
            if downs < 4:
                downs = downs + 1
                if downs == 4:
                    print("You lose! ")
                    quit()
            else:
                print("You lose! ")
                quit()
        elif play == "hail":
            if c <= hail:
                points = points - 10
                print("SAM HOWELL GOES LONG AND SCORES!!! ")
            if c > hail:
                print("The defense got us this time. Run another play. ")
            if downs < 4:
                downs = downs + 1
                if downs == 4:
                    print("You lose! ")
                    quit()
            else:
                print("You lose! ")
                quit()
        else:
            print("invalid input ")
        if points > 0:
            print(f"We're now { points } yards from the endzone" )
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