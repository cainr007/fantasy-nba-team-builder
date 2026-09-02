DROP DATABASE IF EXISTS NBA_DB;
CREATE DATABASE IF NOT EXISTS NBA_DB;
USE NBA_DB;

CREATE TABLE Teams (
	teamID INT AUTO_INCREMENT PRIMARY KEY,
    teamName CHAR(3) NOT NULL
);

INSERT INTO Teams (teamName)
VALUES ('ATL'),('BOS'),('BKN'),('CHA'),('CHI'),('CLE'),
('DAL'),('DEN'),('DET'),('GSW'),('HOU'),('IND'),
('LAC'),('LAL'),('MEM'),('MIA'),('MIL'),('MIN'),
('NOP'),('NYK'),('OKC'),('ORL'),('PHI'),('PHX'),
('POR'),('SAC'),('SAS'),('TOR'),('UTA'),('WAS');

CREATE TABLE Players (
	playerID INT AUTO_INCREMENT PRIMARY KEY,
    playerName VARCHAR(50) NOT NULL,
    teamID INT NOT NULL,
    teamPosition ENUM ('PG', 'SG', 'SF', 'PF', 'C') NOT NULL,
    
    FOREIGN KEY (teamID) REFERENCES Teams (teamID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Players (playerName, teamID, teamPosition)
VALUES
('Shai Gilgeous-Alexander', 21, 'PG'),
('Luka Doncic', 14, 'PG'),
('Stephen Curry', 10, 'PG'),
('Trae Young', 4, 'PG'),
('Tyrese Haliburton', 12, 'PG'),
('Jalen Brunson', 20, 'PG'),
('Ja Morant', 15, 'PG'),
('De''Aaron Fox', 29, 'PG'),
('Damian Lillard', 17, 'PG'),
('LaMelo Ball', 4, 'PG'),
('Anthony Edwards', 18, 'SG'),
('Donovan Mitchell', 6, 'SG'),
('Devin Booker', 24, 'SG'),
('Jalen Williams', 21, 'SG'),
('Jaylen Brown', 2, 'SG'),
('Tyrese Maxey', 23, 'SG'),
('Jamal Murray', 8, 'SG'),
('Desmond Bane', 15, 'SG'),
('Zach LaVine', 6, 'SG'),
('Cade Cunningham', 9, 'SG'),
('LeBron James', 14, 'SF'),
('Kevin Durant', 24, 'SF'),
('Jayson Tatum', 2, 'SF'),
('Jimmy Butler', 10, 'SF'),
('Kawhi Leonard', 13, 'SF'),
('Brandon Ingram', 28, 'SF'),
('Franz Wagner', 22, 'SF'),
('Mikal Bridges', 20, 'SF'),
('Scottie Barnes', 28, 'SF'),
('OG Anunoby', 20, 'SF'),
('Giannis Antetokounmpo', 17, 'PF'),
('Anthony Davis', 7, 'PF'),
('Paolo Banchero', 22, 'PF'),
('Evan Mobley', 6, 'PF'),
('Zion Williamson', 19, 'PF'),
('Julius Randle', 18, 'PF'),
('Pascal Siakam', 12, 'PF'),
('Karl-Anthony Towns', 20, 'PF'),
('Jaren Jackson Jr.', 15, 'PF'),
('Alperen Sengun', 11, 'PF'),
('Nikola Jokic', 8, 'C'),
('Joel Embiid', 23, 'C'),
('Victor Wembanyama', 24, 'C'),
('Domantas Sabonis', 26, 'C'),
('Bam Adebayo', 16, 'C'),
('Rudy Gobert', 18, 'C'),
('Chet Holmgren', 21, 'C'),
('Jarrett Allen', 6, 'C'),
('Deandre Ayton', 25, 'C'),
('Myles Turner', 12, 'C');

CREATE TABLE Player_Stats (
	playerID INT PRIMARY KEY,
    ppg DECIMAL(5,2) NOT NULL,
    rpg DECIMAL(5,2) NOT NULL,
    apg DECIMAL(5,2) NOT NULL,
    
    FOREIGN KEY (playerID) REFERENCES Players (playerID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Player_Stats (playerID, ppg, rpg, apg)
VALUES
(1, 31.10, 4.30, 6.60),
(2, 33.50, 7.70, 8.30),
(3, 26.60, 3.60, 4.70),
(4, 17.90, 2.00, 8.00),
(5, 18.60, 3.50, 9.20),
(6, 26.00, 3.30, 6.80),
(7, 19.50, 3.30, 8.10),
(8, 18.60, 3.80, 6.20),
(9, 20.00, 4.00, 4.50),
(10, 20.10, 4.80, 7.10),
(11, 28.80, 5.00, 3.70),
(12, 27.90, 4.5, 5.70),
(13, 26.10, 3.90, 6.00),
(14, 17.10, 4.60, 5.50),
(15, 28.70, 6.90, 5.10),
(16, 28.30, 4.10, 6.60),
(17, 25.40, 4.40, 7.10),
(18, 20.10, 4.10, 4.10),
(19, 19.20, 2.80, 2.30),
(20, 23.90, 5.50, 9.90),
(21, 20.90, 6.10, 7.20),
(22, 26.00, 5.50, 4.80),
(23, 23.30, 10.70, 6.80),
(24, 20.00, 5.60, 4.90),
(25, 27.90, 6.40, 3.7),
(26, 21.50, 5.60, 3.80),
(27, 20.20, 6.10, 3.70),
(28, 14.40, 3.80, 3.70),
(29, 18.70, 7.80, 5.30),
(30, 16.70, 5.20, 2.20),
(31, 27.60, 9.80, 5.40),
(32, 20.40, 11.10, 2.80),
(33, 22.20, 8.40, 5.20),
(34, 18.20, 9.00, 3.60),
(35, 21.00, 5.70, 3.20),
(36, 21.10, 6.70, 5.00),
(37, 24.00, 6.60, 3.80),
(38, 20.10, 11.90, 3.00),
(39, 19.40, 5.70, 2.00),
(40, 22.00, 9.60, 6.70),
(41, 27.70, 12.90, 10.70),
(42, 26.90, 7.70, 3.90),
(43, 25.00, 11.70, 3.20),
(44, 15.80, 11.40, 4.10),
(45, 20.10, 10.00, 3.20),
(46, 10.90, 11.50, 1.70),
(47, 17.10, 8.90, 1.70),
(48, 15.40, 8.50, 1.80),
(49, 12.50, 8.00, 0.80),
(50, 11.90, 5.30, 1.50);

CREATE TABLE Fantasy_Team (
	fantasyID INT AUTO_INCREMENT PRIMARY KEY,
    fantasyName VARCHAR(50) NOT NULL,
    dateCreated DATE NOT NULL,
    isActive BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Fantasy_Players (
	fantasyID INT,
    playerID INT,
    
    PRIMARY KEY(fantasyID, playerID),
    
    FOREIGN KEY (fantasyID) REFERENCES Fantasy_Team (fantasyID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (playerID) REFERENCES Players (playerID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE VIEW All_Stats AS SELECT
Players.playerID, Players.playerName, Players.teamPosition, Teams.TeamID, teams.teamName, Player_Stats.ppg, Player_Stats.rpg, Player_Stats.apg
FROM Players
JOIN Teams
ON Players.teamID = Teams.teamID
JOIN Player_Stats
ON Players.playerID = Player_Stats.playerID;

CREATE VIEW All_PointGuards AS SELECT
Players.playerID, Players.playerName, Players.teamPosition, Teams.TeamID, teams.teamName, Player_Stats.ppg, Player_Stats.rpg, Player_Stats.apg
FROM Players
JOIN Teams
ON Players.teamID = Teams.teamID
JOIN Player_Stats
ON Players.playerID = Player_Stats.playerID
WHERE Players.teamPosition = 'PG';

CREATE VIEW All_ShootingGuards AS SELECT
Players.playerID, Players.playerName, Players.teamPosition, Teams.TeamID, teams.teamName, Player_Stats.ppg, Player_Stats.rpg, Player_Stats.apg
FROM Players
JOIN Teams
ON Players.teamID = Teams.teamID
JOIN Player_Stats
ON Players.playerID = Player_Stats.playerID
WHERE Players.teamPosition = 'SG';

CREATE VIEW All_SmallForwards AS SELECT
Players.playerID, Players.playerName, Players.teamPosition, Teams.TeamID, teams.teamName, Player_Stats.ppg, Player_Stats.rpg, Player_Stats.apg
FROM Players
JOIN Teams
ON Players.teamID = Teams.teamID
JOIN Player_Stats
ON Players.playerID = Player_Stats.playerID
WHERE Players.teamPosition = 'SF';

CREATE VIEW All_PowerForwards AS SELECT
Players.playerID, Players.playerName, Players.teamPosition, Teams.TeamID, teams.teamName, Player_Stats.ppg, Player_Stats.rpg, Player_Stats.apg
FROM Players
JOIN Teams
ON Players.teamID = Teams.teamID
JOIN Player_Stats
ON Players.playerID = Player_Stats.playerID
WHERE Players.teamPosition = 'PF';

CREATE VIEW All_Centers AS SELECT
Players.playerID, Players.playerName, Players.teamPosition, Teams.TeamID, teams.teamName, Player_Stats.ppg, Player_Stats.rpg, Player_Stats.apg
FROM Players
JOIN Teams
ON Players.teamID = Teams.teamID
JOIN Player_Stats
ON Players.playerID = Player_Stats.playerID
WHERE Players.teamPosition = 'C';

DELIMITER //
CREATE PROCEDURE GetAllPlayers()
BEGIN
SELECT * FROM All_Stats
ORDER BY ppg DESC;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AddToFantasyTeam(IN p_fantasyID INT, IN p_playerID INT)
BEGIN
INSERT INTO Fantasy_Players(fantasyID, playerID)
VALUES (p_fantasyID, p_playerID);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteFromFantasyTeam (IN p_fantasyID INT, IN p_playerID INT)
BEGIN
DELETE FROM Fantasy_Players WHERE fantasyID = p_fantasyID AND playerID = p_playerID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateFantasyTeam (IN p_fantasyID INT, IN p_oldPlayerID INT, IN p_newPlayerID INT)
BEGIN
UPDATE Fantasy_Players SET playerID = p_newPlayerID WHERE fantasyID = p_fantasyID AND playerID = p_oldPlayerID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE FantasyPlayerAverages(IN p_fantasyID INT)
BEGIN
SELECT
AVG(ppg) AS avgPPG, AVG(rpg) AS avgRPG, AVG(apg) AS avgAPG
FROM Fantasy_Players
JOIN Player_Stats
ON Fantasy_Players.playerID = Player_Stats.playerID
WHERE Fantasy_Players.fantasyID = p_fantasyID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE CreateFantasyTeam(IN p_fantasyName VARCHAR(50))
BEGIN
INSERT INTO Fantasy_Team (fantasyName, dateCreated)
VALUES (p_fantasyName, CURDATE());
SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetFantasyTeamPlayers(IN p_fantasyID INT)
BEGIN
SELECT 
	Players.playerID,
	Players.playerName,
	Players.teamPosition,
	Teams.teamName,
	Player_Stats.ppg,
	Player_Stats.rpg,
	Player_Stats.apg
FROM Fantasy_Players
JOIN Players
	ON Fantasy_Players.playerID = Players.playerID
JOIN Teams
	ON Players.teamID = Teams.teamID
JOIN Player_Stats
	ON Players.playerID = Player_Stats.playerID
WHERE Fantasy_Players.fantasyID = p_fantasyID;
END //
DELIMITER ;
