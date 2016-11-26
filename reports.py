# How many games are in the file?
def count_games(file_name):
    counter = 0
    with open(file_name, "r") as my_file:
        for lines in my_file:
            counter += 1
    return counter

#Is there a game from a given year?
def decide(file_name, year):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # getting boolean
    for game in range(len(games_list)):
        if int(games_list[game][2]) == year:
            return True
    return False

# Which was the latest game?
def get_latest(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # lits from title and year
    newest = [games_list[0][2]]
    for game in games_list:
        if game[2] > newest[len(newest) - 1]:
            newest = [game[2]]
        elif game[2] == max:
            newest.append(game[2])
    # get latest
    final = []
    for year in newest:
        for game in games_list:
            if game[2] == year:
                final.append(game[0])
    return "" .join(final)

# How many games do we have by genre?
def count_by_genre(file_name, genre):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # counting
    counter = 0
    for game in games_list:
        if game[3] == genre:
            counter += 1
    return counter

# What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    for index in range(len(games_list)):
        if games_list[index][0] == title:
            return index + 1

    raise ValueError("Title doesn't exist.")

# What is the alphabetical ordered list of the titles?
def sort_abc(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))

    return(sorted([title[0] for title in games_list], key=lambda game_title: game_title.lower()))

# What are the genres?
def get_genres(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # get every title's genre
    genreall = []
    for i in range(len(games_list)):
        genreall.append(games_list[i][3])
    # get rid of same genres
    genre = []
    for i in genreall:
        if i not in genre:
            genre.append(i)
    return(sorted(genre, key=lambda x: x.lower()))

# What is the release date of the top sold "First-person shooter" game?
def when_was_top_sold_fps(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # getting fps games
    fps = []
    genre = "First-person shooter"
    for i in range(len(games_list)):
        if games_list[i][3] == genre:
            appending = games_list[i][0], games_list[i][1], games_list[i][2]
            fps.append(appending)
    # get release date
    if len(fps) == 0:
        raise ValueError("No Fps game found")
    else:
        top = max(float(game[1]) for game in fps)
    return int(list(filter(lambda game: float(game[1]) == top, fps))[0][2])
