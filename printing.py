import reports as r

# główne pytanie o nazwe pliku
def menu():
    print("\nWelcome to Game statistics app.")
    ask_for_file_name = input('Please provide the name of a data file(game_stat.txt):  ')
    
    #wywolanie funkcji nr 1 z reports
    number_of_games = r.count_games(ask_for_file_name)
    print("\nHow many games are in the file?")
    print(f"There are {number_of_games} games in the file.")  

    #wywołanie funkcji nr 2 z reports
    year_input = input('\nIs there a game from a given year? Please provide a year: ')
    game_from_inputed_year = r.decide(ask_for_file_name, year_input)
    #Czy ten warunek moze być w princie
    if game_from_inputed_year:
        print(f"There is a game from {year_input}.")
    else:
        print(f"There is not any game produced in {year_input}.")   

    # wywolanie funkcji nr 3
    print("\nWhich is the latest game?")
    latest_game = r.get_latest(ask_for_file_name)
    print(f"The latest game is {latest_game}.")


    # wywolanie funkcji nr 4 dodac wyswietlenie dostepnych gatunkow
    print("\nHow many games are in the file by genre?")
    ask_for_genre = input('Please provide a genre: ')
    genre_count = r.count_by_genre(ask_for_file_name, ask_for_genre)
    print(f"There are {genre_count} {ask_for_genre} games.")

    # wywołanie funkcji nr 5 dodać handle exception
    print("\nWhat is the line number of a given title?")
    ask_for_a_title = input('Please provide a title: ')
    title_line_number = r.get_line_number_by_title(ask_for_file_name, ask_for_a_title)
    if title_line_number:
        print(f"The line number of a given title is {title_line_number}")
    else:
        print("Provided game is not in the file.")

    #wywołanie funkcji nr 6 z reports
    print("\nCan you give me the alphabetically ordered list of the titles?")
    sorted_titles_list = r.sort_abc(ask_for_file_name)
    print(f"Here you are: {sorted_titles_list}.")

    #wywołanie funkcji nr 7 z reports
    print("\nWhich genres occur in the data file?")
    genres = (r.get_genres(ask_for_file_name))
    print(f"In data file we have the following genres: {genres}. ")
    
    #wywolanie funkcji nr 8
    print("\nWhat is the release year of the top selling first-person shooter game?")
    top_selling_fps_realease_year = r.when_was_top_sold_fps(ask_for_file_name)
    print(f"Top selling fps game was released in {top_selling_fps_realease_year}.")
# # Printing functions


if __name__ == "__main__":
    menu()