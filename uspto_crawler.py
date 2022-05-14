#-----------------------------------------------------------------------------
#  import
#-----------------------------------------------------------------------------
#  自己的模組
import is_folder
import line_notify_token
#  其他的模組
from selenium import webdriver
import bs4
import threading
import time
from fake_useragent import UserAgent
import re
import queue
import pandas
#-----------------------------------------------------------------------------
#  filepath
#-----------------------------------------------------------------------------
file_path = input('Please input filepath(EN):')
is_folder.is_folder_exist(file_path)
#-----------------------------------------------------------------------------
#  chrome driver
#-----------------------------------------------------------------------------
driver_path = file_path + '/webdriver/chromedriver_0'
driver = webdriver.Chrome(driver_path)
search_words = input('Search for ?\nP.S. Please in EN\n')
search_words.replace(' ', '+')
url = 'https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=' + search_words + '&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'
driver.get(url)
#  總專利數量＆總共幾頁
patent_amount = int(driver.find_element_by_xpath("/html/body/i/strong[3]").text)
if (patent_amount % 50) == 0:
    patent_page_amount = (patent_amount // 50)
else :
    patent_page_amount = (patent_amount // 50) + 1
print('Results of Search in US Patent Collection db for:\n' + str(patent_amount) + ' patents')
print(str(patent_page_amount) + ' pages in total')
driver.quit()
line_notify_token.line_notify_message('\nResults in db for:\n' + str(patent_amount) + ' patents\n' +  str(patent_page_amount) + ' pages in total')
#  進度條開始
progress_bar_patent_amount = 0
lock = threading.Lock()  #  鎖住線程不重複
#  主要爬蟲工作 單線程
#  主要爬蟲工作 多線程
def spider_job(thread_number, thread_page):
    global progress_bar_patent_amount
    #  fake UA
    ua = UserAgent()
    opt = webdriver.ChromeOptions()
    opt.add_argument('--user-agent=%s' % ua.random)
    opt.add_argument('--headless')  # 背景執行
    #  分別啟動４個線程
    driver_path_thread = file_path + '/webdriver/chromedriver_' + str(thread_number)
    driver_thread = webdriver.Chrome(driver_path_thread, options = opt)
    #  每個線程得到的 data 
    patent_index_list_thread = []
    patent_etAl_list_thread = []
    patent_date_list_thread = []
    patent_title_list_thread = []
    patent_abstract_list_thread = []
    patent_detail_list_thread = []
    patent_priorPublication_detail_list_thread = []
    patent_related_us_list_thread = []
    patent_foreignApplicationPriority_list_thread = []
    patent_referencesCited_us_documents_list_thread = []
    patent_referencesCited_foreign_documents_list_thread = []
    patent_ipc_list_thread = []
    patent_err_list_thread = []
    #  開始爬蟲
    original_patent_number = (thread_page - 1) * 50 + 1  #  目前在所有專利裡面的第幾個
    page_limit = thread_page_list[thread_number + 1]
    while thread_page < page_limit:  #  停止在四等份的下一份前
        line_notify_token.line_notify_message('\nThread ' + str(thread_number) + '\nIn page ' + str(thread_page))
        current_patent_number = 1  #  在每頁 50 個裡的第幾個
        while current_patent_number < 51:
            url = 'https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=' + str(original_patent_number) + '&f=G&l=50&d=PTXT&s1=%22' + search_words + '%22&p=' + str(thread_page) + '&OS=%22' + search_words + '%22'
            if 0 < thread_page < (patent_page_amount - 1) :
                driver_thread.get(url)
            else:  #  到了最後一頁
                if patent_amount - original_patent_number >= 0 :
                    driver_thread.get(url)
                else:
                    break
            #  找到專利號碼作為 index
            patent_index_thread = driver_thread.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[2]').text
            patent_index_list_thread.append(patent_index_thread)
            #  找到作者
            patent_etAl_thread = driver_thread.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[1]').text
            patent_etAl_list_thread.append(patent_etAl_thread)
            #  公告日期，也就是專利核准的日期
            patent_date_thread = driver_thread.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]').text
            patent_date_list_thread.append(patent_date_thread)
            #  專利名稱
            patent_title_thread = driver_thread.find_element_by_xpath('/html/body/font').text
            patent_title_list_thread.append(patent_title_thread)
            #  將 html 存放於 txt
            root = bs4.BeautifulSoup(driver_thread.page_source, 'html.parser')
            with open(file_path + '/uspto_data/WebHtml/' + patent_index_thread + '.txt', mode = 'w', encoding = 'utf = 8') as web_file:
                print(root.prettify(), file = web_file)
            #  用 html 對比尋找 xpath 位置
            def match_xpath(abstract, detail, priorPublication_detail, related_us, foreignApplicationPriority, referencesCited_us_documents, referencesCited_foreign_documents):
                #  專利簡介
                if abstract == '0':
                    patent_abstract_thread = 'NONE'
                else:
                    patent_abstract_thread = driver_thread.find_element_by_xpath('/html/body/p[' + abstract + ']').text
                patent_abstract_list_thread.append(patent_abstract_thread)
                #  專利詳細內容區塊
                if detail == '0':
                    patent_detail_thread = 'NONE'
                else:
                    patent_detail_thread = driver_thread.find_element_by_xpath('/html/body/table[' + detail + ']').text
                patent_detail_list_thread.append(patent_detail_thread)
                #  先期公開資料，包含編號及日期
                if priorPublication_detail == '0':
                    patent_priorPublication_detail_thread = 'NONE'
                else:
                    patent_priorPublication_detail_thread = driver_thread.find_element_by_xpath('/html/body/table[' + priorPublication_detail + ']').text
                patent_priorPublication_detail_list_thread.append(patent_priorPublication_detail_thread)
                # 專利母案的相關資料
                if related_us == '0':
                    patent_related_us_thread = 'NONE'
                else:
                    patent_related_us_thread = driver_thread.find_element_by_xpath('/html/body/table[' + related_us + ']').text
                patent_related_us_list_thread.append(patent_related_us_thread)
                #  國外專利申請相關資料
                if foreignApplicationPriority == '0':
                    patent_foreignApplicationPriority_thread = 'NONE'
                else:
                    patent_foreignApplicationPriority_thread = driver_thread.find_element_by_xpath('/html/body/table[' + foreignApplicationPriority + ']').text
                patent_foreignApplicationPriority_list_thread.append(patent_foreignApplicationPriority_thread)
                # 引用誰 US
                if referencesCited_us_documents == '0':
                    patent_referencesCited_us_documents_thread = 'NONE'
                else:
                    patent_referencesCited_us_documents_thread = driver_thread.find_element_by_xpath('/html/body/table[' + referencesCited_us_documents + ']').text
                patent_referencesCited_us_documents_list_thread.append(patent_referencesCited_us_documents_thread)
                # 引用誰 US以外
                if referencesCited_foreign_documents == '0':
                    patent_referencesCited_foreign_documents_thread = 'NONE'
                else:
                    patent_referencesCited_foreign_documents_thread = driver_thread.find_element_by_xpath('/html/body/table[' + referencesCited_foreign_documents + ']').text
                patent_referencesCited_foreign_documents_list_thread.append(patent_referencesCited_foreign_documents_thread)
                # 國際分類號
                try:
                    patent_ipc_thread = driver_thread.find_element_by_xpath('/html/body/p[2]/table/tbody/tr[3]/td[2]').text
                except:
                    patent_ipc_thread = driver_thread.find_element_by_xpath('/html/body/p[2]/table/tbody/tr[2]/td[2]').text
                patent_ipc_list_thread.append(patent_ipc_thread)
            with open(file_path + '/uspto_data/WebHtml/' + patent_index_thread + '.txt', mode = 'r', encoding = 'utf = 8') as web_file:
                data = web_file.read()
                regex = r"\s{2}Abstract"
                regex2 = r"\s{5}\*\*Please see images for:"
                regex3 = r"\s{2}Prior Publication Data"
                regex4 = r"\s{2}Related U\.S\. Patent Documents"
                regex5 = r"\s{2}Foreign Application Priority Data"
                regex6 = r"\s{3}U\.S\. Patent Documents"
                regex7 = r"\s{3}Foreign Patent Documents"
                test_str = (data)
                m = re.findall(regex, test_str)
                m2 = re.findall(regex2, test_str)
                m3 = re.findall(regex3, test_str)
                m4 = re.findall(regex4, test_str)
                m5 = re.findall(regex5, test_str)
                m6 = re.findall(regex6, test_str)
                m7 = re.findall(regex7, test_str)
                time.sleep(1)
                #  c4 取 0
                if (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '5', '6', '7', '8', '9')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '5', '6', '7', '8', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '4', '5', '6', '7', '8')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '4', '5', '6', '7', '0')
                #  c4 取 1
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '0', '5', '6', '7', '8')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '0', '5', '6', '7', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '0', '4', '5', '6', '7')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '0', '4', '5', '6', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '5', '0', '6', '7', '8')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '5', '0', '6', '7', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '4', '0', '5', '6', '7')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '4', '0', '5', '6', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '5', '6', '0', '7', '8')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '5', '6', '0', '7', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '4', '5', '0', '6', '7')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '4', '5', '0', '6', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '5', '6', '7', '0', '8')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '5', '6', '7', '0', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '4', '5', '6', '0', '7')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '4', '5', '6', '0', '0')
                #  c4 取 2
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '0', '0', '5', '6', '7')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '0', '0', '5', '6', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '0', '0', '4', '5', '6')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '0', '0', '4', '5', '0')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '0', '5', '0', '6', '7')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '0', '5', '0', '6', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '0', '4', '0', '5', '6')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '0', '4', '0', '5', '0')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '0', '5', '6', '0', '7')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '0', '5', '6', '0', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '0', '4', '5', '0', '6')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '0', '4', '5', '0', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '5', '0', '0', '6', '7')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '5', '0', '0', '6', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '4', '0', '0', '5', '6')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '4', '0', '0', '5', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '5', '0', '6', '0', '7')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '5', '0', '6', '0', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '4', '0', '5', '0', '6')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '4', '0', '5', '0', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '5', '6', '0', '0', '7')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '5', '6', '0', '0', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '4', '5', '0', '0', '6')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '4', '5', '0', '0', '0')
                #  c4 取 3
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '4', '0', '0', '0', '5', '6')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '4', '0', '0', '0', '5', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []):
                    match_xpath('1', '3', '0', '0', '0', '4', '5')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []):
                    match_xpath('1', '3', '0', '0', '0', '4', '0')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '0', '0', '5', '0', '6')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '0', '0', '5', '0', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '0', '0', '4', '0', '5')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '0', '0', '4', '0', '0')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '0', '5', '0', '0', '6')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '0', '5', '0', '0', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '0', '4', '0', '0', '5')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '0', '4', '0', '0', '0')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '4', '5', '0', '0', '0', '6')
                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '4', '5', '0', '0', '0', '0')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []):
                    match_xpath('1', '3', '4', '0', '0', '0', '5')
                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []):
                    match_xpath('1', '3', '4', '0', '0', '0', '0')
                #  c4 取 4
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    match_xpath('1', '4', '0', '0', '0', '0', '5')
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    match_xpath('1', '4', '0', '0', '0', '0', '0')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    match_xpath('1', '3', '0', '0', '0', '0', '4')
                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    match_xpath('1', '3', '0', '0', '0', '0', '0')
                #  例外視為 error 之後再根據 index 手動添加
                else:
                    patent_err_list_thread.append(patent_index_thread)
                    patent_index_list_thread.pop()
                    patent_etAl_list_thread.pop()
                    patent_date_list_thread.pop()
                    patent_title_list_thread.pop()
            original_patent_number += 1
            current_patent_number += 1
            time.sleep(0.5)
            lock.acquire()
            progress_bar_patent_amount += 1
            lock.release()
        thread_page += 1
    #  合成一個[]
    combined_list_thread = [
        patent_index_list_thread,
        patent_etAl_list_thread,
        patent_date_list_thread,
        patent_title_list_thread,
        patent_abstract_list_thread,
        patent_detail_list_thread,
        patent_priorPublication_detail_list_thread,
        patent_related_us_list_thread,
        patent_foreignApplicationPriority_list_thread,
        patent_referencesCited_us_documents_list_thread,
        patent_referencesCited_foreign_documents_list_thread,
        patent_ipc_list_thread,
        patent_err_list_thread
        ]
    q.put(combined_list_thread)
    driver_thread.quit()
#-----------------------------------------------------------------------------
#  threading
#-----------------------------------------------------------------------------
# 小於 4 頁部分線程
if patent_page_amount < 4:
    thread_page_list = []
    for i in range(patent_page_amount):
        thread_page_list.append(i + 1)
    thread_page_list.append(patent_page_amount + 1)  #  設置線程結束在最後一頁
    q = queue.Queue()
    start_time = time.perf_counter()  #  計時線程總時數
    threads = []
    for i in range(patent_page_amount):
        threads.append(threading.Thread(target = spider_job, args = [i, thread_page_list[i], ]))
        threads[i].start()
        time.sleep(20)  #  避免短時間網頁請求過多
    print('--------------------Threading Progress Start--------------------')
    while progress_bar_patent_amount < patent_amount:
        print('\r' + '[Threading Progress] ---> [%s%s]%.2f%% TIME --> %.2fs; ' % ('▋' * int(progress_bar_patent_amount*25/patent_amount), ' ' * (25-int(progress_bar_patent_amount*25/patent_amount)), float(progress_bar_patent_amount/patent_amount*100), float(time.perf_counter() - start_time)), end='')
        time.sleep(5)
    else:
        print('\r' + '[Threading Progress] ---> [%s%s]%.2f%% TIME --> %.2fs; ' % ('▋' * int(progress_bar_patent_amount*25/patent_amount), ' ' * (25-int(progress_bar_patent_amount*25/patent_amount)), float(progress_bar_patent_amount/patent_amount*100), float(time.perf_counter() - start_time)), end='')
    for i in range(patent_page_amount):
        threads[i].join()
    line_notify_token.line_notify_message('\nThreading Progress Done')
    print('\n--------------------Threading Progress Done--------------------')
    temp_list = [[],[],[],[],[],[],[],[],[],[],[],[],[]]  #  模擬不足四線程的空集合
    for i in range(4 - patent_page_amount):
        q.put(temp_list)
# 大於 4 頁全部線程
else:
    x = (patent_page_amount // 4)
    y = (patent_page_amount % 4)
    thread_page_list = [1]
    i = 1
    j = 1
    while y > 0:
        i = i + x + 1
        y -= 1
        j += 1
        thread_page_list.append(i)
    while y == 0 and j < 4:
        i += x
        j += 1
        thread_page_list.append(i)
    thread_page_list.append(patent_page_amount + 1)  #  設置線程結束在最後一頁
    q = queue.Queue()
    start_time = time.perf_counter()  #  計時線程總時數
    threads = []
    for i in range(4):
        threads.append(threading.Thread(target = spider_job, args = [i, thread_page_list[i], ]))
        threads[i].start()
        time.sleep(30)  #  避免短時間網頁請求過多
    print('--------------------Threading Progress Start--------------------')
    while progress_bar_patent_amount < patent_amount:
        print('\r' + '[Threading Progress] ---> [%s%s]%.2f%% TIME --> %.2fs; ' % ('▋' * int(progress_bar_patent_amount*25/patent_amount), ' ' * (25-int(progress_bar_patent_amount*25/patent_amount)), float(progress_bar_patent_amount/patent_amount*100), float(time.perf_counter() - start_time)), end='')
        time.sleep(5)
    else:
        print('\r' + '[Threading Progress] ---> [%s%s]%.2f%% TIME --> %.2fs; ' % ('▋' * int(progress_bar_patent_amount*25/patent_amount), ' ' * (25-int(progress_bar_patent_amount*25/patent_amount)), float(progress_bar_patent_amount/patent_amount*100), float(time.perf_counter() - start_time)), end='')
    for i in range(4):
        threads[i].join()
    line_notify_token.line_notify_message('\nThreading Progress Done')
    print('\n--------------------Threading Progress Done--------------------')
combined_list_1 = q.get()
combined_list_2 = q.get()
combined_list_3 = q.get()
combined_list_4 = q.get()
#-----------------------------------------------------------------------------
#  cleaning data
#-----------------------------------------------------------------------------
#  專利編號作為 dataframe 的 index
patent_index_list = combined_list_1[0] + combined_list_2[0] + combined_list_3[0] + combined_list_4[0]
#  該專利有多人團隊或是單人
patent_etAl_list = combined_list_1[1] + combined_list_2[1] + combined_list_3[1] + combined_list_4[1]
etAl = []  #  團隊
n_etAl = []  #  單人
for i in patent_etAl_list:
    if ' ,   et al.' in i:
        etAl.append(i.replace(' ,   et al.', ''))
        n_etAl.append('NONE')
    else:
        etAl.append('NONE')
        n_etAl.append(i)
#  重組 yyyy-mm-dd replace
patent_date_list = combined_list_1[2] + combined_list_2[2] + combined_list_3[2] + combined_list_4[2]
dic_month = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
dic_month_2 = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }
full_date = []  #  符合格式 YYYY-MM-DD
year_date = []  #  只有年份
for i in patent_date_list:
    for i_2 in dic_month:
        if i_2 in i :
            if i[-8] != ' ':
                full_date.append(i[-4:-1] + i[-1] + '-' + dic_month[i_2] + '-' + i[-8] + i[-7])
            else:
                full_date.append(i[-4:-1] + i[-1] + '-' + dic_month[i_2] + '-0' + i[-7])
    year_date.append(i[-4:-1] + i[-1])
#  標題
patent_title_list = combined_list_1[3] + combined_list_2[3] + combined_list_3[3] + combined_list_4[3]
#  簡介
patent_abstract_list = combined_list_1[4] + combined_list_2[4] + combined_list_3[4] + combined_list_4[4]
#  分割成多項 Inventors Family_ID Appl_No Filed PCT_Filed PCT_No 371Date PCT_Pub_No PCT_Pub_Date Applicant Assignee
patent_detail_list = combined_list_1[5] + combined_list_2[5] + combined_list_3[5] + combined_list_4[5]
def normalization_date(list_need_to_normalization):  #  用來正規化日期
    temp_list = []
    for i in list_need_to_normalization:
        if i == 'NONE':
            temp_list.append('NONE')
        else:
            for i_2 in dic_month:
                if i_2 in i :
                    if i[-8] != ' ':
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month[i_2] + '-' + i[-8] + i[-7])
                    else:
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month[i_2] + '-0' + i[-7])
    return temp_list
def normalization_date_2(list_need_to_normalization):  #  有的月份是簡寫
    temp_list = []
    for i in list_need_to_normalization:
        if i == 'NONE':
            temp_list.append('NONE')
        else:
            for i_2 in dic_month_2:
                if i_2 in i :
                    if i[-8] != ' ':
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month_2[i_2] + '-' + i[-8] + i[-7])
                    else:
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month_2[i_2] + '-0' + i[-7])
    return temp_list
def normalization_month(list_need_to_normalization):
    temp_list = []
    for i in list_need_to_normalization:
        if i != 'NONE':
            temp_list_2 = []
            for i_2 in i:
                temp_list_2.append(dic_month[i_2])
            temp_list.append(temp_list_2)
        else:
            temp_list.append('NONE')
    return temp_list
def normalization_month_2(list_need_to_normalization):
    temp_list = []
    for i in list_need_to_normalization:
        if i != 'NONE':
            temp_list_2 = []
            for i_2 in i:
                temp_list_2.append(dic_month_2[i_2])
            temp_list.append(temp_list_2)
        else:
            temp_list.append('NONE')
    return temp_list
def list_to_list(big_list, small_list, regex,  words_need_to_delete):  #  用來切片 list
    for i in big_list:
        m = re.findall(regex, i)
        if m != []:
            temp_m = m[0].replace(words_need_to_delete, '')
            small_list.append(temp_m)
        else:
            small_list.append('NONE')
inventors_list = []  #  ---> Inventors
inventors_name_list = []
inventors_city_list = []
inventors_country_list = []
regex = r"^Inventors:\s.+"  # 利用正規表達對比
for i in patent_detail_list:
    m = re.findall(regex, i)
    if m != []:
        temp_m = m[0].replace('Inventors: ', '')  #  把小標題取代掉
        inventors_list.append(temp_m.replace('), ', ')@@@').split('@@@'))  #  建立 [['a', 'b', 'c'], ['d', 'e', 'f'], ...] @@@是切片符號
    else:
        inventors_list.append('NONE')
for i in inventors_list:
    if i != 'NONE':
        temp_list = []
        temp_list_2 = []
        temp_list_3 = []
        for i_2 in i:
            temp_list.append(i_2.rsplit(' (', 1)[0])
            temp_list_2.append(i_2.rsplit(', ', 1)[0].rsplit(' (', 1)[-1])
            temp_list_3.append(i_2.rsplit(', ', 1)[-1].replace(')', ''))
        inventors_name_list.append(temp_list)
        inventors_city_list.append(temp_list_2)
        inventors_country_list.append(temp_list_3)
    else:
        inventors_name_list.append('NONE')
        inventors_city_list.append('NONE')
        inventors_country_list.append('NONE')
family_id_list = []
applNo_list = []
filed_list = []
pct_filed_list = []
pctNo_list = []
pct371_date_list = []  #  美國專利法第 371 條規範國際申請案 PCT 進入美國國家階段的程序
pct_pubNo_list = []
pct_pub_date_list = []
list_to_list(patent_detail_list, family_id_list, r"Family ID:\s.+", 'Family ID: ')
list_to_list(patent_detail_list, applNo_list, r"Appl\. No\.:\s.+", 'Appl. No.: ')
list_to_list(patent_detail_list, filed_list, r"Filed:\s.+", 'Filed: ')
filed_list = normalization_date(filed_list)
list_to_list(patent_detail_list, pct_filed_list, r"PCT Filed:\s.+", 'PCT Filed: ')
pct_filed_list = normalization_date(pct_filed_list)
list_to_list(patent_detail_list, pctNo_list, r"PCT No\.:\s.+", 'PCT No.: ')
list_to_list(patent_detail_list, pct371_date_list, r"371\(c\)\(1\),\(2\),\(4\) Date:\s.+", '371(c)(1),(2),(4) Date: ')
pct371_date_list = normalization_date(pct371_date_list)
list_to_list(patent_detail_list, pct_pubNo_list, r"PCT Pub\. No\.:\s.+", 'PCT Pub. No.: ')
list_to_list(patent_detail_list, pct_pub_date_list, r"PCT Pub\. Date:\s.+", 'PCT Pub. Date: ')
pct_pub_date_list = normalization_date(pct_pub_date_list)
applicant_list = []  #  ---> Applicant
applicant_name_list = []
applicant_city_list = []
applicant_state_list = []
applicant_country_list = []
regex = r"Applicant:\nName City State Country Type\n\n(.*\n)*[A-Z]{2}\n"
for i in patent_detail_list:
    m = re.search(regex, i)
    if m != None:
        temp_m = (m.group().replace('Applicant:\nName City State Country Type\n\n', ''))[0:-1].split('\n')
        applicant_list.append(temp_m)
    else:
        applicant_list.append('NONE')
for i in applicant_list:
    if i != 'NONE':
        x = len(i)//4
        applicant_name_list.append(i[ :x])
        applicant_city_list.append(i[x:x*2])
        applicant_state_list.append(i[x*2:x*3])
        applicant_country_list.append(i[x*3: ])
    else:
        applicant_name_list.append('NONE')
        applicant_city_list.append('NONE')
        applicant_state_list.append('NONE')
        applicant_country_list.append('NONE')
assignee_list = []  #  ---> Assignee
assignee_name_list = []
assignee_city_list = []
assignee_country_list = []
regex = r"Assignee: (.*\n)*.*\(.*[A-Z]{2}\)"
for i in patent_detail_list:
    m = re.search(regex, i)
    if m != None:
        temp_m = (m.group().replace('Assignee: ', '')).split('\n')
        assignee_list.append(temp_m)
    else:
        assignee_list.append('NONE')
for i in assignee_list:
    if i != 'NONE':
        temp_list = []
        temp_list_2 = []
        temp_list_3 = []
        for i_2 in i:
            temp_list.append(i_2.split(' (', 1)[0])
            temp_list_2.append(i_2.rsplit(', ', 1)[0].rsplit('(', 1)[1])
            if 'N/A' not in i_2.split(' (', 1)[1]:
                temp_list_3.append(i_2.split(' (', 1)[1][-3:-1])
            else:
                temp_list_3.append('N/A')
        assignee_name_list.append(temp_list)
        assignee_city_list.append(temp_list_2)
        assignee_country_list.append(temp_list_3)
    else:
        assignee_name_list.append('NONE')
        assignee_city_list.append('NONE')
        assignee_country_list.append('NONE')
#  Prior Publication
patent_priorPublication_detail_list = combined_list_1[6] + combined_list_2[6] + combined_list_3[6] + combined_list_4[6]
prior_name_list = []  #  先期公開資料，包含編號及日期。
prior_date_list = []
list_to_list(patent_priorPublication_detail_list, prior_name_list, r"[A-Z]{2} \d* [A-Z][0-9]", '')
list_to_list(patent_priorPublication_detail_list, prior_date_list, r"[A-Z][a-z]{2} [0-9]+, [0-9]{4}", '')
prior_date_list = normalization_date_2(prior_date_list)
#  不會用到的資料先不用節省空間
patent_related_us_list = combined_list_1[7] + combined_list_2[7] + combined_list_3[7] + combined_list_4[7]
#  不會用到的資料先不用節省空間
patent_foreignApplicationPriority_list = combined_list_1[8] + combined_list_2[8] + combined_list_3[8] + combined_list_4[8]
#  分割成多項 Id Month Year Name
patent_referencesCited_us_documents_list = combined_list_1[9] + combined_list_2[9] + combined_list_3[9] + combined_list_4[9]
referencesCited_us_list = []
referencesCited_us_month_list = []
referencesCited_us_year_list = []
referencesCited_us_name_list = []
for i in patent_referencesCited_us_documents_list:
    if i != 'NONE':
        temp_list = []
        temp_list_2 = []
        temp_list_3 = []
        temp_list_4 = []
        for i_2 in i.split('\n'):
            temp_list.append(i_2.split(' ', 1)[0])
            temp_list_2.append(i_2.split(' ', 1)[1].split(' ', 2)[0])
            temp_list_3.append(i_2.split(' ', 1)[1].split(' ', 2)[1])
            temp_list_4.append(i_2.split(' ', 1)[1].split(' ', 2)[2])
        referencesCited_us_list.append(temp_list)
        referencesCited_us_month_list.append(temp_list_2)
        referencesCited_us_year_list.append(temp_list_3)
        referencesCited_us_name_list.append(temp_list_4)
    else:
        referencesCited_us_list.append('NONE')
        referencesCited_us_month_list.append('NONE')
        referencesCited_us_year_list.append('NONE')
        referencesCited_us_name_list.append('NONE')
referencesCited_us_month_list = normalization_month(referencesCited_us_month_list)
referencesCited_us_etAl_list = []
referencesCited_us_n_etAl_list = []
for i in referencesCited_us_name_list:
    if i != 'NONE':
        temp_list = []
        temp_list_2 = []
        for i_2 in i:
            if 'et al.' in i_2:
                temp_list.append(i_2)
                temp_list_2.append('NONE')
            else:
                temp_list.append('NONE')
                temp_list_2.append(i_2)
        referencesCited_us_etAl_list.append(temp_list)
        referencesCited_us_n_etAl_list.append(temp_list_2)
    else:
        referencesCited_us_etAl_list.append('NONE')
        referencesCited_us_n_etAl_list.append('NONE')
#  分割成多項 Id Month Year Database
patent_referencesCited_foreign_documents_list = combined_list_1[10] + combined_list_2[10] + combined_list_3[10] + combined_list_4[10]
referencesCited_f_list = []
referencesCited_f_month_list = []
referencesCited_f_year_list = []
referencesCited_f_dataBaseName_list = []
for i in patent_referencesCited_foreign_documents_list:
    if i != 'NONE':
        temp_list = []
        temp_list_2 = []
        temp_list_3 = []
        temp_list_4 = []
        for i_2 in i.split('\n'):
            temp_list.append(i_2.rsplit(' ', 3)[0])
            temp_list_2.append(i_2.split(' ')[-3])
            temp_list_3.append(i_2.split(' ')[-2])
            temp_list_4.append(i_2.split(' ')[-1])
        referencesCited_f_list.append(temp_list)
        referencesCited_f_month_list.append(temp_list_2)
        referencesCited_f_year_list.append(temp_list_3)
        referencesCited_f_dataBaseName_list.append(temp_list_4)
    else:
        referencesCited_f_list.append('NONE')
        referencesCited_f_month_list.append('NONE')
        referencesCited_f_year_list.append('NONE')
        referencesCited_f_dataBaseName_list.append('NONE')
referencesCited_f_month_list = normalization_month_2(referencesCited_f_month_list)
#  分割成多項 ipc class subclass scetion subgroup date
patent_ipc_list = combined_list_1[11] + combined_list_2[11] + combined_list_3[11] + combined_list_4[11]
ipc_list = []
ipc_section_list = []
ipc_class_list = []
ipc_subclass_list = []
ipc_subgroup_list = []
ipc_date_list = []
for i in patent_ipc_list:
    if i != 'NONE':
        temp_list = []
        temp_list_2 = []
        temp_list_3 = []
        temp_list_4 = []
        temp_list_5 = []
        ipc_list.append(i.split('; '))
        for i_2 in i.split('; '):
            temp_list.append(i_2.split(' ')[0][0])
            temp_list_2.append(i_2.split(' ')[0][:-1])
            temp_list_3.append(i_2.split(' ')[0])
            temp_list_4.append(i_2.split(' ')[1])
            if '()' not in i_2:
                temp_list_5.append(i_2.rsplit(' ', 1)[1].replace('(', '').replace(')', '')[:4] + '-' + i_2.rsplit(' ', 1)[1].replace('(', '').replace(')', '')[4:6] + '-' + i_2.rsplit(' ', 1)[1].replace('(', '').replace(')', '')[6:8])
            else:
                temp_list_5.append('N/A')
        ipc_section_list.append(temp_list)
        ipc_class_list.append(temp_list_2)
        ipc_subclass_list.append(temp_list_3)
        ipc_subgroup_list.append(temp_list_4)
        ipc_date_list.append(temp_list_5)
    else:
        ipc_list.append('NONE')
        ipc_section_list.append('NONE')
        ipc_class_list.append('NONE')
        ipc_subclass_list.append('NONE')
        ipc_subgroup_list.append('NONE')
        ipc_date_list.append('NONE')
#  錯誤發生在
patent_err_list_thread = combined_list_1[12] + combined_list_2[12] + combined_list_3[12] + combined_list_4[12]
if len(patent_err_list_thread) < 1:
    print('Congratulations!!! No error occured')
else:
    print('Error at: ')
    print(patent_err_list_thread)
#-----------------------------------------------------------------------------
#  data frame
#-----------------------------------------------------------------------------
#  客製index
def un_zip_index_list(aim_list, index_list_need_to_unzip):
    temp_list = []
    num = 0
    for i in aim_list:
        if i != 'NONE':
            num_2 = 0
            while num_2 < len(i):
                temp_list.append(index_list_need_to_unzip[num])
                num_2 += 1
            num +=  1
        else:
            temp_list.append(index_list_need_to_unzip[num])
            num +=  1
    return temp_list
#  [[],[],[],....[]] ---> []
def un_zip_list(list_need_to_unzip):
    temp_list = []
    for i in list_need_to_unzip:
        if i != 'NONE':
            for i_2 in i:
                temp_list.append(i_2)
        else:
            temp_list.append(i)
    return temp_list
detail_data = pandas.DataFrame({
    'Title' : patent_title_list,
    'Abstract' : patent_abstract_list,
    'et al.' : etAl,
    'n_et al.' : n_etAl,
    'Date' : full_date,
    'Year' : year_date,
    'Family ID' : family_id_list,
    'Appl. No.' : applNo_list,
    'Filed' : filed_list,
    'PCT Filed' : pct_filed_list,
    'PCT No.' : pctNo_list,
    '371(c)(1),(2),(4) Date' : pct371_date_list,
    'PCT Pub. No.' : pct_pubNo_list,
    'PCT Pub. Date' : pct_pub_date_list,
    'Prior Publication Data' : prior_name_list,
    'Prior Publication Data Date' : prior_date_list
}, index = patent_index_list)
inventors_data = pandas.DataFrame({
    'Inventors Name' : un_zip_list(inventors_name_list),
    'Inventors City' : un_zip_list(inventors_city_list),
    'Inventors Country' : un_zip_list(inventors_country_list)
}, index =  un_zip_index_list(inventors_name_list, patent_index_list))
applicant_data = pandas.DataFrame({
    'Applicant Name' : un_zip_list(applicant_name_list),
    'Applicant City' : un_zip_list(applicant_city_list),
    'Applicant State' : un_zip_list(applicant_state_list),
    'Applicant Country' : un_zip_list(applicant_country_list)
}, index =  un_zip_index_list(applicant_name_list, patent_index_list))
assignee_data = pandas.DataFrame({
    'Assignee Name' : un_zip_list(assignee_name_list),
    'Assignee City' : un_zip_list(assignee_city_list),
    'Assignee Country' : un_zip_list(assignee_country_list)
}, index =  un_zip_index_list(assignee_name_list, patent_index_list))
referencesCited_us_data = pandas.DataFrame({
    'References Cited U.S. Patent' : un_zip_list(referencesCited_us_list),
    'References Cited U.S. Month' : un_zip_list(referencesCited_us_month_list),
    'References Cited U.S.Year' : un_zip_list(referencesCited_us_year_list),
    'References Cited U.S. et al.' : un_zip_list(referencesCited_us_etAl_list),
    'References Cited U.S. n_et al' : un_zip_list(referencesCited_us_n_etAl_list)
}, index =  un_zip_index_list(referencesCited_us_list, patent_index_list))
referencesCited_f_data = pandas.DataFrame({
    'References Cited Foreign Patent' : un_zip_list(referencesCited_f_list),
    'References Cited Foreign Month' : un_zip_list(referencesCited_f_month_list),
    'References Cited Foreign Year' : un_zip_list(referencesCited_f_year_list),
    'References Cited Foreign DB' : un_zip_list(referencesCited_f_dataBaseName_list)
}, index =  un_zip_index_list(referencesCited_f_list, patent_index_list))
ipc_data = pandas.DataFrame({
    'IPC Section' : un_zip_list(ipc_section_list),
    'IPC Class' : un_zip_list(ipc_class_list),
    'IPC Subclass' : un_zip_list(ipc_subclass_list),
    'IPC Subgroup' : un_zip_list(ipc_subgroup_list),
    'IPC Date' : un_zip_list(ipc_date_list)
}, index =  un_zip_index_list(ipc_section_list, patent_index_list))
#  記得先安裝 openpyxl
with pandas.ExcelWriter(file_path + '/uspto_data/data.xlsx', engine = 'openpyxl') as writer:
    detail_data.to_excel(writer, sheet_name = 'Detail')
    inventors_data.to_excel(writer, sheet_name = 'Inventors')
    applicant_data.to_excel(writer, sheet_name = 'Applicant')
    assignee_data.to_excel(writer, sheet_name = 'Assignee')
    referencesCited_us_data.to_excel(writer, sheet_name = 'References Cited U.S.')
    referencesCited_f_data.to_excel(writer, sheet_name = 'References Cited Forigen')
    ipc_data.to_excel(writer, sheet_name = 'Ipc')