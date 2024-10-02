import function

def display_scoreboard():
    sql = "SELECT screen_name, points FROM game ORDER BY points DESC"
    cursor = function.yhteys.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()

    print("\nScoreboard:")
    for row in results:
        print(f"Player: {row[0]}, Points: {row[1]}")
