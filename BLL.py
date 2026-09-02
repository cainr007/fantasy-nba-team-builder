from DAL import Database
from DAL import Fantasy_Team_DAL
from DAL import Players_DAL

class LogIn_BLL:
    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def logIn(self):
        database = Database(self.username, self.password, self.host, self.port)
        return database.try_connection()

class Fantasy_Team_BLL:
    def __init__(self, username, password, host, port):
        self.fantasy_team_dal = Fantasy_Team_DAL(username, password, host, port)

    def get_fantasy_team_summary(self, fantasyID):
        return self.fantasy_team_dal.get_fantasy_team_summary(fantasyID)

    def get_fantasy_team_players(self, fantasyID):
        return self.fantasy_team_dal.get_fantasy_team_players(fantasyID)

    def create_fantasy_team(self, fantasyName):
        if not fantasyName.strip():
            return "The fantasy team name can't be empty."
        result = self.fantasy_team_dal.create_fantasy_team(fantasyName)
        return result
    
    def add_to_fantasy_team(self, fantasyID, playerID):
        if fantasyID <= 0 or playerID <= 0:
            return "Invalid fantasy team ID or player ID."
        players = self.fantasy_team_dal.get_fantasy_team_players(fantasyID)
        for p in players:
            if p[0] == playerID:
                return "This player is already on your fantasy team."
        if len(players) >= 5:
            return "Your fantasy team already has 5 players. You'll have to remove a player before adding a new one."
        return self.fantasy_team_dal.add_to_fantasy_team(fantasyID, playerID)
    
    def update_fantasy_team(self, fantasyID, playerID, newPlayerID):
        if fantasyID <= 0 or playerID <= 0 or newPlayerID <= 0:
            return "Invalid fantasy team ID or player IDs."
        if newPlayerID == playerID:
            return "The new player ID is the same as the current player ID. No update needed!"
        players = self.fantasy_team_dal.get_fantasy_team_players(fantasyID)
        old_player_found = False
        for p in players:
            if p[0] == newPlayerID:
                return "This player is already on your fantasy team."
            if p[0] == playerID:
                old_player_found = True
        if not old_player_found:
            return "The player you want to replace is not in your fantasy team."
        return self.fantasy_team_dal.update_fantasy_team(fantasyID, playerID, newPlayerID)

    def remove_from_fantasy_team(self, fantasyID, playerID):
        if fantasyID <= 0 or playerID <= 0:
            return "Sorry, that's not a valid fantasy team ID or player ID."
        players = self.fantasy_team_dal.get_fantasy_team_players(fantasyID)
        for p in players:
            if p[0] == playerID:
                return self.fantasy_team_dal.remove_from_fantasy_team(fantasyID, playerID)
        return "Sorry, that player is not on your fantasy team."

class Players_BLL:
    def __init__(self, username, password, host, port):
        self.players_dal = Players_DAL(username, password, host, port)
        
    def get_player_list(self):
        return self.players_dal.get_player_list()