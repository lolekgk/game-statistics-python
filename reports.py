TITLE = 0
SOLD_COPIES = 1
PRODUCTION_YEAR = 2
GENRE = 3
PRODUCENT = 4

# FUNKCJE TWORZACE LISTY + OTWIERAJĄCA PLIK
#########################################################################
# spoko, eliminacja powtorzen
def open_file(file_name):
    f = open(file_name)
    txt_file_lines = f.readlines()
    f.close()
    return txt_file_lines


def create_title_list(file_name):
    txt_file_lines = open_file(file_name)
    games_list = []
    for i in txt_file_lines:
        games_list.append(i.split('\t')[TITLE])
    return games_list


def create_production_year_list(file_name):
    txt_file_lines = open_file(file_name)
    production_year_list = []
    for i in txt_file_lines:
        production_year_list.append(i.split('\t')[PRODUCTION_YEAR])
    return production_year_list


def create_genre_list(file_name):
    txt_file_lines = open_file(file_name)
    genres_list = []
    for i in txt_file_lines:
        genres_list.append(i.split('\t')[GENRE])
    return genres_list

def create_sales_list(file_name):
    txt_file_lines = open_file(file_name)
    sold_copies_list = []
    for i in txt_file_lines:
        sold_copies_list.append(i.split('\t')[SOLD_COPIES])
    return sold_copies_list

def get_fps_games_indexes(file_name):
    genre_list = create_genre_list(file_name)
    fps_game_indexes_list = []
    for i in range(len(genre_list)):
        if genre_list[i] == 'First-person shooter':
            fps_game_indexes_list.append(i)
    return fps_game_indexes_list
#############################################################################

# raczej spoko, mozna tez wyszukac po txt_file_lines
def count_games(file_name):
    games_list = create_title_list(file_name)
    return len(games_list)

# nie dzialaja testy, pomimo iz powinny; mozna tez wyszukac po txt_file_lines zamienic input na str
def decide(file_name, year):
    production_year_list = create_production_year_list(file_name)
    if str(year) in production_year_list:
        return True
    else:
        return False

# działa, ale mega nieelegancko, uzyc max zamiast for
def get_latest(file_name):
    production_year_list = create_production_year_list(file_name)
    games_list = create_title_list(file_name)
    latest_year = production_year_list[0]
    for i in production_year_list:
        if i > latest_year:
            latest_year = i
    latest_year_index = production_year_list.index(latest_year)
    latest_game = games_list[latest_year_index]
    return latest_game
    
# zrobione, mozna stworzyc osobna funkcje robiaca liste gaturnkow
def count_by_genre(file_name, genre):
    genres_list = create_genre_list(file_name)
    count = genres_list.count(genre)
    return count

# linie mają być zliczanie od 0 czy od 1? ValueError - mamy sami wymusić? Obecnie jest None w przypadku braku elementu.
def get_line_number_by_title(file_name, title):
    games_list = create_title_list(file_name)
    try:
        if title in games_list:
            title_line_number = games_list.index(title) + 1
            return  title_line_number
    except:
        pass
        
    
    # try:
    #     title_line_number = games_list.index(title) + 1
    #     return title_line_number
    # except ValueError:
    #     return "Non-existing game"
    # line_num = 0
    # txt_file_lines = open_file(file_name)
    # for line in txt_file_lines:
    #     line_num += 1
    #     if line.find(title) >= 0:
    #         return line_num

# tutaj wykorzystywana jest tylko lista gier, dlatego create_title_list mozna uzyc 2x
def sort_abc(file_name):
    games_list = create_title_list(file_name)
    games_list.sort()
    return games_list

# poprawić to bo tragedia jest + dlaczego wersja nizej nie dziala
def get_genres(file_name):
    genres_list = create_genre_list(file_name)
    genres_set = set(genres_list)
    genres_list = list(genres_set)
    genres_list.sort()
    return genres_list

# DLACZEGO TO NIE DZIAŁA?
# def get_genres(file_name):
#     txt_file_lines = open_file(file_name)
#     genres_list = []
#     for i in txt_file_lines:
#         if i not in genres_list:
#             genres_list.append(i.split('\t')[GENRE])
#     genres_list.sort()
#     return genres_list

# praca w toku/ problem z 
def when_was_top_sold_fps(file_name):
    try:
        fps_games_indexes_list = get_fps_games_indexes(file_name)
        sales_list = create_sales_list(file_name)
        production_year_list = create_production_year_list(file_name)
        fps_sales_list =[]
        for i in fps_games_indexes_list:
            fps_sales_list.append(sales_list[i])

        fps_sales_list = [float(x) for x in fps_sales_list]
        top_selling_fps_price = max(fps_sales_list)
        top_selling_fps_price_index = sales_list.index(str(top_selling_fps_price))
        return production_year_list[top_selling_fps_price_index]
    except:
        pass