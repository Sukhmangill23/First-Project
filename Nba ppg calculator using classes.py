class average(): # Calulcate nba players average points per game

    def __init__(self,total_points,games_played):
        self.total = total_points
        self.games = games_played

class calculate(average):
    def __init(self,total,games):
        super().__init__(total,games)
    def ppg(self):
        return self.total/self.games

avg = calculate(2303,81)

print("The average points this player scored per game is " + str(avg.ppg()))



