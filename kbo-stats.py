#%% import python libraries
import os
import time
from last_games import RecordLastGames
from get_current_players import getPlayerIds


#%% html file path
HTML_PATH = './results/index.html'
ATBATS_THRESHOLD = 30

HTML_CONTENTS = []
HTML_CONTENTS.append('선수명')
HTML_CONTENTS.append('소속팀')
HTML_CONTENTS.append('등번호')
HTML_CONTENTS.append('포지션')
HTML_CONTENTS.append('타석수')
HTML_CONTENTS.append('안타수')
HTML_CONTENTS.append('타율')


#%% function: main
###############################################################################
if __name__ == "__main__":
    ## get date
    today = time.strftime("%Y/%m/%d")
    
    ## get player IDs
    PLAYER_ID_LIST = getPlayerIds()
    
    ## open file
    if os.path.exists(HTML_PATH):
        os.remove(HTML_PATH)
    
    with open(HTML_PATH, mode='a', encoding="utf-8") as the_file:
        the_file.write("<!DOCTYPE html>\n")
        the_file.write("<html>\n")
        the_file.write("<head>\n")
        the_file.write("    <title>KBO 타자 최근 10경기 성적</title>\n")
        the_file.write("    <link rel=\"stylesheet\" href=\"./css/jquery.dataTables.min.css\">\n")
        the_file.write("    <link rel=\"stylesheet\" href=\"./css/custom.css\">\n")
        the_file.write("    <script type=\"text/javascript\" src=\"./js/jquery-3.3.1.js\"></script>\n")
        the_file.write("    <script type=\"text/javascript\" src=\"./js/jquery.dataTables.min.js\"></script>\n")
        the_file.write("</head>\n")
        the_file.write("<body>\n")
        the_file.write("  <div id=\"upper_div\">\n")
        the_file.write("    <table>\n")
        the_file.write("      <tbody>\n")
        
        content = "            <th>KBO 타자 최근 10경기 성적 - %s, Summarized by Alex Choi</th>\n" % (today)
        the_file.write(content)
        the_file.write("        </tr>\n")
        the_file.write("      </tbody>\n")
        the_file.write("    </table>\n")
        the_file.write("  </div>\n")
        the_file.write("  <br>\n")
        the_file.write("    <table id=\"example\" class=\"display dataTable\" style=\"width: 100%\">\n")
        the_file.write("        <thead>\n")
        the_file.write("            <tr>\n")
        
        for tmp in HTML_CONTENTS:
            content = "                <th>%s</th>\n" % (tmp)
            the_file.write(content)
        
        the_file.write("            </tr>\n")
        the_file.write("        </thead>\n")
        the_file.write("        <tbody>\n")
        
        ## loop over player ID list
        cnt = 0
        for playerId in PLAYER_ID_LIST:
            cnt += 1
            print("Progress: %d / %d" % (cnt, len(PLAYER_ID_LIST)))
            
            results = RecordLastGames(playerId)
            
            if results['atBats'] > ATBATS_THRESHOLD:
                the_file.write("\n")
                the_file.write("            <tr>\n")
                
                content = "                <td>%s</td>\n" % (results['playerName'])
                the_file.write(content)
                
                content = "                <td>%s</td>\n" % (results['teamName'])
                the_file.write(content)
                
                content = "                <td>%d</td>\n" % (results['backNumber'])
                the_file.write(content)
                
                content = "                <td>%s</td>\n" % (results['position'])
                the_file.write(content)
                
                content = "                <td>%d</td>\n" % (results['atBats'])
                the_file.write(content)
                
                content = "                <td>%d</td>\n" % (results['hits'])
                the_file.write(content)
                
                content = "                <td>%5.3f</td>\n" % (results['average'])
                the_file.write(content)
                
                the_file.write("            </tr>\n")
                the_file.write("\n")
        
        the_file.write("        </tbody>\n")
        the_file.write("        <tfoot>\n")
        the_file.write("            <tr>\n")
        
        for tmp in HTML_CONTENTS:
            content = "                <th>%s</th>\n" % (tmp)
            the_file.write(content)
        
        the_file.write("            </tr>\n")
        the_file.write("        </tfoot>\n")
        the_file.write("    </table>\n")
        the_file.write("\n")
        the_file.write("  <script type=\"text/javascript\">\n")
        the_file.write("    $(document).ready(function() {\n")
        the_file.write("        $('#example').DataTable();\n")
        the_file.write("    } );\n")
        the_file.write("  </script>\n")
        the_file.write("\n")
        the_file.write("</body>\n")
        the_file.write("</html>\n")