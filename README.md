## A TITLE WINNING TEAM FROM 2022
A dataset of 19k professional players is given, with more than 100+ attributes, a title winning team has to be made out of them, a team that not only win domestic title but also stand out among other title winners at the grand stage of Champions League, a team that doesn’t miss opportunities and neither give opportunities to opponent, could clutch at the last minute, play a beautiful game and at last win and all that on a budget.

### main.py
This code is using the mplsoccer library to create a soccer pitch visualization, using data from a MySQL database. It connects to a local MySQL server using the mysql.connector library and selects a database called “fifa”. Then it executes two queries from text files ‘sql_query.txt’ and ‘pre_requisite_query.txt’ to retrieve data from the database and stores it in a Pandas dataframe.

After that, it loops through the DataFrame and for each row, it retrieves the URLs of images of soccer players and loads them onto the pitch visualization using the PIL library. It also displays the name of the player on top of the image.


Dataset used is : https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset

Approach, Methodology used is explained in this article - https://medium.com/@manasvichoudhary8/title-winning-team-of-2022-81937d30b8e1
