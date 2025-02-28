import random
from soccer_game_utils import get_strPlayerName, display_intMenu, choose_strTeam, play_strGame, display_finalRecord

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
