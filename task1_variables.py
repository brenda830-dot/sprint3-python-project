
# Column index reference (use these throughout the project)
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

total_games = len(video_game_sales)
print(total_games) 

avg_global_sales = sum(row[GLOBAL_SALES] 
for row in video_game_sales) / total_games 
print("Average global sales:",  
avg_global_sales) 

total_global_sales = sum(row[GLOBAL_SALES]  
for row in video_game_sales) 
top_game_share = (video_game_sales[0] 
[GLOBAL_SALES] / total_global_sales) * 100 
print("Wii Sports share of total global sales:", top_game_share, "%")
