import random

def get_strPlayerName():
    print("Welcome to the Women's Soccer Season Simulator!")
    print("In this game, you'll select a home team, play a season, and track your results.")
    str_name = input("Please enter your name: ")
    print(f"Welcome, {str_name}! Let's get started.")
    return str_name

def display_intMenu():
    print("\nMenu:")
    print("1. Start New Season")
    print("2. Exit")
    int_choice = input("Enter your choice: ")
    return int_choice

def choose_strTeam(lst_availableTeams):
    print("\nAvailable Teams:")
    for int_index, str_team in enumerate(lst_availableTeams, 1):
        print(f"{int_index}. {str_team}")
    
    int_choice = int(input("Select a team by number: ")) - 1
    return lst_availableTeams.pop(int_choice)

def play_strGame(str_homeTeam, str_awayTeam):
    int_homeScore = random.randint(0, 5)
    int_awayScore = random.randint(0, 5)
    
    while int_homeScore == int_awayScore:
        int_homeScore = random.randint(0, 5)
        int_awayScore = random.randint(0, 5)
    
    return str_homeTeam, int_homeScore, str_awayTeam, int_awayScore, "W" if int_homeScore > int_awayScore else "L"

def display_finalRecord(str_teamName, lst_games):
    int_wins = sum(1 for game in lst_games if game[4] == "W")
    int_losses = sum(1 for game in lst_games if game[4] == "L")
    
    print("\nGame Results:")
    for game in lst_games:
        print(f"{game[0]} {game[1]} - {game[2]} {game[3]} ({'Win' if game[4] == 'W' else 'Loss'})")
    
    print(f"\nFinal season record: {str_teamName} {int_wins}-{int_losses}")
    if int_wins / len(lst_games) >= 0.75:
        print("Qualified for the NCAA Women's Soccer Tournament!")
    elif int_wins / len(lst_games) >= 0.50:
        print("You had a good season.")
    else:
        print("Your team needs to practice!")

def main():
    str_playerName = get_strPlayerName()
    bool_continue = True
    
    while bool_continue:
        int_choice = display_intMenu()
        if int_choice == "1":
            lst_availableTeams = ["BYU", "Utah State", "Stanford", "UCLA", "USC", "Oregon", "Washington"]
            str_homeTeam = choose_strTeam(lst_availableTeams)
            int_numGames = int(input(f"How many games will {str_homeTeam} play this season? (1-10): "))
            lst_games = []
            
            for int_game in range(1, int_numGames + 1):
                print(f"\nGame {int_game}:")
                str_awayTeam = choose_strTeam(lst_availableTeams)
                lst_games.append(play_strGame(str_homeTeam, str_awayTeam))
            
            display_finalRecord(str_homeTeam, lst_games)
        elif int_choice == "2":
            print(f"Goodbye, {str_playerName}! Thanks for playing.")
            bool_continue = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
