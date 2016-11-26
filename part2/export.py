import reports


def main():
    exporting = open('export.txt', 'w')
    exporting.write("The most played game: ")
    exporting.write(str(reports.get_most_played('game_stat.txt')))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Games total sold :")
    exporting.write(str(reports.sum_sold('game_stat.txt')))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Average Selling: ")
    exporting.write(str(reports.get_selling_avg("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Longest title is (character long): ")
    exporting.write(str(reports.count_longest_title("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Average release date is: ")
    exporting.write(str(reports.get_date_avg("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("The games asked properties: ")
    exporting.write(str(reports.get_game("game_stat.txt", "Minecraft")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Count each genre:")
    exporting.write(str(reports.count_grouped_by_genre("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')
    exporting.write("Date ordered list of games: ")
    exporting.write(str(reports.get_date_ordered("game_stat.txt")))
    exporting.write('\n')
    exporting.write('\n')

    return

main()

if __name__ == "__main__":
    main()
