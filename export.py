import sys
import reports as r


source_file_name = sys.argv[1]
target_file_name = sys.argv[2]
input_year = sys.argv[3] 
input_genre = sys.argv[4]
input_title = sys.argv[5]


def start():
    results = save_results_to_a_list()
    save_results_to_a_file(results)


def save_results_to_a_file(results):
    f = open('results.txt', 'w')
    for i in range(len(results)):
        f.write(results[i] + '\n')
    f.close()

    f_reopened = open('results.txt', 'r')
    for line in f_reopened:
        print(line)
    f_reopened.close()


def save_results_to_a_list():
    production_year_result = production_year(source_file_name)
    games_number_in_genre_result = games_number_in_genre(source_file_name)
    line_number_by_title_result = line_number_by_title(source_file_name)
    results = [production_year_result, games_number_in_genre_result, line_number_by_title_result]
    return results


def production_year(file_name):
    game_from_inputed_year = r.decide(file_name, input_year)
    if game_from_inputed_year:
        return str(game_from_inputed_year)
    else:
        print(f"There is not any game in a file released in {input_year}.")  

   
def games_number_in_genre(file_name):
    genre_count = r.count_by_genre(file_name, input_genre)
    if genre_count:
        return str(genre_count)
    else:
        print(f"There's no such genre - {input_genre}. Please enter another one!")
        
    
def line_number_by_title(file_name):
    try:
        line_number = r.get_line_number_by_title(file_name, input_title)
        return str(line_number)
    except ValueError:
        print("There's no such title. Please enter another one!")
            

if __name__ == "__main__":
    start()