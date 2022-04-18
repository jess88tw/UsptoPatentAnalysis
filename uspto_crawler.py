#-----------------------------------------------------------------------------
#    IMPORT
#-----------------------------------------------------------------------------
import sys
import urllib
import time
import bs4
from selenium import webdriver
import urllib.request as request
import ssl
import re
import os
import csv
import requests
import shutil
ssl._create_default_https_context = ssl._create_unverified_context
#-----------------------------------------------------------------------------
#    FILEPATE IS EXSIT
#-----------------------------------------------------------------------------
print('You wanna check the folder ?, [PLEASE TYPE Y or N]')
wanna = input()

if wanna == 'Y':
    print('Please input filepath :')
    filepath = input()

    regex = r"\/[A-Z,a-z,0-9]+$"

    m = re.findall(regex, str(filepath))

    if m != []:
        if os.path.isdir(''+ str(filepath) +'/uspto'):
            print('Updating .....')
            shutil.rmtree(''+ str(filepath) +'/uspto')
            os.makedirs(''+ str(filepath) +'/uspto')
            os.makedirs(''+ str(filepath) +'/uspto/Abstract')
            os.makedirs(''+ str(filepath) +'/uspto/csv')
            os.makedirs(''+ str(filepath) +'/uspto/Date')
            os.makedirs(''+ str(filepath) +'/uspto/Detail')
            os.makedirs(''+ str(filepath) +'/uspto/eror')
            os.makedirs(''+ str(filepath) +'/uspto/et al.')
            os.makedirs(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data')
            os.makedirs(''+ str(filepath) +'/uspto/NO.')
            os.makedirs(''+ str(filepath) +'/uspto/Prior_Publication_Data')
            os.makedirs(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents')
            os.makedirs(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents')
            os.makedirs(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents')
            os.makedirs(''+ str(filepath) +'/uspto/secStep')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/371Date')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Appl_No')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/City')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/Country')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/Name')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/State')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Assignee')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Family_ID')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Filed')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Inventors')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors_Detail')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_Filed')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_No')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No')
            os.makedirs(''+ str(filepath) +'/uspto/Title')
            os.makedirs(''+ str(filepath) +'/uspto/WebHtml')
            os.makedirs(''+ str(filepath) +'/uspto/Total')
            os.makedirs(''+ str(filepath) +'/uspto/IPC')
            os.makedirs(''+ str(filepath) +'/uspto/IPC/IPC_Detail')
        else:
            print('Loading data .....')
            os.makedirs(''+ str(filepath) +'/uspto')
            os.makedirs(''+ str(filepath) +'/uspto/Abstract')
            os.makedirs(''+ str(filepath) +'/uspto/csv')
            os.makedirs(''+ str(filepath) +'/uspto/Date')
            os.makedirs(''+ str(filepath) +'/uspto/Detail')
            os.makedirs(''+ str(filepath) +'/uspto/eror')
            os.makedirs(''+ str(filepath) +'/uspto/et al.')
            os.makedirs(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data')
            os.makedirs(''+ str(filepath) +'/uspto/NO.')
            os.makedirs(''+ str(filepath) +'/uspto/Prior_Publication_Data')
            os.makedirs(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents')
            os.makedirs(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents')
            os.makedirs(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents')
            os.makedirs(''+ str(filepath) +'/uspto/secStep')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/371Date')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Appl_No')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/City')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/Country')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/Name')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Applicant/State')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Assignee')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Family_ID')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Filed')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Inventors')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors_Detail')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_Filed')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_No')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date')
            os.makedirs(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No')
            os.makedirs(''+ str(filepath) +'/uspto/Title')
            os.makedirs(''+ str(filepath) +'/uspto/WebHtml')
            os.makedirs(''+ str(filepath) +'/uspto/Total')
            os.makedirs(''+ str(filepath) +'/uspto/IPC')
            os.makedirs(''+ str(filepath) +'/uspto/IPC/IPC_Detail')
    else:
        print('Please input the right filepath :')
        print('Ex : /Users/jess88tw/MyPython/data')
        sys.exit()
elif wanna == 'N':
    print('Ok, next')
else:
    print('[PLEASE TYPE Y or N] , and try again')
#-----------------------------------------------------------------------------
#    LINE NOTIFY DEF
#-----------------------------------------------------------------------------
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

token = 'ext70taJ5hkZa6JSLHq4W8CB4Re6tsBvF1QbVNOVRQo'
#-----------------------------------------------------------------------------
#     DICTIONARY
#-----------------------------------------------------------------------------
dic_type = {
'TYPE_ER' : '0', 
'TYPE_01' : '0', 'TYPE_02' : '0', 'TYPE_03' : '0', 'TYPE_04' : '0', 'TYPE_05' : '0', 'TYPE_06' : '0', 'TYPE_07' : '0', 'TYPE_08' : '0', 
'TYPE_09' : '0', 'TYPE_10' : '0', 'TYPE_11' : '0', 'TYPE_12' : '0', 'TYPE_13' : '0', 'TYPE_14' : '0', 'TYPE_15' : '0', 'TYPE_16' : '0', 
'TYPE_17' : '0', 'TYPE_18' : '0', 'TYPE_19' : '0', 'TYPE_20' : '0', 'TYPE_21' : '0', 'TYPE_22' : '0', 'TYPE_23' : '0', 'TYPE_24' : '0', 
'TYPE_25' : '0', 'TYPE_26' : '0', 'TYPE_27' : '0', 'TYPE_28' : '0', 'TYPE_29' : '0', 'TYPE_30' : '0', 'TYPE_31' : '0', 'TYPE_32' : '0',
'TYPE_33' : '0', 'TYPE_34' : '0', 'TYPE_35' : '0', 'TYPE_36' : '0', 'TYPE_37' : '0', 'TYPE_38' : '0', 'TYPE_39' : '0', 'TYPE_40' : '0', 
'TYPE_41' : '0', 'TYPE_42' : '0', 'TYPE_43' : '0', 'TYPE_44' : '0', 'TYPE_45' : '0', 'TYPE_46' : '0', 'TYPE_47' : '0', 'TYPE_48' : '0', 
'TYPE_49' : '0', 'TYPE_50' : '0', 'TYPE_51' : '0', 'TYPE_52' : '0', 'TYPE_53' : '0', 'TYPE_54' : '0', 'TYPE_55' : '0', 'TYPE_56' : '0', 
'TYPE_57' : '0', 'TYPE_58' : '0', 'TYPE_59' : '0', 'TYPE_60' : '0', 'TYPE_61' : '0', 'TYPE_62' : '0', 'TYPE_63' : '0', 'TYPE_64' : '0', 
}

dic_detail = {
'Inventors_Yes' : '0', 'Inventors_None' : '0', 
'Family_ID_Yes' : '0', 'Family_ID_None' : '0', 
'Appl_No_Yes' : '0', 'Appl_No_None' : '0', 
'Filed_Yes' : '0', 'Filed_None' : '0', 
'Pct_Filed_Yes' : '0', 'Pct_Filed_None' : '0', 
'Pct_No_Yes' : '0', 'Pct_No_None' : '0', 
'SDate_Yes' : '0', 'SDate_None' : '0', 
'Pct_Pub_No_Yes' : '0', 'Pct_Pub_No_None' : '0', 
'Pct_Pub_Date_Yes' : '0', 'Pct_Pub_Date_None' : '0', 
'Applicant_Yes' : '0', 'Applicant_None' : '0', 
'Assignee_Yes' : '0', 'Assignee_None' : '0'
}
#-----------------------------------------------------------------------------
#     START SPIDER ?
#-----------------------------------------------------------------------------
print('Are you sure you want to start the spider ? , [PLEASE TYPE Y or N]')
DoIt = (input())
if DoIt == 'Y':
#-----------------------------------------------------------------------------
#     CHROME DRIVER
#-----------------------------------------------------------------------------
    driver_path ='/Users/jess88tw/webdriver/chromedriver'
    driver = webdriver.Chrome(driver_path)
    print('url ?')
    url = ''+ input() +''
    # url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=4&f=S&l=50&d=PTXT&p=1&S1=%22Umbilical+Cord+Blood+Stem+Cells%22&Query=%22Umbilical+Cord+Blood+Stem+Cells%22'   #Umbilical Cord Blood Stem Cells
    # url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=15&f=S&l=50&co1=AND&d=PTXT&s1=%22Peripheral+Blood+Stem+Cells%22&Query=%22Peripheral+Blood+Stem+Cells%22'  #Peripheral Blood Stem Cells
    # url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&RS=%22Adipose-+derived+Stem+Cells%22&Query=%22Adipose-+derived+Stem+Cells%22&TD=915&Srch1=%22Adipose-+derived+Stem+Cells%22&StartAt=Jump+To&StartNum=1'   #Adipose-derived Stem Cells
    driver.get(url)
#-----------------------------------------------------------------------------
#     WRITE HTML
#-----------------------------------------------------------------------------
    TOTAl = int(driver.find_element_by_xpath("/html/body/i/strong[3]").text)

    with open(''+ str(filepath) +'/uspto/Total/Total.txt', mode = 'w',encoding = 'utf=8') as pagefile :
        print(TOTAl, file = pagefile)
        
    print('TOTAL :', TOTAl)

    if (TOTAl % 50) == 0:
        x = (TOTAl // 50) + 1
    else :
        x = (TOTAl // 50) + 2
    
    message = 'All pages : '+ str(x-1) +''
    lineNotifyMessage(token, message)

    print('第幾頁？')
    pages = int(input())
    while pages < x:
        print('PAGE', pages)
        title = 2
        number = 1

        body = driver.find_element_by_tag_name("body")
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[4]/a').click()

        while number < 51 :
            current_number = number + (50 * (pages - 1))
            current_title = title - 1
            print('TITLE', current_title)
            
            current_url = driver.current_url
            source = current_url
            headerinfo = request.Request(source, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'})

            with request.urlopen(headerinfo) as page:
                try :
                    pagedata = page.read().decode('utf-8')
                except ConnectionResetError :
                    driver.refresh()
                    time.sleep(1.5)
                    pagedata = page.read().decode('utf-8')

            with open(''+ str(filepath) +'/uspto/WebHtml/' + str(current_number) + '.txt', mode = 'w',encoding = 'utf=8') as pagefile :
                print(pagedata, file = pagefile)

            sys.path.append(''+ str(filepath) +'/uspto/WebHtml/')
            soup = bs4.BeautifulSoup(pagedata,'html.parser')

            with open(''+ str(filepath) +'/uspto/WebHtml/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as pagefile :
                print(soup.prettify(), file = pagefile)

            time.sleep(1.5)
#-----------------------------------------------------------------------------
#     CLASSIFY
#-----------------------------------------------------------------------------
            with open(''+ str(filepath) +'/uspto/WebHtml/' + str(current_number) + '.txt', mode = 'r', encoding = 'utf = 8') as f:
                data = f.read()

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
#-----------------------------------------------------------------------------
#     C4 取 0
#-----------------------------------------------------------------------------
                if (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 1')
                    dic_type['TYPE_01'] = int(dic_type['TYPE_01']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[9]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 2')
                    dic_type['TYPE_02'] = int(dic_type['TYPE_02']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 3')
                    dic_type['TYPE_03'] = int(dic_type['TYPE_03']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 4')
                    dic_type['TYPE_04'] = int(dic_type['TYPE_04']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)
#-----------------------------------------------------------------------------
#     C4 取 1
#-----------------------------------------------------------------------------
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 5')
                    dic_type['TYPE_05'] = int(dic_type['TYPE_05']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 6')
                    dic_type['TYPE_06'] = int(dic_type['TYPE_06']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 7')
                    dic_type['TYPE_07'] = int(dic_type['TYPE_07']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 8')
                    dic_type['TYPE_08'] = int(dic_type['TYPE_08']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 9')
                    dic_type['TYPE_09'] = int(dic_type['TYPE_09']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 10')
                    dic_type['TYPE_10'] = int(dic_type['TYPE_10']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 11')
                    dic_type['TYPE_11'] = int(dic_type['TYPE_11']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 12')
                    dic_type['TYPE_12'] = int(dic_type['TYPE_12']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 13')
                    dic_type['TYPE_13'] = int(dic_type['TYPE_13']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 14')
                    dic_type['TYPE_14'] = int(dic_type['TYPE_14']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 15')
                    dic_type['TYPE_15'] = int(dic_type['TYPE_15']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 16')
                    dic_type['TYPE_16'] = int(dic_type['TYPE_16']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 17')
                    dic_type['TYPE_17'] = int(dic_type['TYPE_17']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[8]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 18')
                    dic_type['TYPE_18'] = int(dic_type['TYPE_18']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 19')
                    dic_type['TYPE_19'] = int(dic_type['TYPE_19']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 20')
                    dic_type['TYPE_20'] = int(dic_type['TYPE_20']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)
#-----------------------------------------------------------------------------
#     C4 取 2
#-----------------------------------------------------------------------------
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 21')
                    dic_type['TYPE_21'] = int(dic_type['TYPE_21']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 22')
                    dic_type['TYPE_22'] = int(dic_type['TYPE_22']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 != []) :
                    print('TYPE 23')
                    dic_type['TYPE_23'] = int(dic_type['TYPE_23']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 != []) and (m7 == []) :
                    print('TYPE 24')
                    dic_type['TYPE_24'] = int(dic_type['TYPE_24']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 25')
                    dic_type['TYPE_25'] = int(dic_type['TYPE_25']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 26')
                    dic_type['TYPE_26'] = int(dic_type['TYPE_26']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 27')
                    dic_type['TYPE_27'] = int(dic_type['TYPE_27']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 28')
                    dic_type['TYPE_28'] = int(dic_type['TYPE_28']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 29')
                    dic_type['TYPE_29'] = int(dic_type['TYPE_29']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)
                    
                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 30')
                    dic_type['TYPE_30'] = int(dic_type['TYPE_30']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 31')
                    dic_type['TYPE_31'] = int(dic_type['TYPE_31']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 32')
                    dic_type['TYPE_32'] = int(dic_type['TYPE_32']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 33')
                    dic_type['TYPE_33'] = int(dic_type['TYPE_33']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 34')
                    dic_type['TYPE_34'] = int(dic_type['TYPE_34']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 35')
                    dic_type['TYPE_35'] = int(dic_type['TYPE_35']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 36')
                    dic_type['TYPE_36'] = int(dic_type['TYPE_36']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 37')
                    dic_type['TYPE_37'] = int(dic_type['TYPE_37']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 38')
                    dic_type['TYPE_38'] = int(dic_type['TYPE_38']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 39')
                    dic_type['TYPE_39'] = int(dic_type['TYPE_39']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 40')
                    dic_type['TYPE_40'] = int(dic_type['TYPE_40']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 41')
                    dic_type['TYPE_41'] = int(dic_type['TYPE_41']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[7]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 42')
                    dic_type['TYPE_42'] = int(dic_type['TYPE_42']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 43')
                    dic_type['TYPE_43'] = int(dic_type['TYPE_43']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 44')
                    dic_type['TYPE_44'] = int(dic_type['TYPE_44']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)
#-----------------------------------------------------------------------------
#     C4 取 3
#-----------------------------------------------------------------------------
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 45')
                    dic_type['TYPE_45'] = int(dic_type['TYPE_45']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 46')
                    dic_type['TYPE_46'] = int(dic_type['TYPE_46']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 != []) :
                    print('TYPE 47')
                    dic_type['TYPE_47'] = int(dic_type['TYPE_47']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 != []) and (m7 == []) :
                    print('TYPE 48')
                    dic_type['TYPE_48'] = int(dic_type['TYPE_48']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 49')
                    dic_type['TYPE_49'] = int(dic_type['TYPE_49']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 50')
                    dic_type['TYPE_50'] = int(dic_type['TYPE_50']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 != []) :
                    print('TYPE 51')
                    dic_type['TYPE_51'] = int(dic_type['TYPE_51']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 != []) and (m6 == []) and (m7 == []) :
                    print('TYPE 52')
                    dic_type['TYPE_52'] = int(dic_type['TYPE_52']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 53')
                    dic_type['TYPE_53'] = int(dic_type['TYPE_53']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 54')
                    dic_type['TYPE_54'] = int(dic_type['TYPE_54']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 55')
                    dic_type['TYPE_55'] = int(dic_type['TYPE_55']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 != []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 56')
                    dic_type['TYPE_56'] = int(dic_type['TYPE_56']) + 1
                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)


                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 57')
                    dic_type['TYPE_57'] = int(dic_type['TYPE_57']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[6]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 58')
                    dic_type['TYPE_58'] = int(dic_type['TYPE_58']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 59')
                    dic_type['TYPE_59'] = int(dic_type['TYPE_59']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 != []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 60')
                    dic_type['TYPE_60'] = int(dic_type['TYPE_60']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)
#-----------------------------------------------------------------------------
#     C4 取 4
#-----------------------------------------------------------------------------
                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 61')
                    dic_type['TYPE_61'] = int(dic_type['TYPE_61']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[5]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 != []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 62')
                    dic_type['TYPE_62'] = int(dic_type['TYPE_62']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 != []) :
                    print('TYPE 63')
                    dic_type['TYPE_63'] = int(dic_type['TYPE_63']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print(driver.find_element_by_xpath("/html/body/table[4]").text, file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)

                elif (m != []) and (m2 == []) and (m3 == []) and (m4 == []) and (m5 == []) and (m6 == []) and (m7 == []) :
                    print('TYPE 64')
                    dic_type['TYPE_64'] = int(dic_type['TYPE_64']) + 1

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]").text, file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[1]").text, file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text, file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print(driver.find_element_by_xpath("/html/body/font").text, file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print(driver.find_element_by_xpath("/html/body/p[1]").text, file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print(driver.find_element_by_xpath("/html/body/table[3]").text, file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('None', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('None', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('None', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('None', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('None', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        try :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[3]/td[2]").text, file = IPCfile)
                        except :
                            print(driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]").text, file = IPCfile)
#-----------------------------------------------------------------------------
#     EROR
#-----------------------------------------------------------------------------
                else:
                    dic_type['TYPE_ER'] = int(dic_type['TYPE_ER']) + 1
                    with open(''+ str(filepath) +'/uspto/eror/eror.txt', mode = 'a', encoding = 'utf = 8') as eroefile :
                        print(current_number, file = eroefile)

                    with open(''+ str(filepath) +'/uspto/NO./NO.txt', mode = 'a', encoding = 'utf = 8') as NOfile :
                        print('EROR', file = NOfile)

                    with open(''+ str(filepath) +'/uspto/et al./et_al.txt', mode = 'a', encoding = 'utf = 8') as et_alfile :
                        print('EROR', file = et_alfile)

                    with open(''+ str(filepath) +'/uspto/Date/Date.txt', mode = 'a', encoding = 'utf = 8') as Datefile :
                        print('EROR', file = Datefile)

                    with open(''+ str(filepath) +'/uspto/Title/Title.txt', mode = 'a', encoding = 'utf = 8') as Titlefile :
                        print('EROR', file = Titlefile)

                    with open(''+ str(filepath) +'/uspto/Abstract/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Abstractfile :
                        print('EROR', file = Abstractfile)

                    with open(''+ str(filepath) +'/uspto/Detail/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Detailfile :
                        print('EROR', file = Detailfile)

                    with open(''+ str(filepath) +'/uspto/Prior_Publication_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Prior_Publication_Datafile :
                        print('EROR', file = Prior_Publication_Datafile)

                    with open(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Related_US_Patent_Documentsfile :
                        print('EROR', file = Related_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as Foreign_Application_Priority_Datafile :
                        print('EROR', file = Foreign_Application_Priority_Datafile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_US_Patent_Documentsfile :
                        print('EROR', file = References_Cited_US_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as References_Cited_Foreign_Patent_Documentsfile :
                        print('EROR', file = References_Cited_Foreign_Patent_Documentsfile)

                    with open(''+ str(filepath) +'/uspto/IPC/' + str(current_number) + '.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                        print('EROR', file = IPCfile)
#-----------------------------------------------------------------------------
#     CLICK
#-----------------------------------------------------------------------------
            if pages < 2 :
                if number < 2 :
                    message = 'Spider is in page '+ str(pages) +' now'
                    lineNotifyMessage(token, message)
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[3]').click()
                elif 1 < number < 50 :
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[4]').click()
                else :
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[2]').click()

            elif 1 < pages < (x - 1) :
                if number < 2 :
                    message = 'Spider is in page '+ str(pages) +' now'
                    lineNotifyMessage(token, message)
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[4]').click()
                elif 1 < number < 50 :
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[5]').click()
                else :
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[3]').click()

            else :
                backNum = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/strong/font").text
                frontNum = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/font[1]/strong").text
                num = int(backNum) - int(frontNum)

                if number < 2 :
                    message = 'Spider is in page '+ str(pages) +' now'
                    lineNotifyMessage(token, message)
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[3]').click()
                elif (1 < number) and (num != 0) :
                    driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr[2]/td/a[4]').click()
                else :
                    break
            title = 1 + title
            number = 1 + number
            time.sleep(2)

        pages = pages + 1
#-----------------------------------------------------------------------------
#     CLOSE DRIVER
#-----------------------------------------------------------------------------
    driver.quit()
    print(dic_type)
#-----------------------------------------------------------------------------
#     CLASSIFY DETAIL
#-----------------------------------------------------------------------------
    file_Number = 1
    while file_Number < (TOTAl + 1) :
        with open(''+ str(filepath) +'/uspto/Detail/' + str(file_Number) + '.txt', mode = 'r', encoding = 'utf = 8') as Detailfile :
            dData = Detailfile.read()

            regex = r"^Inventors:\s.+"
            regex2 = r"Family ID:\s.+"
            regex3 = r"Appl\. No\.:\s.+"
            regex4 = r"Filed:\s.+"
            regex5 = r"PCT Filed:\s.+"
            regex6 = r"PCT No\.:\s.+"
            regex7 = r"371\(c\)\(1\),\(2\),\(4\) Date:\s.+"
            regex8 = r"PCT Pub\. No\.:\s.+"
            regex9 = r"PCT Pub\. Date:\s.+"
            regex10_1 = r"Applicant:"
            regex10_2 = (r"Applicant:\n"
                r"Name City State Country Type\n\n"
                r"(.+\n)*..$")
            regex11_1 = r"Assignee:"
            regex11_2 = r"Assignee:(.*\n)*.*\)$"

            test_str = (dData)

            m = re.findall(regex, test_str)
            m2 = re.findall(regex2, test_str)
            m3 = re.findall(regex3, test_str)
            m4 = re.findall(regex4, test_str)
            m5 = re.findall(regex5, test_str)
            m6 = re.findall(regex6, test_str)
            m7 = re.findall(regex7, test_str)
            m8 = re.findall(regex8, test_str)
            m9 = re.findall(regex9, test_str)
            m10 = re.findall(regex10_1, test_str)
            m11 = re.findall(regex11_1, test_str)

            matches4 = re.finditer(regex4, test_str, re.MULTILINE)
            matches10 = re.finditer(regex10_2, test_str, re.MULTILINE)
            matches11 = re.finditer(regex11_2, test_str, re.MULTILINE)

            with open(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors.txt', mode = 'a', encoding = 'utf = 8') as Inventors_file :  
                if m != [] :
                    dic_detail['Inventors_Yes'] = int(dic_detail['Inventors_Yes']) + 1
                    print(m, file = Inventors_file)
                else :
                    dic_detail['Inventors_None'] = int(dic_detail['Inventors_None']) + 1
                    print('None', file = Inventors_file)

            with open(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors_Detail/' + str(file_Number) + '.txt', mode = 'a', encoding = 'utf = 8') as Inventors_Detail_file :  
                if m != [] :
                    print(m, file = Inventors_Detail_file)
                else :
                    print('None', file = Inventors_Detail_file)

            with open(''+ str(filepath) +'/uspto/secStep/Family_ID/Family_ID.txt', mode = 'a', encoding = 'utf = 8') as Family_ID_file :  
                if m2 != [] :
                    dic_detail['Family_ID_Yes'] = int(dic_detail['Family_ID_Yes']) + 1
                    print(m2, file = Family_ID_file)
                else :
                    dic_detail['Family_ID_None'] = int(dic_detail['Family_ID_None']) + 1
                    print('None', file = Family_ID_file)

            with open(''+ str(filepath) +'/uspto/secStep/Appl_No/Appl_No.txt', mode = 'a', encoding = 'utf = 8') as Appl_No_file :  
                if m3 != [] :
                    dic_detail['Appl_No_Yes'] = int(dic_detail['Appl_No_Yes']) + 1
                    print(m3, file = Appl_No_file)
                else :
                    dic_detail['Appl_No_None'] = int(dic_detail['Appl_No_None']) + 1
                    print('None', file = Appl_No_file)

            with open(''+ str(filepath) +'/uspto/secStep/Filed/Filed.txt', mode = 'a', encoding = 'utf = 8') as Filed_file :  
                if m4 != [] :
                    dic_detail['Filed_Yes'] = int(dic_detail['Filed_Yes']) + 1
                    for matchNum, match in enumerate(matches4, start = 1):
                        print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), file = Filed_file)
                        break
                else :
                    dic_detail['Filed_None'] = int(dic_detail['Filed_None']) + 1
                    print('None', file = Filed_file)

            with open(''+ str(filepath) +'/uspto/secStep/PCT_Filed/PCT_Filed.txt', mode = 'a', encoding = 'utf = 8') as Pct_Filed_file :  
                if m5 != [] :
                    dic_detail['Pct_Filed_Yes'] = int(dic_detail['Pct_Filed_Yes']) + 1
                    print(m5, file = Pct_Filed_file)
                else :
                    dic_detail['Pct_Filed_None'] = int(dic_detail['Pct_Filed_None']) + 1
                    print('None', file = Pct_Filed_file)

            with open(''+ str(filepath) +'/uspto/secStep/PCT_No/PCT_No.txt', mode = 'a', encoding = 'utf = 8') as Pct_No_file :  
                if m6 != [] :
                    dic_detail['Pct_No_Yes'] = int(dic_detail['Pct_No_Yes']) + 1
                    print(m6, file = Pct_No_file)
                else :
                    dic_detail['Pct_No_None'] = int(dic_detail['Pct_No_None']) + 1
                    print('None', file = Pct_No_file)

            with open(''+ str(filepath) +'/uspto/secStep/371Date/371Date.txt', mode = 'a', encoding = 'utf = 8') as SDate_file :  
                if m7 != [] :
                    dic_detail['SDate_Yes'] = int(dic_detail['SDate_Yes']) + 1
                    print(m7, file = SDate_file)
                else :
                    dic_detail['SDate_None'] = int(dic_detail['SDate_None']) + 1
                    print('None', file = SDate_file)

            with open(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No/PCT_Pub_No.txt', mode = 'a', encoding = 'utf = 8') as Pct_Pub_No_file :  
                if m8 != [] :
                    dic_detail['Pct_Pub_No_Yes'] = int(dic_detail['Pct_Pub_No_Yes']) + 1
                    print(m8, file = Pct_Pub_No_file)
                else :
                    dic_detail['Pct_Pub_No_None'] = int(dic_detail['Pct_Pub_No_None']) + 1
                    print('None', file = Pct_Pub_No_file)
            
            with open(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date/PCT_Pub_Date.txt', mode = 'a', encoding = 'utf = 8') as Pct_Pub_Date_file :  
                if m9 != [] :
                    dic_detail['Pct_Pub_Date_Yes'] = int(dic_detail['Pct_Pub_Date_Yes']) + 1
                    print(m9, file = Pct_Pub_Date_file)
                else :
                    dic_detail['Pct_Pub_Date_None'] = int(dic_detail['Pct_Pub_Date_None']) + 1
                    print('None', file = Pct_Pub_Date_file)

            with open(''+ str(filepath) +'/uspto/secStep/Applicant/' + str(file_Number) + '.txt', mode = 'w', encoding = 'utf = 8') as Applicant_file :  
                if m10 != []:
                    dic_detail['Applicant_Yes'] = int(dic_detail['Applicant_Yes']) + 1
                    for matchNum, match in enumerate(matches10, start=1):
                        print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), file = Applicant_file)
                else :
                    dic_detail['Applicant_None'] = int(dic_detail['Applicant_None']) + 1
                    print('None', file = Applicant_file)

            with open(''+ str(filepath) +'/uspto/secStep/Assignee/' + str(file_Number) + '.txt', mode = 'w', encoding = 'utf = 8') as Assignee_file :  
                if m11 != []:
                    dic_detail['Assignee_Yes'] = int(dic_detail['Assignee_Yes']) + 1
                    for matchNum, match in enumerate(matches11, start=1):
                        print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), file = Assignee_file)
                else :
                    dic_detail['Assignee_None'] = int(dic_detail['Assignee_None']) + 1
                    print('None', file = Assignee_file)
                    
        with open(''+ str(filepath) +'/uspto/IPC/'+ str(file_Number) +'.txt', mode = 'r', encoding = 'utf = 8') as Detailfile :
            dData = Detailfile.read()

            regex12 = r"[A-Z][0-9]+"

            test_str = (dData)

            m12 = re.findall(regex12, test_str)

            with open(''+ str(filepath) +'/uspto/IPC/IPC_Detail/'+ str(file_Number) +'.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                if m12 != [] :
                    unique = []
                    for i in m12 :
                        if i not in unique :
                            unique.append(i)
                    print(unique, file = IPCfile)
                else :
                    print('None', file = IPCfile)
                
        file_Number = file_Number + 1

    print(dic_detail)
#-----------------------------------------------------------------------------
#    CLEAN ['']
#-----------------------------------------------------------------------------
    def fix(folder, txt_name, keyword) :
        with open('' + folder + '/' + txt_name + '.txt', mode = 'r', encoding = 'utf = 8') as f :
            regex = r"" + keyword + ""
            for line in f.readlines() :
                test_str = line

                m = re.findall(regex, test_str)

                matches = re.finditer(regex, test_str, re.MULTILINE)
                with open('' + folder + '/tep.txt', mode = 'a', encoding = 'utf = 8') as f2 :
                    if m != [] :
                        for matchNum, match in enumerate(matches, start = 1) :
                            for groupNum in range(0, len(match.groups())):
                                groupNum = 1
                                print ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)), file = f2)
                    else :
                        print('None', file = f2)

        os.remove('' + folder + '/' + txt_name + '.txt')
        os.rename('' + folder + '/tep.txt', '' + folder + '/' + txt_name + '.txt')

    def fixx(folder, keyword) :
        i = 1
        while i < (TOTAl + 1):
            with open('' + folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                regex = r"" + keyword + ""
                for line in f.readlines() :
                    test_str = line

                    m = re.findall(regex, test_str)

                    matches = re.finditer(regex, test_str, re.MULTILINE)
                    with open('' + folder + '/tep.txt', mode = 'a', encoding = 'utf = 8') as f2 :
                        if m != [] :
                            for matchNum, match in enumerate(matches, start = 1) :
                                for groupNum in range(0, len(match.groups())):
                                    groupNum = 1
                                    print ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)), file = f2)
                        else :
                            print('None', file = f2)

            os.remove('' + folder + '/' + str(i) + '.txt')
            os.rename('' + folder + '/tep.txt', '' + folder + '/' + str(i) + '.txt')
            i = i + 1

    fix(''+ str(filepath) +'/uspto/secStep/371Date', '371Date', "\['371\(c\)\(1\),\(2\),\(4\) Date: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Appl_No', 'Appl_No', "\['Appl\. No\.: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Family_ID', 'Family_ID', "\['Family ID: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Filed', 'Filed', "Filed: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Inventors', 'Inventors', "\[\'?\"?Inventors: (.*\))")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_Filed', 'PCT_Filed', "\['PCT Filed: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_No', 'PCT_No', "\['PCT No\.: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date', 'PCT_Pub_Date', "\['PCT Pub\. Date: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No', 'PCT_Pub_No', "\['PCT Pub\. No\.: (.*\d)")

    fixx(''+ str(filepath) +'/uspto/IPC/IPC_Detail', "([A-Z][0-9]+)")
#-----------------------------------------------------------------------------
#    CLEAN KEYWORDS
#-----------------------------------------------------------------------------
    def fiix(folder, keyword) :
        i = 1
        while i < (TOTAl + 1):
            with open('' + folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                regex = r"" + keyword + ""
                test_str = f.read()

                m = re.findall(regex, test_str)

                with open('' + folder + '/tep.txt', mode = 'w', encoding = 'utf = 8') as f2 :
                    if m != [] :
                        print(test_str.replace('' + keyword + '', ''), file = f2, end = '')
                    else :
                        print('None', file = f2, end = '')
            
            os.remove('' + folder + '/' + str(i) + '.txt')
            os.rename('' + folder + '/tep.txt', '' + folder + '/' + str(i) + '.txt')
            i = i + 1

    def fiixx(folder, keyword) :
        i = 1
        while i < (TOTAl + 1):
            with open('' + folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                x = f.read()
                with open(''+ folder +'/tep.txt', mode = 'a') as f2:
                    print(x.replace('"', ''), end = '', sep='', file = f2)
            os.remove('' + folder + '/' + str(i) + '.txt')
            os.rename(''+ folder +'/tep.txt', '' + folder + '/' + str(i) + '.txt')
            i = i + 1

    fiix(''+ str(filepath) +'/uspto/Prior_Publication_Data', "Document Identifier Publication Date\n")
    fiix(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents', "Application Number Filing Date Patent Number Issue Date\n")
    fiix(''+ str(filepath) +'/uspto/secStep/Assignee', "Assignee: ")
    fiix(''+ str(filepath) +'/uspto/secStep/Applicant', '''Applicant:
Name City State Country Type

''')

    fiixx(''+ str(filepath) +'/uspto/secStep/Assignee', '"')
    fiixx(''+ str(filepath) +'/uspto/Abstract', '"')
#-----------------------------------------------------------------------------
#    CLASSIFY APPLICANT
#-----------------------------------------------------------------------------
    def fiiix(old_folder, neew_folder):
        i = 1
        while i < (TOTAl + 1):
            with open('' + old_folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                lens = len(f.readlines())
                x = int(lens / 4)
                file = open(r'' + old_folder + '/' + str(i) + '.txt')
                text = []
                for line in file:
                    text.append(line)
                if lens == 1 :
                    with open ('' + neew_folder + '/Name/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as Name_file :
                        print('None', file = Name_file)

                    with open ('' + neew_folder + '/City/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as City_file :
                        print('None', file = City_file)

                    with open ('' + neew_folder + '/State/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as State_file :
                        print('None', file = State_file)

                    with open ('' + neew_folder + '/Country/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as Country_file :
                        print('None', file = Country_file)
                else :
                    j = 1
                    while j < (x + 1) :
                        with open ('' + neew_folder + '/Name/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as Name_file :
                            print(text[j - 1], end = '', file = Name_file)

                        with open ('' + neew_folder + '/City/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as City_file :
                            print(text[j + (x - 1)], end = '', file = City_file)

                        with open ('' + neew_folder + '/State/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as State_file :
                            print(text[j + 1 + ((x - 1) * 2)], end = '', file = State_file)
                        
                        with open ('' + neew_folder + '/Country/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as Country_file :
                            print(text[j + 2 + ((x - 1) * 3)], end = '', file = Country_file)

                        j = j + 1
            i = i + 1

    fiiix(''+ str(filepath) +'/uspto/secStep/Applicant', ''+ str(filepath) +'/uspto/secStep/Applicant')
#-----------------------------------------------------------------------------
#    TO CSV FIRST
#-----------------------------------------------------------------------------
    file = open(r''+ str(filepath) +'/uspto/NO./NO.txt')

    file2 = open(r''+ str(filepath) +'/uspto/et al./et_al.txt')

    text = []
    text2 = []

    for line in file:
        text.append(line)

    for line in file2:
        text2.append(line)

    i = 1
    with open(''+ str(filepath) +'/uspto/csv/final.txt', mode = 'a') as f :
        while i < (TOTAl + 1):
            print('"', text[i - 1].replace('\n', '","'+ text2[i - 1] +''), end = '', sep='', file = f)
            i = i + 1
#-----------------------------------------------------------------------------
#    TO CSV DEFs
#-----------------------------------------------------------------------------
    def toCSV(txt):
        i = 1
        file = open(r''+ txt +'')
        finalfile = open(r''+ str(filepath) +'/uspto/csv/final.txt')

        text = []
        finaltext = []

        for line in file:
            text.append(line)

        for line in finalfile:
            finaltext.append(line)

        with open(''+ str(filepath) +'/uspto/csv/final.txt', mode = 'r') as f:
            while i < (TOTAl + 1):
                with open(''+ str(filepath) +'/uspto/csv/tep2.txt', mode = 'a') as f2:
                    print(finaltext[i - 1].replace('\n', '","'+ text[i - 1] +''), end = '', sep='', file = f2)
                    i = i + 1
        os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
        os.rename(''+ str(filepath) +'/uspto/csv/tep2.txt',''+ str(filepath) +'/uspto/csv/final.txt')

    def ONELINE(folder):
        i = 1
        while i < (TOTAl + 1) :
            with open(''+ folder +'/'+ str(i) +'.txt', mode = 'r', encoding = 'utf = 8') as f:
                lens = int(len(f.readlines()))
                if lens < 500:
                    with open(''+ folder +'/'+ str(i) +'.txt', mode = 'r', encoding = 'utf = 8') as f2:
                        x = f2.read()
                        with open(''+ folder +'/tep.txt', mode = 'a') as f3:
                            print(x.replace('\n', '@@@'), end = '', sep='', file = f3)
                            print('\n', end = '', file= f3)
                else :
                    with open(''+ folder +'/'+ str(i) +'.txt', mode = 'r', encoding = 'utf = 8') as f2:
                        x = f2.read()
                        with open(''+ folder +'/tep.txt', mode = 'a') as f3:
                            print('IT IS TOO LOONG : '+ str(lens) +'', end = '', file= f3)
                            print('\n', end = '', file= f3)
            i = i + 1
        i = 1
        file2 = open(r''+ folder +'/tep.txt')

        finalfile = open(r''+ str(filepath) +'/uspto/csv/final.txt')

        text2 = []
        finaltext = []

        for line in file2:
            text2.append(line)

        for line in finalfile:
            finaltext.append(line)

        with open(''+ str(filepath) +'/uspto/csv/final.txt', mode = 'r') as f:
            while i < (TOTAl + 1):
                with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f2:
                    print(finaltext[i - 1].replace('\n', '","'+ text2[i - 1] +''), end = '', sep='', file = f2)
                    i = i + 1
        os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
        os.remove('' + folder + '/tep.txt')
        os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.txt')

        file3 = open(r''+ str(filepath) +'/uspto/csv/final.txt')

        text3 = []
        
        for line in file3:
            text3.append(line)

        i = 1
        with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f :
            while i < (TOTAl + 1):
                print(text3[i - 1].replace('@@@\n', '\n'), end = '', sep='', file = f)
                i = i + 1
        os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
        os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.txt')
#-----------------------------------------------------------------------------
#    TO CSV
#-----------------------------------------------------------------------------
    toCSV(''+ str(filepath) +'/uspto/Date/Date.txt')
    toCSV(''+ str(filepath) +'/uspto/Title/Title.txt')
    ONELINE(''+ str(filepath) +'/uspto/Abstract')
    toCSV(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors.txt')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/City')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/Country')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/Name')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/State')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Assignee')
    toCSV(''+ str(filepath) +'/uspto/secStep/371Date/371Date.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/Appl_No/Appl_No.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/Family_ID/Family_ID.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/Filed/Filed.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_Filed/PCT_Filed.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_No/PCT_No.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date/PCT_Pub_Date.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No/PCT_Pub_No.txt')
    ONELINE(''+ str(filepath) +'/uspto/Prior_Publication_Data')
    ONELINE(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents')
    ONELINE(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data')
    ONELINE(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents')
    ONELINE(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents')
#-----------------------------------------------------------------------------
#    TO CSV END
#-----------------------------------------------------------------------------
    file3 = open(r''+ str(filepath) +'/uspto/csv/final.txt')

    text3 = []

    for line in file3:
        text3.append(line)

    i = 1
    with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f3 :
        while i < (TOTAl + 1):
            print(text3[i - 1].replace('\n', '"\n'), end = '', sep='', file = f3)
            i = i + 1

    os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
    os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.txt')
#-----------------------------------------------------------------------------
#    TO CSV CLEAN @@@
#-----------------------------------------------------------------------------
    file4 = open(r''+ str(filepath) +'/uspto/csv/final.txt')

    text4 = []

    for line in file4:
        text4.append(line)

    i = 1
    with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f4 :
        while i < (TOTAl + 1):
            print(text4[i - 1].replace('@@@', '\n'), end = '', sep='', file = f4)
            i = i + 1

    with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'r+') as f5 :
        content = f5.read()
        f5.seek(0, 0)
        f5.write('"NO.","et al.","Date","Title","Abstract","Inventors","Applicant_City","Applicant_Country","Applicant_Name","Applicant_State","Assignee","371Date","Appl_No.","Family_ID","Filed","PCT_Filed","PCT_No.","PCT_Pub_Date","PCT_Pub_No.","Prior_Publication_Data","Related_U.S._Patent_Documents","Foreign_Application_Priority_Data","References_Cited_Foreign_Patent_Documents","References_Cited_U.S._Patent_Documents"\n'+content)

    os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
    os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.csv')
    message = 'Done'
    lineNotifyMessage(token, message)
    
elif DoIt == 'N':
    print('Nothing to do now')
    
elif DoIt == 'F':
    print('Please input filepath :')
    filepath = input()
    with open(''+ str(filepath) +'/uspto/Total/Total.txt', mode = 'r',encoding = 'utf=8') as pagefile :
        TOTAl = int(pagefile.readline())
#-----------------------------------------------------------------------------
#     CLASSIFY DETAIL
#-----------------------------------------------------------------------------
    file_Number = 1
    while file_Number < (TOTAl + 1) :
        with open(''+ str(filepath) +'/uspto/Detail/' + str(file_Number) + '.txt', mode = 'r', encoding = 'utf = 8') as Detailfile :
            dData = Detailfile.read()

            regex = r"^Inventors:\s.+"
            regex2 = r"Family ID:\s.+"
            regex3 = r"Appl\. No\.:\s.+"
            regex4 = r"Filed:\s.+"
            regex5 = r"PCT Filed:\s.+"
            regex6 = r"PCT No\.:\s.+"
            regex7 = r"371\(c\)\(1\),\(2\),\(4\) Date:\s.+"
            regex8 = r"PCT Pub\. No\.:\s.+"
            regex9 = r"PCT Pub\. Date:\s.+"
            regex10_1 = r"Applicant:"
            regex10_2 = (r"Applicant:\n"
                r"Name City State Country Type\n\n"
                r"(.+\n)*..$")
            regex11_1 = r"Assignee:"
            regex11_2 = r"Assignee:(.*\n)*.*\)$"

            test_str = (dData)

            m = re.findall(regex, test_str)
            m2 = re.findall(regex2, test_str)
            m3 = re.findall(regex3, test_str)
            m4 = re.findall(regex4, test_str)
            m5 = re.findall(regex5, test_str)
            m6 = re.findall(regex6, test_str)
            m7 = re.findall(regex7, test_str)
            m8 = re.findall(regex8, test_str)
            m9 = re.findall(regex9, test_str)
            m10 = re.findall(regex10_1, test_str)
            m11 = re.findall(regex11_1, test_str)

            matches4 = re.finditer(regex4, test_str, re.MULTILINE)
            matches10 = re.finditer(regex10_2, test_str, re.MULTILINE)
            matches11 = re.finditer(regex11_2, test_str, re.MULTILINE)

            with open(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors.txt', mode = 'a', encoding = 'utf = 8') as Inventors_file :  
                if m != [] :
                    dic_detail['Inventors_Yes'] = int(dic_detail['Inventors_Yes']) + 1
                    print(m, file = Inventors_file)
                else :
                    dic_detail['Inventors_None'] = int(dic_detail['Inventors_None']) + 1
                    print('None', file = Inventors_file)

            with open(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors_Detail/' + str(file_Number) + '.txt', mode = 'a', encoding = 'utf = 8') as Inventors_Detail_file :  
                if m != [] :
                    print(m, file = Inventors_Detail_file)
                else :
                    print('None', file = Inventors_Detail_file)

            with open(''+ str(filepath) +'/uspto/secStep/Family_ID/Family_ID.txt', mode = 'a', encoding = 'utf = 8') as Family_ID_file :  
                if m2 != [] :
                    dic_detail['Family_ID_Yes'] = int(dic_detail['Family_ID_Yes']) + 1
                    print(m2, file = Family_ID_file)
                else :
                    dic_detail['Family_ID_None'] = int(dic_detail['Family_ID_None']) + 1
                    print('None', file = Family_ID_file)

            with open(''+ str(filepath) +'/uspto/secStep/Appl_No/Appl_No.txt', mode = 'a', encoding = 'utf = 8') as Appl_No_file :  
                if m3 != [] :
                    dic_detail['Appl_No_Yes'] = int(dic_detail['Appl_No_Yes']) + 1
                    print(m3, file = Appl_No_file)
                else :
                    dic_detail['Appl_No_None'] = int(dic_detail['Appl_No_None']) + 1
                    print('None', file = Appl_No_file)

            with open(''+ str(filepath) +'/uspto/secStep/Filed/Filed.txt', mode = 'a', encoding = 'utf = 8') as Filed_file :  
                if m4 != [] :
                    dic_detail['Filed_Yes'] = int(dic_detail['Filed_Yes']) + 1
                    for matchNum, match in enumerate(matches4, start = 1):
                        print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), file = Filed_file)
                        break
                else :
                    dic_detail['Filed_None'] = int(dic_detail['Filed_None']) + 1
                    print('None', file = Filed_file)

            with open(''+ str(filepath) +'/uspto/secStep/PCT_Filed/PCT_Filed.txt', mode = 'a', encoding = 'utf = 8') as Pct_Filed_file :  
                if m5 != [] :
                    dic_detail['Pct_Filed_Yes'] = int(dic_detail['Pct_Filed_Yes']) + 1
                    print(m5, file = Pct_Filed_file)
                else :
                    dic_detail['Pct_Filed_None'] = int(dic_detail['Pct_Filed_None']) + 1
                    print('None', file = Pct_Filed_file)

            with open(''+ str(filepath) +'/uspto/secStep/PCT_No/PCT_No.txt', mode = 'a', encoding = 'utf = 8') as Pct_No_file :  
                if m6 != [] :
                    dic_detail['Pct_No_Yes'] = int(dic_detail['Pct_No_Yes']) + 1
                    print(m6, file = Pct_No_file)
                else :
                    dic_detail['Pct_No_None'] = int(dic_detail['Pct_No_None']) + 1
                    print('None', file = Pct_No_file)

            with open(''+ str(filepath) +'/uspto/secStep/371Date/371Date.txt', mode = 'a', encoding = 'utf = 8') as SDate_file :  
                if m7 != [] :
                    dic_detail['SDate_Yes'] = int(dic_detail['SDate_Yes']) + 1
                    print(m7, file = SDate_file)
                else :
                    dic_detail['SDate_None'] = int(dic_detail['SDate_None']) + 1
                    print('None', file = SDate_file)

            with open(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No/PCT_Pub_No.txt', mode = 'a', encoding = 'utf = 8') as Pct_Pub_No_file :  
                if m8 != [] :
                    dic_detail['Pct_Pub_No_Yes'] = int(dic_detail['Pct_Pub_No_Yes']) + 1
                    print(m8, file = Pct_Pub_No_file)
                else :
                    dic_detail['Pct_Pub_No_None'] = int(dic_detail['Pct_Pub_No_None']) + 1
                    print('None', file = Pct_Pub_No_file)
            
            with open(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date/PCT_Pub_Date.txt', mode = 'a', encoding = 'utf = 8') as Pct_Pub_Date_file :  
                if m9 != [] :
                    dic_detail['Pct_Pub_Date_Yes'] = int(dic_detail['Pct_Pub_Date_Yes']) + 1
                    print(m9, file = Pct_Pub_Date_file)
                else :
                    dic_detail['Pct_Pub_Date_None'] = int(dic_detail['Pct_Pub_Date_None']) + 1
                    print('None', file = Pct_Pub_Date_file)

            with open(''+ str(filepath) +'/uspto/secStep/Applicant/' + str(file_Number) + '.txt', mode = 'w', encoding = 'utf = 8') as Applicant_file :  
                if m10 != []:
                    dic_detail['Applicant_Yes'] = int(dic_detail['Applicant_Yes']) + 1
                    for matchNum, match in enumerate(matches10, start=1):
                        print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), file = Applicant_file)
                else :
                    dic_detail['Applicant_None'] = int(dic_detail['Applicant_None']) + 1
                    print('None', file = Applicant_file)

            with open(''+ str(filepath) +'/uspto/secStep/Assignee/' + str(file_Number) + '.txt', mode = 'w', encoding = 'utf = 8') as Assignee_file :  
                if m11 != []:
                    dic_detail['Assignee_Yes'] = int(dic_detail['Assignee_Yes']) + 1
                    for matchNum, match in enumerate(matches11, start=1):
                        print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), file = Assignee_file)
                else :
                    dic_detail['Assignee_None'] = int(dic_detail['Assignee_None']) + 1
                    print('None', file = Assignee_file)
                    
        with open(''+ str(filepath) +'/uspto/IPC/'+ str(file_Number) +'.txt', mode = 'r', encoding = 'utf = 8') as Detailfile :
            dData = Detailfile.read()

            regex12 = r"[A-Z][0-9]+"

            test_str = (dData)

            m12 = re.findall(regex12, test_str)

            with open(''+ str(filepath) +'/uspto/IPC/IPC_Detail/'+ str(file_Number) +'.txt', mode = 'w', encoding = 'utf = 8') as IPCfile :
                if m12 != [] :
                    unique = []
                    for i in m12 :
                        if i not in unique :
                            unique.append(i)
                    print(unique, file = IPCfile)
                else :
                    print('None', file = IPCfile)
                
        file_Number = file_Number + 1

    print(dic_detail)
#-----------------------------------------------------------------------------
#    CLEAN ['']
#-----------------------------------------------------------------------------
    def fix(folder, txt_name, keyword) :
        with open('' + folder + '/' + txt_name + '.txt', mode = 'r', encoding = 'utf = 8') as f :
            regex = r"" + keyword + ""
            for line in f.readlines() :
                test_str = line

                m = re.findall(regex, test_str)

                matches = re.finditer(regex, test_str, re.MULTILINE)
                with open('' + folder + '/tep.txt', mode = 'a', encoding = 'utf = 8') as f2 :
                    if m != [] :
                        for matchNum, match in enumerate(matches, start = 1) :
                            for groupNum in range(0, len(match.groups())):
                                groupNum = 1
                                print ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)), file = f2)
                    else :
                        print('None', file = f2)

        os.remove('' + folder + '/' + txt_name + '.txt')
        os.rename('' + folder + '/tep.txt', '' + folder + '/' + txt_name + '.txt')

    def fixx(folder, keyword) :
        i = 1
        while i < (TOTAl + 1):
            with open('' + folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                regex = r"" + keyword + ""
                for line in f.readlines() :
                    test_str = line

                    m = re.findall(regex, test_str)

                    matches = re.finditer(regex, test_str, re.MULTILINE)
                    with open('' + folder + '/tep.txt', mode = 'a', encoding = 'utf = 8') as f2 :
                        if m != [] :
                            for matchNum, match in enumerate(matches, start = 1) :
                                for groupNum in range(0, len(match.groups())):
                                    groupNum = 1
                                    print ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)), file = f2)
                        else :
                            print('None', file = f2)

            os.remove('' + folder + '/' + str(i) + '.txt')
            os.rename('' + folder + '/tep.txt', '' + folder + '/' + str(i) + '.txt')
            i = i + 1

    fix(''+ str(filepath) +'/uspto/secStep/371Date', '371Date', "\['371\(c\)\(1\),\(2\),\(4\) Date: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Appl_No', 'Appl_No', "\['Appl\. No\.: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Family_ID', 'Family_ID', "\['Family ID: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Filed', 'Filed', "Filed: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/Inventors', 'Inventors', "\[\'?\"?Inventors: (.*\))")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_Filed', 'PCT_Filed', "\['PCT Filed: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_No', 'PCT_No', "\['PCT No\.: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date', 'PCT_Pub_Date', "\['PCT Pub\. Date: (.*\d)")
    fix(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No', 'PCT_Pub_No', "\['PCT Pub\. No\.: (.*\d)")

    fixx(''+ str(filepath) +'/uspto/IPC/IPC_Detail', "([A-Z][0-9]+)")
#-----------------------------------------------------------------------------
#    CLEAN KEYWORDS
#-----------------------------------------------------------------------------
    def fiix(folder, keyword) :
        i = 1
        while i < (TOTAl + 1):
            with open('' + folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                regex = r"" + keyword + ""
                test_str = f.read()

                m = re.findall(regex, test_str)

                with open('' + folder + '/tep.txt', mode = 'w', encoding = 'utf = 8') as f2 :
                    if m != [] :
                        print(test_str.replace('' + keyword + '', ''), file = f2, end = '')
                    else :
                        print('None', file = f2, end = '')
            
            os.remove('' + folder + '/' + str(i) + '.txt')
            os.rename('' + folder + '/tep.txt', '' + folder + '/' + str(i) + '.txt')
            i = i + 1

    def fiixx(folder, keyword) :
        i = 1
        while i < (TOTAl + 1):
            with open('' + folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                x = f.read()
                with open(''+ folder +'/tep.txt', mode = 'a') as f2:
                    print(x.replace('"', ''), end = '', sep='', file = f2)
            os.remove('' + folder + '/' + str(i) + '.txt')
            os.rename(''+ folder +'/tep.txt', '' + folder + '/' + str(i) + '.txt')
            i = i + 1

    fiix(''+ str(filepath) +'/uspto/Prior_Publication_Data', "Document Identifier Publication Date\n")
    fiix(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents', "Application Number Filing Date Patent Number Issue Date\n")
    fiix(''+ str(filepath) +'/uspto/secStep/Assignee', "Assignee: ")
    fiix(''+ str(filepath) +'/uspto/secStep/Applicant', '''Applicant:
Name City State Country Type

''')

    fiixx(''+ str(filepath) +'/uspto/secStep/Assignee', '"')
    fiixx(''+ str(filepath) +'/uspto/Abstract', '"')
#-----------------------------------------------------------------------------
#    CLASSIFY APPLICANT
#-----------------------------------------------------------------------------
    def fiiix(old_folder, neew_folder):
        i = 1
        while i < (TOTAl + 1):
            with open('' + old_folder + '/' + str(i) + '.txt', mode = 'r', encoding = 'utf = 8') as f :
                lens = len(f.readlines())
                x = int(lens / 4)
                file = open(r'' + old_folder + '/' + str(i) + '.txt')
                text = []
                for line in file:
                    text.append(line)
                if lens == 1 :
                    with open ('' + neew_folder + '/Name/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as Name_file :
                        print('None', file = Name_file)

                    with open ('' + neew_folder + '/City/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as City_file :
                        print('None', file = City_file)

                    with open ('' + neew_folder + '/State/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as State_file :
                        print('None', file = State_file)

                    with open ('' + neew_folder + '/Country/' + str(i) + '.txt', mode = 'w', encoding = 'utf = 8') as Country_file :
                        print('None', file = Country_file)
                else :
                    j = 1
                    while j < (x + 1) :
                        with open ('' + neew_folder + '/Name/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as Name_file :
                            print(text[j - 1], end = '', file = Name_file)

                        with open ('' + neew_folder + '/City/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as City_file :
                            print(text[j + (x - 1)], end = '', file = City_file)

                        with open ('' + neew_folder + '/State/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as State_file :
                            print(text[j + 1 + ((x - 1) * 2)], end = '', file = State_file)
                        
                        with open ('' + neew_folder + '/Country/' + str(i) + '.txt', mode = 'a', encoding = 'utf = 8') as Country_file :
                            print(text[j + 2 + ((x - 1) * 3)], end = '', file = Country_file)

                        j = j + 1
            i = i + 1

    fiiix(''+ str(filepath) +'/uspto/secStep/Applicant', ''+ str(filepath) +'/uspto/secStep/Applicant')
#-----------------------------------------------------------------------------
#    TO CSV FIRST
#-----------------------------------------------------------------------------
    file = open(r''+ str(filepath) +'/uspto/NO./NO.txt')

    file2 = open(r''+ str(filepath) +'/uspto/et al./et_al.txt')

    text = []
    text2 = []

    for line in file:
        text.append(line)

    for line in file2:
        text2.append(line)

    i = 1
    with open(''+ str(filepath) +'/uspto/csv/final.txt', mode = 'a') as f :
        while i < (TOTAl + 1):
            print('"', text[i - 1].replace('\n', '","'+ text2[i - 1] +''), end = '', sep='', file = f)
            i = i + 1
#-----------------------------------------------------------------------------
#    TO CSV DEFs
#-----------------------------------------------------------------------------
    def toCSV(txt):
        i = 1
        file = open(r''+ txt +'')
        finalfile = open(r''+ str(filepath) +'/uspto/csv/final.txt')

        text = []
        finaltext = []

        for line in file:
            text.append(line)

        for line in finalfile:
            finaltext.append(line)

        with open(''+ str(filepath) +'/uspto/csv/final.txt', mode = 'r') as f:
            while i < (TOTAl + 1):
                with open(''+ str(filepath) +'/uspto/csv/tep2.txt', mode = 'a') as f2:
                    print(finaltext[i - 1].replace('\n', '","'+ text[i - 1] +''), end = '', sep='', file = f2)
                    i = i + 1
        os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
        os.rename(''+ str(filepath) +'/uspto/csv/tep2.txt',''+ str(filepath) +'/uspto/csv/final.txt')

    def ONELINE(folder):
        i = 1
        while i < (TOTAl + 1) :
            with open(''+ folder +'/'+ str(i) +'.txt', mode = 'r', encoding = 'utf = 8') as f:
                lens = int(len(f.readlines()))
                if lens < 500:
                    with open(''+ folder +'/'+ str(i) +'.txt', mode = 'r', encoding = 'utf = 8') as f2:
                        x = f2.read()
                        with open(''+ folder +'/tep.txt', mode = 'a') as f3:
                            print(x.replace('\n', '@@@'), end = '', sep='', file = f3)
                            print('\n', end = '', file= f3)
                else :
                    with open(''+ folder +'/'+ str(i) +'.txt', mode = 'r', encoding = 'utf = 8') as f2:
                        x = f2.read()
                        with open(''+ folder +'/tep.txt', mode = 'a') as f3:
                            print('IT IS TOO LOONG : '+ str(lens) +'', end = '', file= f3)
                            print('\n', end = '', file= f3)
            i = i + 1
        i = 1
        file2 = open(r''+ folder +'/tep.txt')

        finalfile = open(r''+ str(filepath) +'/uspto/csv/final.txt')

        text2 = []
        finaltext = []

        for line in file2:
            text2.append(line)

        for line in finalfile:
            finaltext.append(line)

        with open(''+ str(filepath) +'/uspto/csv/final.txt', mode = 'r') as f:
            while i < (TOTAl + 1):
                with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f2:
                    print(finaltext[i - 1].replace('\n', '","'+ text2[i - 1] +''), end = '', sep='', file = f2)
                    i = i + 1
        os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
        os.remove('' + folder + '/tep.txt')
        os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.txt')

        file3 = open(r''+ str(filepath) +'/uspto/csv/final.txt')

        text3 = []
        
        for line in file3:
            text3.append(line)

        i = 1
        with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f :
            while i < (TOTAl + 1):
                print(text3[i - 1].replace('@@@\n', '\n'), end = '', sep='', file = f)
                i = i + 1
        os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
        os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.txt')
#-----------------------------------------------------------------------------
#    TO CSV
#-----------------------------------------------------------------------------
    toCSV(''+ str(filepath) +'/uspto/Date/Date.txt')
    toCSV(''+ str(filepath) +'/uspto/Title/Title.txt')
    ONELINE(''+ str(filepath) +'/uspto/Abstract')
    toCSV(''+ str(filepath) +'/uspto/secStep/Inventors/Inventors.txt')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/City')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/Country')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/Name')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Applicant/State')
    ONELINE(''+ str(filepath) +'/uspto/secStep/Assignee')
    toCSV(''+ str(filepath) +'/uspto/secStep/371Date/371Date.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/Appl_No/Appl_No.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/Family_ID/Family_ID.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/Filed/Filed.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_Filed/PCT_Filed.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_No/PCT_No.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_Pub_Date/PCT_Pub_Date.txt')
    toCSV(''+ str(filepath) +'/uspto/secStep/PCT_Pub_No/PCT_Pub_No.txt')
    ONELINE(''+ str(filepath) +'/uspto/Prior_Publication_Data')
    ONELINE(''+ str(filepath) +'/uspto/Related_U.S._Patent_Documents')
    ONELINE(''+ str(filepath) +'/uspto/Foreign_Application_Priority_Data')
    ONELINE(''+ str(filepath) +'/uspto/References_Cited_Foreign_Patent_Documents')
    ONELINE(''+ str(filepath) +'/uspto/References_Cited_U.S._Patent_Documents')
#-----------------------------------------------------------------------------
#    TO CSV END
#-----------------------------------------------------------------------------
    file3 = open(r''+ str(filepath) +'/uspto/csv/final.txt')

    text3 = []

    for line in file3:
        text3.append(line)

    i = 1
    with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f3 :
        while i < (TOTAl + 1):
            print(text3[i - 1].replace('\n', '"\n'), end = '', sep='', file = f3)
            i = i + 1

    os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
    os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.txt')
#-----------------------------------------------------------------------------
#    TO CSV CLEAN @@@
#-----------------------------------------------------------------------------
    file4 = open(r''+ str(filepath) +'/uspto/csv/final.txt')

    text4 = []

    for line in file4:
        text4.append(line)

    i = 1
    with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'a') as f4 :
        while i < (TOTAl + 1):
            print(text4[i - 1].replace('@@@', '\n'), end = '', sep='', file = f4)
            i = i + 1

    with open(''+ str(filepath) +'/uspto/csv/tep.txt', mode = 'r+') as f5 :
        content = f5.read()
        f5.seek(0, 0)
        f5.write('"NO.","et al.","Date","Title","Abstract","Inventors","Applicant_City","Applicant_Country","Applicant_Name","Applicant_State","Assignee","371Date","Appl_No.","Family_ID","Filed","PCT_Filed","PCT_No.","PCT_Pub_Date","PCT_Pub_No.","Prior_Publication_Data","Related_U.S._Patent_Documents","Foreign_Application_Priority_Data","References_Cited_Foreign_Patent_Documents","References_Cited_U.S._Patent_Documents"\n'+content)

    os.remove(''+ str(filepath) +'/uspto/csv/final.txt')
    os.rename(''+ str(filepath) +'/uspto/csv/tep.txt',''+ str(filepath) +'/uspto/csv/final.csv')
    message = 'Done'
    lineNotifyMessage(token, message)
        
else:
    print('[PLEASE TYPE Y or N] , and try again')