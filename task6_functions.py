
# Video Game Sales Dataset
video_game_sales = [
    [1, 'Wii Sports', 'Wii', 2006, 'Sports', 'Nintendo', 41.49, 29.02, 3.77, 82.74],
    [2, 'Super Mario Bros.', 'NES', 1985, 'Platform', 'Nintendo', 29.08, 3.58, 6.81, 40.24],
    [3, 'Mario Kart Wii', 'Wii', 2008, 'Racing', 'Nintendo', 15.85, 12.88, 3.79, 35.82],
    [4, 'Wii Sports Resort', 'Wii', 2009, 'Sports', 'Nintendo', 15.75, 11.01, 3.28, 33.0],
    [5, 'Pokemon Red/Blue', 'GB', 1996, 'Role-Playing', 'Nintendo', 11.27, 8.89, 10.22, 31.37],
    [6, 'Tetris', 'GB', 1989, 'Puzzle', 'Nintendo', 23.2, 2.26, 4.22, 30.26],
    [7, 'New Super Mario Bros.', 'DS', 2006, 'Platform', 'Nintendo', 11.38, 9.23, 6.5, 30.01],
    [8, 'Wii Play', 'Wii', 2006, 'Misc', 'Nintendo', 14.03, 9.2, 2.93, 29.02],
    [9, 'New Super Mario Bros. Wii', 'Wii', 2009, 'Platform', 'Nintendo', 14.59, 7.06, 4.7, 28.62],
    [10, 'Duck Hunt', 'NES', 1984, 'Shooter', 'Nintendo', 26.93, 0.63, 0.28, 28.31],
    [11, 'Nintendogs', 'DS', 2005, 'Simulation', 'Nintendo', 9.07, 11.0, 1.93, 24.76],
    [12, 'Mario Kart DS', 'DS', 2005, 'Racing', 'Nintendo', 9.81, 7.57, 4.13, 23.42],
    [13, 'Pokemon Gold/Silver', 'GB', 1999, 'Role-Playing', 'Nintendo', 9.0, 6.18, 7.2, 23.1],
    [14, 'Wii Fit', 'Wii', 2007, 'Sports', 'Nintendo', 8.94, 8.03, 3.6, 22.72],
    [15, 'Kinect Adventures!', 'X360', 2010, 'Misc', 'Microsoft', 14.97, 4.94, 0.24, 21.82],
    [16, 'Grand Theft Auto V', 'PS3', 2013, 'Action', 'Take-Two', 7.01, 9.27, 0.97, 21.4],
    [17, 'Grand Theft Auto: San Andreas', 'PS2', 2004, 'Action', 'Take-Two', 9.43, 0.4, 0.41, 20.81],
    [18, 'Super Mario World', 'SNES', 1990, 'Platform', 'Nintendo', 12.78, 3.75, 3.54, 20.61],
    [19, 'Brain Age', 'DS', 2005, 'Puzzle', 'Nintendo', 4.75, 9.26, 4.16, 20.22],
    [20, 'Pokemon Diamond/Pearl', 'DS', 2006, 'Role-Playing', 'Nintendo', 6.42, 4.52, 6.04, 18.36],
]

RANK = 0
NAME = 1
PLATFORM = 2
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9

# Define column index constants for readability
NAME = 0
YEAR = 1
GENRE = 2
NA_SALES = 3
EU_SALES = 4
JP_SALES = 5
OTHER_SALES = 6
GLOBAL_SALES = 7

# Sample dataset representing rows: [Name, Year, Genre, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales]
dataset = [
    ["Wii Sports", 2006, "Sports", 41.49, 29.02, 3.77, 8.46, 82.74],
    ["Super Mario Bros.", 1985, "Platform", 29.08, 3.58, 6.81, 0.77, 40.24],
    ["Mario Kart Wii", 2008, "Racing", 15.68, 12.76, 3.79, 3.29, 35.52],
    ["Super Mario World", 1990, "Platform", 12.78, 3.75, 3.54, 0.55, 20.61],
    ["Pokemon Red/Pokemon Blue", 1996, "Role-Playing", 11.27, 8.89, 10.22, 1.00, 31.37]
]

# --- Part A: calculate_total_sales ---
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

# Testing Part A
first_game = dataset[0]
total_regional_sales = calculate_total_sales(first_game)
print("--- Part A Test ---")
print(f"Total NA + EU + JP sales for '{first_game[NAME]}': ${total_regional_sales:.2f}M\n")


# --- Part B: filter_by_genre ---
def filter_by_genre(data, genre="Platform"):
    result = []
    for game in data:
        if game[GENRE].lower() == genre.lower():
            result.append(game)
    return result

# Testing Part B
print("--- Part B Tests ---")
# 1. Without specifying genre (uses default 'Platform')
default_filtered = filter_by_genre(dataset)
print(f"Games with default genre ('Platform'): {[g[NAME] for g in default_filtered]}")

# 2. Specifying a genre ('Racing')
racing_filtered = filter_by_genre(dataset, "Racing")
print(f"Games with genre 'Racing': {[g[NAME] for g in racing_filtered]}\n")


# --- Part C: get_summary & loop ---
def get_summary(game):
    # Uses the total sales from the row (or calculated sales) formatted to 2 decimal places
    sales = game[GLOBAL_SALES]
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${sales:.2f}M"

# Testing Part C
print("--- Part C Test: Full Dataset Summary ---")
for game in dataset:
    print(get_summary(game))
