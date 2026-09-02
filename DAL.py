import mysql.connector
from config import config

class Database():
    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def sqlconnect(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.username,
            password = self.password,
            database = config['database'],
            port = self.port
        )

    def try_connection(self):
        try:
            db = self.sqlconnect()
            db.close()
            return True
        except mysql.connector.Error:
            return False

class Fantasy_Team_DAL:
    def __init__(self, username, password, host, port):
        self.database = Database(username, password, host, port)
    
    def get_fantasy_team_summary(self, fantasyID):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('FantasyPlayerAverages', [fantasyID])
        summary = []
        for x in cursor.stored_results():
            summary = x.fetchall()
        cursor.close()
        db.close()
        return summary

    def get_fantasy_team_players(self, fantasyID):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('GetFantasyTeamPlayers', [fantasyID])
        players = []
        for x in cursor.stored_results():
            players = x.fetchall()
        cursor.close()
        db.close()
        return players

    def create_fantasy_team(self, fantasyName):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('CreateFantasyTeam', [fantasyName])
        fantasyID = None
        for x in cursor.stored_results():
            fantasyID = x.fetchone()[0]
        db.commit()
        cursor.close()
        db.close()
        return fantasyID


    def add_to_fantasy_team(self, fantasyID, playerID):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('AddToFantasyTeam', [fantasyID, playerID])
        db.commit()
        cursor.close()
        db.close()
    
    def update_fantasy_team(self, fantasyID, playerID, newPlayerID):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('UpdateFantasyTeam', [fantasyID, playerID, newPlayerID])
        db.commit()
        cursor.close()
        db.close()
    
    def remove_from_fantasy_team(self, fantasyID, playerID):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('DeleteFromFantasyTeam', [fantasyID, playerID])
        db.commit()
        cursor.close()
        db.close()

class Players_DAL:
    def __init__(self, username, password, host, port):
        self.database = Database(username, password, host, port)

    def get_player_list(self):
        db = self.database.sqlconnect()
        cursor = db.cursor()
        cursor.callproc('GetAllPlayers')
        players = []
        for x in cursor.stored_results():
            players = x.fetchall()
        cursor.close()
        db.close()
        return players