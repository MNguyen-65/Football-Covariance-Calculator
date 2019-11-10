# Football-Covariance-Calculator
Prints out the covariance between the scores of different offensive positions for each football team.
Program will read from CSV files so replace "Salary and Player Data.csv" with the filename of your desired football data.
The data in the read csv files must be formatted with columns labelled: "Team", "Year", "Week", "QB", "RB", "WR", "TE", and "Def". 
Teams are labelled with their standard 3 letter acronyms, but you must edit the teams list if you don't label the Rams, Radiers, and Chargers in the same convention that we used (since the teams changed cities)
Each correlation matrix will be outputted to a CSV as teamname_corr.csv
Note that WR1 and RB1 are assigned to the wide reciever and runningback for each team that is regarded as the primary player of that position (measured by the cost of each player)
If you have any errors/bugs feel free to contact me
