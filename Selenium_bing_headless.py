from selenium import webdriver
import time
import login_data
import random
import datetime
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
from colorama import Fore, Back, init
from googleapiclient.discovery import build
from google.oauth2 import service_account


path_wortlist = 'wordlist.txt'
username_list = login_data.get_username_login()
password_list = login_data.get_password_login()
maxwait = 3
minwait = 2
shortmin = 0.2
shortmax = 1
counter_acc = 0
counter_excel = 1


edge_options = EdgeOptions()
edge_options.add_argument('--disable-logging')
edge_options.add_argument('log-level=3')
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.use_chromium = True
init()

SERVICE_ACCOUNT_FILE = 'Keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = login_data.get_Sheets_ID()

service = build('sheets', 'v4', credentials=creds)


def shortsleep():
    time.sleep(random.uniform(shortmin, shortmax))


def sleep():
    time.sleep(random.uniform(minwait, maxwait))


def bing_pc_search():
    driver.get('https://www.bing.com/')
    for i in range(get_pc_search()):
        words = open(path_wortlist).read().split('\n')
        bing_search_field = driver.find_element_by_id('sb_form_q')
        bing_search_field.send_keys(random.choice(words) + ' ')
        shortsleep()
        bing_search_field.submit()
        shortsleep()


def get_pc_search():
    driver.get('https://www.bing.com///rewardsapp///flyout')
    sleep()
    element = driver.find_element_by_xpath(
        '//*[@id="modern-flyout"]/div/div[5]/div/div[2]/div[1]/div/div').text.split("/")
    element1 = driver.find_element_by_xpath(
        '//*[@id="modern-flyout"]/div/div[5]/div/div[2]/div[2]/div/div').text.split("/")  # probaly wrong div
    number = (int(element[1]) - int(element[0]) +
              (int(element1[1]) - int(element1[0])))/3
    driver.get('https://www.bing.com/')
    print(str(number) + ' pc Search|', end='')
    return int(number)


def get_mobile_search():
    mobile_driver.get('https://www.bing.com///rewardsapp///flyout')
    element = mobile_driver.find_element_by_xpath(
        '//*[@id="modern-flyout"]/div/div[5]/div/div[2]/div[3]/div/div').text.split("/")
    number = (int(element[1]) - int(element[0]))/3
    mobile_driver.get('https://www.bing.com/')
    print(str(number) + ' mobil search|', end='')
    return int(number)


def get_mobile_search_on_pc():
    driver.get('https://www.bing.com///rewardsapp///flyout')
    element = driver.find_element_by_xpath(
        '//*[@id="modern-flyout"]/div/div[5]/div/div[2]/div[3]/div/div').text.split("/")
    number = (int(element[1]) - int(element[0]))/3
    driver.get('https://www.bing.com/')
    print(str(number) + ' mobil search|', end='')
    return int(number)


def bing_mobile_search():
    for i in range(get_mobile_search()):
        words = open(path_wortlist).read().split('\n')
        bing_search_mobile_field = mobile_driver.find_element_by_id(
            'sb_form_q')
        bing_search_mobile_field.send_keys(random.choice(words) + ' ')
        shortsleep()
        bing_search_mobile_field.submit()
        shortsleep()


def login_bing(counter_acc_int):
    driver.get('https://www.bing.com/?cc=de')
    time.sleep(9)
    try:
        driver.find_element_by_class_name('bnp_btn_accept').click()
       # driver.find_element_by_id('bnp_btn_accept').click()
    except:
        print('error 23123 no cookie button found|', end='')
    sleep()
    try:
        sleep()
        driver.find_element_by_id('id_s').click()
        sleep()
        driver.find_element_by_class_name('id_link_text').click()
        sleep()
        driver.find_element_by_id('id_s').click()
        sleep()
    except:
        print('error login 3|', end='')
    try:
        shortsleep()
        driver.find_element_by_id('i0116').send_keys(
            username_list[counter_acc_int])
        sleep()
        driver.find_element_by_id('idSIButton9').click()
        sleep()
    except:
        print('could not find login field now try restart|', end='')
        login_bing(counter_acc)
    try:
        driver.find_element_by_id('msaTile').click()
        sleep()
    except:
        print('', end='')
    driver.find_element_by_id('i0118').send_keys(
        password_list[counter_acc_int])
    sleep()
    driver.find_element_by_id('idSIButton9').click()


def get_mobile_driver():
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "mobileEmulation", mobile_emulation)
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    return webdriver.Chrome('chromedriver.exe', options=chrome_options)


def bing_mobile_login(counter_acc_int):
    mobile_driver.get('https://www.bing.com/')
    time.sleep(4)
    try:
        mobile_driver.find_element_by_id('bnp_btn_accept').click()
    except:
        print('error 1903481729471 no cookie button found|', end='')
    sleep()
    mobile_driver.find_element_by_id('mHamburger').click()
    sleep()
    mobile_driver.find_element_by_id('hb_s').click()
    sleep()
    # dont know what is happening some time works sometimens not
    mobile_driver.find_element_by_id(
        'i0116').send_keys(username_list[counter_acc_int])
    sleep()
    mobile_driver.find_element_by_id('idSIButton9').click()
    sleep()
    try:
        mobile_driver.find_element_by_id('msaTile').click()
        sleep()
    except:
        print('', end='')
    mobile_driver.find_element_by_id(
        'i0118').send_keys(password_list[counter_acc_int])
    sleep()
    mobile_driver.find_element_by_id('idSIButton9').click()
    sleep()


def scan_daily_task():
    driver.get('https://www.bing.com///rewardsapp///flyout')
    list_len = len(driver.find_elements_by_class_name('rw-si.add'))
    print("daily task:" + str(list_len) + '|', end='')
    while list_len != 0:
        driver.find_elements_by_class_name('rw-si.add')[0].click()
        bing_do_task(quiz=False)
        driver.get('https://www.bing.com///rewardsapp///flyout')
        sleep()
        list_len = len(driver.find_elements_by_class_name('rw-si.add'))
        print("daily task: " + str(list_len) + '|', end='')
    sleep()
    driver.find_element_by_class_name('i-h.rw-sh.fp_row').click()
    list_len = len(driver.find_elements_by_class_name('rw-si.add'))
    print("daily special:" + str(list_len) + '|', end='')
    while list_len != 0:
        driver.find_elements_by_class_name('rw-si.add')[0].click()
        bing_do_task(quiz=False)
        driver.get('https://www.bing.com///rewardsapp///flyout')
        sleep()
        driver.find_element_by_class_name('i-h.rw-sh.fp_row').click()
        list_len = len(driver.find_elements_by_class_name('rw-si.add'))
        print("daily special:" + str(list_len) + '|', end='')


def bing_do_task(quiz):
    sleep()
    if len(driver.find_elements_by_id('rqStartQuiz')) > 0:
        quiz = True
    if len(driver.find_elements_by_id('btoption0')) > 0:
        driver.find_element_by_id('btoption0').click()
        shortsleep()
        return
    if quiz == True:
        driver.find_element_by_id('rqStartQuiz').click()
        sleep()
        if len(driver.find_elements_by_class_name('btCardImg')) > 0:
            print('quiz 3|', end='')
            do_quiz_3()
            shortsleep()
            return
        if len(driver.find_elements_by_class_name("bt_cardText")) > 0:
            print('quiz 1|', end='')
            do_quiz_1()
            shortsleep()
            return
        if len(driver.find_elements_by_id('rqAnswerOption0')) > 0:
            print('quiz 2|', end='')
            do_quiz_2()
            shortsleep()
            return
    if len(driver.find_elements_by_id('rqAnswerOption0')) > 0:
        do_quiz_1()
        return


def do_quiz_1():
    list_len = len(driver.find_elements_by_css_selector(
        'div.b_cards[iscorrectoption="True"]'))
    for i in range(3):
        time.sleep(7)
        for t in range(len(driver.find_elements_by_css_selector('div.b_cards[iscorrectoption="True"]'))):
            sleep()

            try:
                driver.find_elements_by_css_selector(
                    'div.b_cards[iscorrectoption="True"]')[t].click()
                sleep()
            except:
                print('something went wrong|', end='')


def do_quiz_2():
    button_quiz = driver.find_elements_by_class_name('rq_button')
    sleep()
    for i in range(3):
        sleep()
        for i in range(len(button_quiz)):
            sleep()
            try:
                button_quiz = driver.find_elements_by_class_name('rq_button')
                button_quiz[i].click()
            except:
                print('The Cake is a lie|', end='')


def do_quiz_3():
    for d in range(10):
        sleep()
        button_quiz_3 = driver.find_elements_by_class_name(
            'btCardImg')
        sleep()
        button_quiz_3[1].click()


def get_points_pc():
    driver.get('https://www.bing.com/')
    sleep()
    points = driver.find_element_by_id('id_rc').text
    return points


def get_points_mobile():
    mobile_driver.get('https://www.bing.com/')
    sleep()
    mobile_driver.find_element_by_id('mHamburger').click()
    sleep()
    points = mobile_driver.find_element_by_id('fly_id_rc').text
    return points


def get_excel_data_mobile(counter_excel):
    points = get_points_mobile()
    first_day = datetime.date(2021, 6, 30)
    today = datetime.date.today()
    sub_date = today - first_day
    sub_date = sub_date.days + 2
    if counter_excel == 1:
        range = 'Laurin!A'+str(sub_date)
    if counter_excel == 2:
        range = 'Tim!A'+str(sub_date)
    if counter_excel == 3:
        range = 'Laurin_2!A'+str(sub_date)
    if counter_excel == 4:
        range = 'Marvin!A'+str(sub_date)
    date_sheets = today.strftime('%d.%m.%Y')
    values = [[date_sheets, points], ]
    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range,
        valueInputOption='USER_ENTERED', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')), '|', end='')
    print('sheets Done|', end='')


def get_excel_data_pc(counter_excel):

    points = get_points_pc()
    first_day = datetime.date(2021, 6, 30)
    today = datetime.date.today()
    sub_date = today - first_day
    sub_date = sub_date.days + 2
    if counter_excel == 1:
        range = 'Laurin!A'+str(sub_date)
    if counter_excel == 2:
        range = 'Tim!A'+str(sub_date)
    if counter_excel == 3:
        range = 'Laurin_2!A'+str(sub_date)
    if counter_excel == 4:
        range = 'Marvin!A'+str(sub_date)
    date_sheets = today.strftime('%d.%m.%Y')
    values = [[date_sheets, points], ]
    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range,
        valueInputOption='USER_ENTERED', body=body).execute()
    print('{0} cells updated'.format(result.get('updatedCells')), '|', end='')
    print('sheets Done|', end='')


for j in range(len(username_list)):
    driver = Edge(executable_path='msedgedriver.exe', options=edge_options)
    driver.get('https://bing.com')
    login_bing(counter_acc)
    scan_daily_task()
    print('daily task done|', end='')
    bing_pc_search()
    print('bing search done|', end='')
    mobil_search_todo = get_mobile_search_on_pc()
    if mobil_search_todo != 0:
        driver.quit()
        mobile_driver = get_mobile_driver()
        bing_mobile_login(counter_acc)
        bing_mobile_search()
        print('mobile search done|',)
        get_excel_data_mobile(counter_excel)
        mobile_driver.quit()
    else:
        get_excel_data_pc(counter_excel)
        driver.quit()
    print('\n', end='')
    if counter_acc == 0:
        print('\033[32m' + 'Laurin Done', end='')
        print('\033[39m')
    elif counter_acc == 1:
        print('\033[32m' + 'Tim Done', end='')
        print('\033[39m')
    elif counter_acc == 2:
        print('\033[32m' + 'Laurin_2 Done', end='')
        print('\033[39m')
    elif counter_acc == 3:
        print('\033[32m' + 'Marvin Done')
        print('\033[39m')
    counter_excel = counter_excel + 1
    counter_acc = counter_acc + 1
