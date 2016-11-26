import reports


def main():
    exporting = open('export.txt', 'w')
    exporting.write("Number of games in the list: ")
    exporting.write(str(reports.count_games('game_stat.txt')))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Is there a game from the given year? :")
    exporting.write(str(reports.decide('game_stat.txt', 1999)))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Latest game: ")
    exporting.write(reports.get_latest('game_stat.txt'))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Genres in the list: ")
    exporting.write(str(reports.count_by_genre('game_stat.txt', 'RPG')))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("The line of this title is: ")
    exporting.write(str(reports.get_line_number_by_title('game_stat.txt', 'Crysis')))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Sorted by abc: ")
    exporting.write(str(reports.sort_abc("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Genres in (abc) :")
    exporting.write(str(reports.get_genres("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Release date of top sold FPS: ")
    exporting.write(str(reports.when_was_top_sold_fps("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')

    return

main()

if __name__ == "__main__":
    main()
