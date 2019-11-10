teams = ["ari", "atl","det","ind","den","ten","chi","sea","pit","cin","car","buf","bal","jac","sfo","nor","tam","phi","min","oak","mia","nyj","sdg","hou","cle","kan","dal","gnb","nwe","was","nyg"]
positions = ["QB", "RB","WR","TE","PK","Def"]
import csv
import pandas
import numpy as np

data = pandas.read_csv("Salary and Player Data.csv")

best_scores = pandas.DataFrame(columns=["QB", "WR1", "WR2", "RB1", "RB2", "TE", "DEF"])

for team in teams:
    #print(team)
    teamdata = data.loc[data["Team"] == team]
    for year in [2014, 2015, 2016, 2017, 2018]:
        #print(year)
        yeardata = teamdata.loc[teamdata["Year"] == year]
        for week in range(1, 18):
            weekdata = yeardata.loc[teamdata["Week"] == week]
            if not weekdata.empty:
                # get the qb, top wr/rb, def and append
                QB = weekdata.loc[weekdata["Pos"] == "QB"]["FD points"].max()

                tmpRB = weekdata.loc[weekdata["Pos"] == "RB"].sort_values(by=["FD salary"])
                RBs = tmpRB["FD points"].nlargest(2)
                tmpWR = weekdata.loc[weekdata["Pos"] == "WR"].sort_values(by=["FD salary"])
                WRs = tmpWR["FD points"].nlargest(2)
                tmpTE = weekdata.loc[weekdata["Pos"] == "TE"].sort_values(by=["FD salary"])
                TE = tmpTE["FD points"].max()
                DEF = weekdata.loc[weekdata["Pos"] == "Def"]["FD points"].max()

                if len(RBs) != 2:
                    print("don't have 2 rbs for:", team, year, week)
                    RBs.loc[len(RBs)] = np.nan
                if len(WRs) != 2:
                    print("don't have 2 wrs for:", team, year, week)
                    WRs.loc[len(WRs)] = np.nan

                # append data to best_scores
                best_scores.loc[len(best_scores)] = {"QB": QB, "WR1": WRs.iloc[0], "WR2": WRs.iloc[1], "RB1": RBs.iloc[0], "RB2": RBs.iloc[1], "TE": TE, "DEF": DEF}
            else:
                print()

# we have all the data for a single team, create the covariance matrix
print("Below is the matrix for everything")
print(best_scores.corr())
best_scores.corr().to_csv("aggregate_corr.csv")