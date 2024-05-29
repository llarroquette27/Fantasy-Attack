from bs4 import BeautifulSoup
import requests

# QB DATA
# -----------------------------------------------------------------
qbData = []

years = ['2023', '2022', '2021', '2020', '2019']
urls = []
for year in years:
    urls.append(requests.get('https://www.fantasypros.com/nfl/stats/qb.php?year=' + year))

year = 2023
for url in urls:
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
            rushYds = float(columns[11].text.strip().replace(',', ""))
            rushTd = float(columns[12].text.strip())
            games = float(columns[14].text.strip())
            fantasyPoints = float(columns[15].text.strip())
            fantasyPointsPerGame = float(columns[16].text.strip())

            values = [year, name, team, passCmp, passAtt, passPct,
            passYds, passYdsPerAtt, passTd, interceptions, sacks,
            rushAtt, rushYds, rushTd, games, fantasyPoints, fantasyPointsPerGame]
            qbData.append(values)
            
    year -= 1

print(qbData)

# RB DATA
# -----------------------------------------------------------------
rbData = []

years = ['2023', '2022', '2021', '2020', '2019']
urls = []
for year in years:
    urls.append(requests.get('https://www.fantasypros.com/nfl/stats/rb.php?year=' + year))

year = 2023
for url in urls:
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
            recYards = float(columns[10].text.strip().replace(',', ""))
            receiveTd = float(columns[12].text.strip())
            games = float(columns[14].text.strip())
            fantasyPoints = float(columns[15].text.strip())
            fantasyPointsPerGame = float(columns[16].text.strip())

            values = [year, name, team, att, rushYds, ydsPerAtt,
            lg, plus20, rushTd, rec, targets,
            recYards, receiveTd, games, fantasyPoints, fantasyPointsPerGame]
            rbData.append(values)
    year -= 1
    
print(rbData)

# WR DATA
# -----------------------------------------------------------------
wrData = []

years = ['2023', '2022', '2021', '2020', '2019']
urls = []
for year in years:
    urls.append(requests.get('https://www.fantasypros.com/nfl/stats/wr.php?year=' + year))

year = 2023

for url in urls:
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
            targets = float(columns[3].text.strip().replace(',', ""))
            yds = float(columns[4].text.strip().replace(',', ""))
            yardsPerRec = float(columns[5].text.strip())
            lg = float(columns[6].text.strip())
            plus20 = float(columns[7].text.strip())
            td = float(columns[8].text.strip())
            games = float(columns[13].text.strip())
            fantasyPoints = float(columns[14].text.strip())
            fantasyPointsPerGame = float(columns[15].text.strip())

            values = [year, name, team, rec, targets, yds,
            lg, plus20, yardsPerRec, td, games, fantasyPoints, fantasyPointsPerGame]
            wrData.append(values)

    year -= 1
    
print(wrData)

# TE DATA
# -----------------------------------------------------------------
teData = []

years = ['2023', '2022', '2021', '2020', '2019']
urls = []
for year in years:
    urls.append(requests.get('https://www.fantasypros.com/nfl/stats/te.php?year=' + year))

year = 2023
for url in urls:
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

            values = [year, name, team, rec, targets, yds,
            lg, plus20, yardsPerRec, td, games, fantasyPoints, fantasyPointsPerGame]
            teData.append(values)
    
    year -= 1
 
print(teData)
