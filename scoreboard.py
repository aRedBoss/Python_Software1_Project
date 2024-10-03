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


                
                if choice == 1:
                    print("✅ Correct! You successfully avoided the storm and continue your journey.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                if choice == 1:
                    print("✅ Correct! You successfully avoided the storm and continue your journey.")
                    return 1
