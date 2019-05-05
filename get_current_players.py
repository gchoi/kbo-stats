#%% import python libraries
import urllib.request
from bs4 import BeautifulSoup

#%% function: getPlayerIds
def getPlayerIds():
    URL_LIST = []
    
    ## SK
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/sk-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/sk-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/sk-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/sk-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/sk-player-05.html')
    
    ## DOOSAN
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/doosan-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/doosan-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/doosan-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/doosan-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/doosan-player-05.html')
    
    ## HANWHA
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/hanwha-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/hanwha-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/hanwha-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/hanwha-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/hanwha-player-05.html')
    
    ## KIWOOM
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kiwoom-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kiwoom-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kiwoom-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kiwoom-player-04.html')
    
    ## KIA
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kia-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kia-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kia-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kia-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kia-player-05.html')
    
    ## SAMSUNG
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/samsung-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/samsung-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/samsung-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/samsung-player-04.html')
    
    ## LOTTE
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lotte-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lotte-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lotte-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lotte-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lotte-player-05.html')
    
    ## LG
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lg-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lg-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lg-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lg-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/lg-player-05.html')
    
    ## KT
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kt-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kt-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kt-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/kt-player-04.html')
    
    ## NC
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/nc-player-01.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/nc-player-02.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/nc-player-03.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/nc-player-04.html')
    URL_LIST.append('file:///D:/Projects/Python/project-02/DataScience/Baseball/Source/kbo-stats/dataset/nc-player-05.html')
    
    ###########################################################################
    # iteration over URL_LIST
    PLAYER_ID_LIST = []
    for URL in URL_LIST:
        # request URL
        req = urllib.request.Request(URL)
        
        # fetch data from URL
        data = urllib.request.urlopen(req).read()
        bs = BeautifulSoup(data, 'html.parser')
        
        # get playerIds
        table_tag = bs.find_all('table',
                                attrs={'summary':'경기내용인 2루타,3루타,홈런,도루를 확인 하실 수 있습니다'})[0]
        tbody_tag = table_tag.find_all('tbody')[0]
        tr_tag = tbody_tag.find_all('tr')
        
        for idx in range(len(tr_tag)):
            cur_tr_tag = tr_tag[idx]
            td_tag = cur_tr_tag.find_all('td')[1]
            a_tag = td_tag.find_all('a')[0]
            
            position = cur_tr_tag.find_all('td')[3].text
            if not position == '투수':
                playerId = int(a_tag.attrs['href'].split('playerId=')[1])
                PLAYER_ID_LIST.append(playerId)
        
    return(PLAYER_ID_LIST)