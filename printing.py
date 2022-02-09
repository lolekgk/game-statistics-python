import reports as r


instruction = """\n * At first you need to provide .txt file name.
\n * Then enter a number from 1 to 8 to get the answer for the following questions.
\n1. How many games are in the file?
2. Is there a game from a given year?
3. Which is the latest game?
4. How many games are in the file by genre?
5. What is the line number of a given title?
6. Can you give me the alphabetically ordered list of the titles?
7. Which genres occur in the data file?
8. What is the release year of the top selling first-person shooter game?"""


def menu():
    print("\nWelcome to Game statistics app.")
    instruction_decide = input("To see how to use the app enter 1: ")
    if instruction_decide == '1':
        print(instruction)
    app()


def app():
    ask_for_file_name = input("\nPlease provide the name of a data file:  ")
    while True:
        chose_question = int(input("\nProvide number from 1 to 8 to get the answer or other number to quit: "))
        if chose_question == 1:
            print_number_of_games_in_a_file(ask_for_file_name)
        elif chose_question == 2:
            print_production_year(ask_for_file_name)
        elif chose_question == 3:
            print_latest_game(ask_for_file_name)
        elif chose_question == 4:
            print_games_number_in_genre(ask_for_file_name)
        elif chose_question == 5:
            print_line_number_by_title(ask_for_file_name)
        elif chose_question == 6:
            print_alphabetically_ordered_list_of_titles(ask_for_file_name)
        elif chose_question == 7:
            print_genres(ask_for_file_name)
        elif chose_question == 8:    
            print_top_selling_fps_release_year(ask_for_file_name)
        else:
            break

  
def print_number_of_games_in_a_file(file_name):
    number_of_games = r.count_games(file_name)
    print(f"\nThere are {number_of_games} games in the file.")  


def print_production_year(file_name):
    year_input = input('\nPlease provide a year: ')
    game_from_inputed_year = r.decide(file_name, year_input)
    if game_from_inputed_year:
        print(f"There is a game from {year_input}.")
    else:
        print(f"There is not any game in a file released in {year_input}.")  


def print_latest_game(file_name):
    latest_game = r.get_latest(file_name)
    print(f"The latest game is {latest_game}.")


def print_games_number_in_genre(file_name):
    while True:
        ask_for_genre = input('\nPlease provide a genre: ')
        genre_count = r.count_by_genre(file_name, ask_for_genre)
        if genre_count:
            break
        else:
            print("There's no such genre. Please enter another one!")
            continue
    print(f"There are {genre_count} {ask_for_genre} games.")


def print_line_number_by_title(file_name):
    while True:
        ask_for_a_title = input("\nEnter a title: ")
        try:
            line_number = r.get_line_number_by_title(file_name, ask_for_a_title)
            break
        except ValueError:
            print("There's no such title. Please enter another one!")
            continue
    print(f"The line number of '{ask_for_a_title}': {line_number}.")


def print_alphabetically_ordered_list_of_titles(file_name):
    sorted_titles_list = r.sort_abc(file_name)
    print(f"\nAlphabetically ordered list of titles:\n")
    print(*sorted_titles_list, sep = "\n")


def print_genres(file_name):
    genres = (r.get_genres(file_name))
    print("In data file we have the following genres:\n")
    print(*genres, sep = "\n")


def print_top_selling_fps_release_year(file_name):
    try:
        top_selling_fps_release_year = r.when_was_top_sold_fps(file_name)
        print(f"\nTop selling fps game was released in {top_selling_fps_release_year}.")
    except ValueError:
        print("\nThere is no fps game in the data file.")
    

if __name__ == "__main__":
    menu()