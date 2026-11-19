#Author: Brett Rix
import pandas as pd

#Your program should:
#• Read the CSV file using Pandas.
game_data = pd.read_csv("video_games_raw.csv")

print()
print("VIDEO GAME CATALOG MANAGER")
print()

#• Ask the user for a specific row number to inspect. Validation done here too.
while True:
    user_input = input("Enter a row number to inspect: ")
    try:
        row_to_inspect = int(user_input) - 1
        if row_to_inspect >=0 and row_to_inspect < len(game_data):
            break
        else:
            print(f"Please input a valid row number from 1 to {len(game_data)}.")
            print()
    except ValueError:
        print("Please enter a valid input.")
        print()

#• Use .iloc[] to display information about the selected game.
selected_game = game_data.iloc[row_to_inspect]

print()
print("Selected Game:")
print(f"Title: {selected_game['Title']}")
print(f"Platform: {selected_game['Platform']}")
print(f"Genre: {selected_game['Genre']}")
print(f"Rating: {selected_game['Rating']}")
print(f"Current Status: {selected_game['Status']}")
print()

#• Ask the user to enter a new status for that game, such as Backlog, Playing, Completed,
#or Dropped.
print("Enter a new status:")
new_status = input()

#• Use .at[] to update the selected game’s status.
game_data.at[row_to_inspect, "Status"] = new_status

#• Add a Recommended column to the panda.
#• Set Recommended to No for all other games.
game_data["Recommended"] = "No"

#• Set Recommended to Yes for games that meet both of these criteria:
#o Rating is at least 8.
#o Price is $40 or less.
game_data.loc[(game_data["Rating"] >= 8) & (game_data["Price"] <= 40), "Recommended"] = "Yes"

#• Use .query() to display the recommended games.
print("Recommended Games:")
print(game_data.query('Recommended == "Yes"') [["Title", "Platform", "Price", "Rating"]])
print()

#• Save the updated data to a new file named video_games_cleaned.csv.
#The original CSV file should remain unchanged.
game_data.to_csv("video_games_cleaned.csv", index = False)

print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv.")
print()