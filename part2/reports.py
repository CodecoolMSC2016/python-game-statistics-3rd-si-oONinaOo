# What is the title of the most played game?
def get_most_played(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # list of all by title and popularity
    most_played = []
    for i in range(len(games_list)):
        appending = games_list[i][0], games_list[i][1]
        most_played.append(appending)
    top = max(float(game[1]) for game in most_played)   # get the top number
    for game in most_played:
        if top == game[1]:
            result = game[1]
    return str(list(filter(lambda game: float(game[1]) == top, most_played))[0][0]) # pair the number with title

# How many copies have been sold total?
def sum_sold(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # summing
    total = 0.0
    for game in range(len(games_list)):
        total += float(games_list[game][1])
    return total

# What is the average selling?
def get_selling_avg(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # summ all sold
    total = 0.0
    for game in range(len(games_list)):
        total += float(games_list[game][1])
    # count games in list
    counter = 0
    for i in games_list:
        counter += 1

    return(total / counter) # AVG = total / piece

# How many characters long is the longest title?
def count_longest_title(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # see all titles and get the longest
    longest = 0
    for game in range(len(games_list)):
        if len(games_list[game][0]) > len(games_list[longest][0]):
            longest = game
    return len(games_list[longest][0])

# What is the average of the release dates?
def get_date_avg(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # summing the years
    total = 0.0
    for game in range(len(games_list)):
        total += int(games_list[game][2])
    # count games in list
    counter = 0
    for i in games_list:
        counter += 1

    return round((total / counter)) # AVG = total / piece -> rounded to int

# What properties has a game?
def get_game(file_name, title):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # getting everyting to a different list from the title
    properties = []
    for game in range(len(games_list)):
        if title == games_list[game][0]:
            properties.append(games_list[game][0])
            properties.append(float(games_list[game][1]))
            properties.append(int(games_list[game][2]))
            properties.append(games_list[game][3])
            properties.append(games_list[game][4])
            return properties
    raise ValueError

# How many games are there grouped by genre?
def count_grouped_by_genre(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # making the dictionary and fill it with genres and the amount of genres
    grouped = {}
    for game in range(len(games_list)):
        if games_list[game][3] not in grouped:
            grouped.update(
                {games_list[game][3]: grouped.get(games_list[game][3], 0) + 1})

        else:
            grouped.update(
                {games_list[game][3]: grouped.get(games_list[game][3]) + 1})

    return grouped

# What is the date ordered list of the games?
def get_date_ordered(file_name):
    games_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            games_list.append(lines.strip().split("\t"))
    # sorting the list out
    games_list = sorted(games_list, key=lambda x: x[0], reverse=False)
    games_list = sorted(games_list, key=lambda x: int(x[2]), reverse=True)
    # addig just titles after sorting to a different list
    titles = []

    for i in range(len(games_list)):
        titles.append(games_list[i][0])

    return titles
