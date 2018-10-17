'''
Created on 2018/10/17
lxml test
@author: Shohei
'''

import lxml.html, time
import requests as webs

def get_links_and_titles_from_top_page():
    #実際にNature Cell Biologyのサイトにつなげるときのメイン関数
    JOURNAL_NAME = "Nature Cell Biology"
    JOURNAL_URL = "https://www.nature.com/ncb/"
    
    #================================================ウェブサイトに接続してトップページを拾ってくる======
    #TODO request.getの例外処理
    time.sleep(1.0)
    web = webs.get(JOURNAL_URL)
    
    #================================================トップページから論文のタイトルやリンクページを拾う======
    
    #utf-8にエンコーディングしないとハイフンがドイツ文字になったりして文字化けする。
    #request.encodingでapparent_endcodingや='utf-8'だと文字化けしたままなので、fromstringのときにエンコーディングしている。
    my_parser = lxml.html.HTMLParser(encoding='utf-8')
    page = lxml.html.fromstring(html = web.content, parser = my_parser)
    
    #articleのタイトルとAbstractへのURLを取得する
    find_article_titles = lxml.etree.XPath('//*[@id="latest-research"]/div/section/div[1]/div/ul/li/article/div/h3/a')
    article_titles = find_article_titles(page)
    article_number = len(article_titles)
    
    find_article_links = lxml.etree.XPath('//*[@id="latest-research"]/div/section/div[1]/div/ul/li/article/div/h3/a/@href')
    article_links = find_article_links(page)   #リンクは相対パスになっている
    article_link_number = len(article_links)
    
    #例外処理。記事の数だけでOK?
    #もし変なものをタイトルとして拾っていた場合、データベースへの登録などはどうしたらいいだろう。
    if article_number == 0:
        print("記事の数が0です。{}のサイトのデザインが変更されている可能性があります。".format(JOURNAL_NAME))
        return
    
    elif article_link_number == 0:
        print("記事へのリンクの数が0です。{}のサイトのデザインが変更されている可能性があります。".format(JOURNAL_NAME))
        return 
    
    elif article_number != article_link_number:
        print("記事の数と記事へのリンクの数が一致しません。{}のサイトのデザインが変更されている可能性があります。".format(JOURNAL_NAME))
        return
    
    #article_titlesをElement型から、その内容の文字列に変える。
    for i in range(article_number):
        article_titles[i] = article_titles[i].text_content().strip()
        
    print(article_titles)
    
    return article_links, article_titles

def main():
    html_file_path = "C:/Users/Shohei/Dropbox/private/script/180704JournalCrawler/ncb_top.html"
    JOURNAL_NAME = "Nature Cell Biology"

    #utf-8にエンコーディングしないとハイフンがドイツ文字になったりして文字化けする。
    my_parser = lxml.html.HTMLParser(encoding='utf-8')
    page = lxml.html.parse(html_file_path, my_parser)
    
    #articleのタイトルとAbstractへのURLを取得する
    find_article_titles = lxml.etree.XPath('//*[@id="latest-research"]/div/section/div[1]/div/ul/li/article/div/h3/a')
    article_titles = find_article_titles(page)
    article_number = len(article_titles)
    
    find_article_links = lxml.etree.XPath('//*[@id="latest-research"]/div/section/div[1]/div/ul/li/article/div/h3/a/@href')
    article_links = find_article_links(page)   #リンクは相対パスになっている
    article_link_number = len(article_links)
    
    #例外処理。記事の数だけでOK?
    #もし変なものをタイトルとして拾っていた場合、データベースへの登録などはどうしたらいいだろう。
    if article_number == 0:
        print("記事の数が0です。{}のサイトのデザインが変更されている可能性があります。".format(JOURNAL_NAME))
        return
    
    elif article_link_number == 0:
        print("記事へのリンクの数が0です。{}のサイトのデザインが変更されている可能性があります。".format(JOURNAL_NAME))
        return 
    
    elif article_number != article_link_number:
        print("記事の数と記事へのリンクの数が一致しません。{}のサイトのデザインが変更されている可能性があります。".format(JOURNAL_NAME))
        return
    
    #article_titlesをElement型から、その内容の文字列に変える。
    for i in range(article_number):
        article_titles[i] = article_titles[i].text_content().strip()
        
    print(article_titles)
    
    return
    

if __name__ == "__main__":
    main()