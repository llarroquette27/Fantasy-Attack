from bs4 import BeautifulSoup
import requests

# QB DATA
# -----------------------------------------------------------------
qbData = []

url = requests.get('https://www.fantasypros.com/nfl/stats/qb.php')
soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find('div', attrs = {'class' : "mobile-table double-header mobile-table-report-page"}).find('table').find('tbody')

rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
        name = columns[1].find('a').text.strip()
        nameAndTeam = columns[1].text.strip().split()
        team = nameAndTeam[-1]
        team = team.replace('(', "")
        team = team.replace(')', "")
        passCmp = float(columns[2].text.strip())
        passAtt = float(columns[3].text.strip())
        passPct = float(columns[4].text.strip())
        passYds = float(columns[5].text.strip().replace(',', ""))
        passYdsPerAtt = float(columns[6].text.strip())
        passTd = float(columns[7].text.strip())
        interceptions = float(columns[8].text.strip())
        sacks = float(columns[9].text.strip())
        rushAtt = float(columns[10].text.strip())
        rushYds = float(columns[11].text.strip())
        rushTd = float(columns[12].text.strip())
        games = float(columns[14].text.strip())
        fantasyPoints = float(columns[15].text.strip())
        fantasyPointsPerGame = float(columns[16].text.strip())

        values = [name, team, passCmp, passAtt, passPct,
        passYds, passYdsPerAtt, passTd, interceptions, sacks,
        rushAtt, rushYds, rushTd, games, fantasyPoints, fantasyPointsPerGame]
        qbData.append(values)

#print(qbData)

# RB DATA
# -----------------------------------------------------------------
rbData = []

url = requests.get('https://www.fantasypros.com/nfl/stats/rb.php')
soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find('div', attrs = {'class' : "mobile-table double-header mobile-table-report-page"}).find('table').find('tbody')

rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
        name = columns[1].find('a').text.strip()
        nameAndTeam = columns[1].text.strip().split()
        team = nameAndTeam[-1]
        team = team.replace('(', "")
        team = team.replace(')', "")
        att = float(columns[2].text.strip())
        rushYds = float(columns[3].text.strip().replace(',', ""))
        ydsPerAtt = float(columns[4].text.strip())
        lg = float(columns[5].text.strip())
        plus20 = float(columns[6].text.strip())
        rushTd = float(columns[7].text.strip())
        rec = float(columns[8].text.strip())
        targets = float(columns[9].text.strip())
        recYards = float(columns[10].text.strip())
        receiveTd = float(columns[12].text.strip())
        games = float(columns[14].text.strip())
        fantasyPoints = float(columns[15].text.strip())
        fantasyPointsPerGame = float(columns[16].text.strip())

        values = [name, team, att, rushYds, ydsPerAtt,
        lg, plus20, rushTd, rec, targets,
        recYards, receiveTd, games, fantasyPoints, fantasyPointsPerGame]
        rbData.append(values)
    
#print(rbData)

# WR DATA
# -----------------------------------------------------------------
wrData = []

url = requests.get('https://www.fantasypros.com/nfl/stats/wr.php')
soup = BeautifulSoup(url.text, 'html.parser')
table = soup.find('div', attrs = {'class' : "mobile-table double-header mobile-table-report-page"}).find('table').find('tbody')

rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
        name = columns[1].find('a').text.strip()
        nameAndTeam = columns[1].text.strip().split()
        team = nameAndTeam[-1]
        team = team.replace('(', "")
        team = team.replace(')', "")
        rec = float(columns[2].text.strip())
        targets = float(columns[3].text.strip())
        yds = float(columns[4].text.strip().replace(',', ""))
        yardsPerRec = float(columns[5].text.strip())
        lg = float(columns[6].text.strip())
        plus20 = float(columns[7].text.strip())
        td = float(columns[8].text.strip())
        games = float(columns[13].text.strip())
        fantasyPoints = float(columns[14].text.strip())
        fantasyPointsPerGame = float(columns[15].text.strip())

        values = [name, team, rec, targets, yds,
        lg, plus20, yardsPerRec, td, games, fantasyPoints, fantasyPointsPerGame]
        wrData.append(values)
    
#print(wrData)

# TE DATA
# -----------------------------------------------------------------
teData = []

url = requests.get('https://www.fantasypros.com/nfl/stats/te.php')
soup = BeautifulSoup(url.text, 'html.parser')
table = soup.find('div', attrs = {'class' : "mobile-table double-header mobile-table-report-page"}).find('table').find('tbody')

rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
        name = columns[1].find('a').text.strip()
        nameAndTeam = columns[1].text.strip().split()
        team = nameAndTeam[-1]
        team = team.replace('(', "")
        team = team.replace(')', "")
        rec = float(columns[2].text.strip())
        targets = float(columns[3].text.strip())
        yds = float(columns[4].text.strip().replace(',', ""))
        yardsPerRec = float(columns[5].text.strip())
        lg = float(columns[6].text.strip())
        plus20 = float(columns[7].text.strip())
        td = float(columns[8].text.strip())
        games = float(columns[13].text.strip())
        fantasyPoints = float(columns[14].text.strip())
        fantasyPointsPerGame = float(columns[15].text.strip())

        values = [name, team, rec, targets, yds,
        lg, plus20, yardsPerRec, td, games, fantasyPoints, fantasyPointsPerGame]
        teData.append(values)
    
#print(teData)