import time
from pyquery import PyQuery as pq

def getPTTBoard(html = 'https://www.ptt.cc/bbs/index.html'):
    doc = pq(html)
    board_items = doc('.board-name').items()
    board_list= [i.text() for i in board_items]
    
    return board_list
    

def getPTTArticle(board_name, page_num=10000):
    ptt_host = 'https://www.ptt.cc'
    board_index_html = 'https://www.ptt.cc/bbs/{}/index.html'.format(board_name)
    print('首頁網址:{}'.format(board_index_html))
    doc = pq(board_index_html, cookies={'over18': '1'}) 
    
    all_article = []
    i = 1
    
    while i <= page_num:
        for article_item in doc('.r-ent').items():
            article_dict = {}
            
            # print( '日期:{}'.format(article_item('.date').text()))
            article_dict['日期'] = article_item('.date').text()

            # print( '標題:{}'.format(article_item('.title').text()))
            article_dict['標題'] = article_item('.title').text()
            
            # print( '作者:{}'.format(article_item('.author').text()))
            article_dict['作者'] = article_item('.author').text()
            
            # print( '看板名稱:{}'.format(board_name))
            article_dict['看板名稱'] = board_name

            # 避免刪文情況
            if article_item('a').attr('href'):

                article_link = ''.join((ptt_host, article_item('a').attr('href')))

                # print('網址:{}'.format(article_link))
                article_dict['網址'] = article_link
                
                doc2 = pq(article_link, cookies={'over18': '1'})
                
                #print('內文:{}'.format(doc2('#main-content').text()))
                article_dict['內文'] = doc2('#main-content').text()
                
            else:
                article_dict['網址'] = None
                article_dict['內文'] = '此文已刪除'


            all_article.append(article_dict)
        # 取得上一頁按鈕
        # try:
        if doc('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)').attr('href'):
            i += 1
            previous_page_html = ''.join((ptt_host,doc('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)').attr('href')))
            print(previous_page_html)
            doc = pq(previous_page_html, cookies={'over18': '1'})
        # except:
        else: 
            print('All page done or some error.')
            return all_article
        
        # time.sleep(10)
    
    return all_article
if __name__ == '__main__':
    popular_board = getPTTBoard()
    for i in popular_board:
        print(getPTTArticle(i, 2))
        # print(getPTTArticle(i))