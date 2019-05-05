#%% import python libraries
import urllib.request
from bs4 import BeautifulSoup


#%% function: RecordLastGames
#   description: record player info & hit average of last 10 games
def RecordLastGames(playerId):
    MY_URL = "https://www.koreabaseball.com/Record/Player/HitterDetail/Basic.aspx?playerId=%d" % (playerId)
    # request URL
    req = urllib.request.Request(MY_URL)
    
    # fetch data from URL
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')
    
    ## get player info
    player_info = bs.find_all('div', attrs={'class':'player_info'})[0]
    TEAM_NAME = player_info.find_all('h4')[0].text
    
    player_basic = bs.find_all('div', attrs={'class':'player_basic'})[0]
    
    ul_tag = player_basic.find_all('ul')[0]
    li_tag = ul_tag.find_all('li')[0]
    
    POSITION = ul_tag.find_all('li')[3].text.split('(')[0].split(': ')[1]
    
    PLAYER_NAME = li_tag.find_all('span')[0].text
    
    if len(ul_tag.find_all('li')[1].find_all('span')[0].text) > 0:
        BACK_NUMBER = int(ul_tag.find_all('li')[1].find_all('span')[0].text)
    else:
        BACK_NUMBER = -1
    
    ## record of last 10 games
    table_tag = bs.find_all('table',
                            attrs={'summary':'최근 10경기 기록으로 타율,타수,득점,안타,도루허용,3루타,홈런,타점,도루 등을 나타냅니다.'})[0]
    tbody_tag = table_tag.find_all('tbody')[0]
    
    tr_tag = tbody_tag.find_all('tr')
    
    AB = 0
    HITS = 0
    for idx in range(len(tr_tag)):
        cur_tr_tag = tr_tag[idx]
        
        if len(cur_tr_tag.text.split('\n')[4]) > 0:
            AB += int(cur_tr_tag.text.split('\n')[4])
        
        if len(cur_tr_tag.text.split('\n')[6]) > 0:
            HITS += int(cur_tr_tag.text.split('\n')[6])
    
    AVG_LAST = 0
    if not AB == 0:
        AVG_LAST = HITS / AB
    
    RESULTS = {"playerName": PLAYER_NAME,
               "teamName": TEAM_NAME,
               "backNumber": BACK_NUMBER,
               "position": POSITION,
               "atBats": AB,
               "hits": HITS,
               "average": AVG_LAST}
    
    return RESULTS