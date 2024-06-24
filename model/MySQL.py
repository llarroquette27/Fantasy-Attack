from web_scrape_FP import scrape_data
import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': 'Lukas$12',
    'host': 'localhost',
}

# Establish a connection to MySQL server
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Create database
try:
    cursor.execute("CREATE DATABASE fantasy_football")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        print("Database already exists.")
    else:
        print(f"Failed creating database: {err}")
        exit(1)

# Connect to the newly created database
config['database'] = 'fantasy_football'
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Create tables
create_qb_table_query = """
CREATE TABLE IF NOT EXISTS qb_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    name VARCHAR(255),
    team VARCHAR(10),
    passCmp FLOAT,
    passAtt FLOAT,
    passPct FLOAT,
    passYds FLOAT,
    passYdsPerAtt FLOAT,
    passTd FLOAT,
    interceptions FLOAT,
    sacks FLOAT,
    rushAtt FLOAT,
    rushYds FLOAT,
    rushTd FLOAT,
    games FLOAT,
    fantasyPoints FLOAT,
    fantasyPointsPerGame FLOAT
)
"""
create_rb_table_query = """
CREATE TABLE IF NOT EXISTS rb_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    name VARCHAR(255),
    team VARCHAR(10),
    att FLOAT,
    rushYds FLOAT,
    ydsPerAtt FLOAT,
    lg FLOAT,
    plus20 FLOAT,
    rushTd FLOAT,
    rec FLOAT,
    targets FLOAT,
    recYards FLOAT,
    receiveTd FLOAT,
    games FLOAT,
    fantasyPoints FLOAT,
    fantasyPointsPerGame FLOAT
)
"""
create_wr_table_query = """
CREATE TABLE IF NOT EXISTS wr_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    name VARCHAR(255),
    team VARCHAR(10),
    rec FLOAT,
    targets FLOAT,
    yds FLOAT,
    lg FLOAT,
    plus20 FLOAT,
    yardsPerRec FLOAT,
    td FLOAT,
    games FLOAT,
    fantasyPoints FLOAT,
    fantasyPointsPerGame FLOAT
)
"""
create_te_table_query = """
CREATE TABLE IF NOT EXISTS te_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    name VARCHAR(255),
    team VARCHAR(10),
    rec FLOAT,
    targets FLOAT,
    yds FLOAT,
    lg FLOAT,
    plus20 FLOAT,
    yardsPerRec FLOAT,
    td FLOAT,
    games FLOAT,
    fantasyPoints FLOAT,
    fantasyPointsPerGame FLOAT
)
"""
# Execute table creation queries
cursor.execute(create_qb_table_query)
cursor.execute(create_rb_table_query)
cursor.execute(create_wr_table_query)
cursor.execute(create_te_table_query)

# Call the scrape_data function to get the arrays
data = scrape_data()
qbData, rbData, wrData, teData = data

# Insert data into the tables
insert_qb_query = """
INSERT INTO qb_data (
    year, name, team, passCmp, passAtt, passPct, passYds, passYdsPerAtt,
    passTd, interceptions, sacks, rushAtt, rushYds, rushTd, games, fantasyPoints, fantasyPointsPerGame
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for row in qbData:
    cursor.execute(insert_qb_query, row)

insert_rb_query = """
INSERT INTO rb_data (
    year, name, team, att, rushYds, ydsPerAtt, lg, plus20, rushTd, rec, targets,
    recYards, receiveTd, games, fantasyPoints, fantasyPointsPerGame
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for row in rbData:
    cursor.execute(insert_rb_query, row)

insert_wr_query = """
INSERT INTO wr_data (
    year, name, team, rec, targets, yds, lg, plus20, yardsPerRec, td, games, fantasyPoints, fantasyPointsPerGame
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for row in wrData:
    cursor.execute(insert_wr_query, row)

insert_te_query = """
INSERT INTO te_data (
    year, name, team, rec, targets, yds, lg, plus20, yardsPerRec, td, games, fantasyPoints, fantasyPointsPerGame
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for row in teData:
    cursor.execute(insert_te_query, row)

# Commit the changes
connection.commit()

# Close cursor and connection
cursor.close()
connection.close()

print("Database setup and data insertion completed successfully.")


