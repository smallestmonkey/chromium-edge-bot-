from selenium import webdriver
import time
import login_data
import random


path_wortlist = 'wordlist.txt'
username_list = login_data.get_username_login()
password_list = login_data.get_password_login()
maxwait = 3
minwait = 2
shortmin = 0.2
shortmax = 1


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
    print(number)
    return int(number)


def get_mobile_search():
    mobile_driver.get('https://www.bing.com///rewardsapp///flyout')

    element = mobile_driver.find_element_by_xpath(
        '//*[@id="modern-flyout"]/div/div[5]/div/div[2]/div[3]/div/div').text.split("/")
    number = (int(element[1]) - int(element[0]))/3
    mobile_driver.get('https://www.bing.com/')
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


def login_bing(counter_acc):
    try:
        driver.get('https://www.bing.com/')
        sleep()
        try:
            driver.find_element_by_id('bnp_btn_accept').click()
        except:
            print('error 23123 no cookie button found', end='')
        sleep()
        try:
            driver.find_element_by_id('id_s').click()
            sleep()
            driver.find_element_by_class_name('id_link_text').click()
            sleep()
            driver.find_element_by_id('id_s').click()
            shortsleep()
        except:
            print('', end='')
        sleep()
        driver.find_element_by_id('i0116').send_keys(
            username_list[counter_acc])
        sleep()
        driver.find_element_by_id('idSIButton9').click()
        sleep()
        try:
            driver.find_element_by_id('msaTile').click()
            sleep()
        except:
            print('', end='')
        driver.find_element_by_id('i0118').send_keys(
            password_list[counter_acc])
        sleep()
        driver.find_element_by_id('idSIButton9').click()
    except:
        print('big login error restart login')
        login_bing()


def get_mobile_driver():
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "mobileEmulation", mobile_emulation)
    return webdriver.Chrome('chromedriver.exe', options=chrome_options)


def bing_mobile_login(counter_acc):
    mobile_driver.get('https://www.bing.com/')
    sleep()
    try:
        mobile_driver.find_element_by_id('bnp_btn_accept').click()
    except:
        print('error 1903481729471 no cookie button found', end='')
    sleep()
    mobile_driver.find_element_by_id('mHamburger').click()
    sleep()
    mobile_driver.find_element_by_id('hb_s').click()
    sleep()
    # dont know what is happening some time works tomtiens not
    mobile_driver.find_element_by_id(
        'i0116').send_keys(username_list[counter_acc])
    sleep()
    mobile_driver.find_element_by_id('idSIButton9').click()
    sleep()
    try:
        mobile_driver.find_element_by_id('msaTile').click()
        sleep()
    except:
        print('', end='')
    mobile_driver.find_element_by_id(
        'i0118').send_keys(password_list[counter_acc])
    sleep()
    mobile_driver.find_element_by_id('idSIButton9').click()
    sleep()


def scan_daily_task():
    driver.get('https://www.bing.com///rewardsapp///flyout')
    list_len = len(driver.find_elements_by_class_name('rw-si.add'))
    print("List_len: " + str(list_len) + '|', end='')
    while list_len != 0:
        driver.find_elements_by_class_name('rw-si.add')[0].click()
        bing_do_task()
        driver.get('https://www.bing.com///rewardsapp///flyout')
        sleep()
        list_len = len(driver.find_elements_by_class_name('rw-si.add'))
        print("List_len: " + str(list_len) + '|', end='')
    driver.find_element_by_class_name('i-h.rw-sh.fp_row').click()
    list_len = len(driver.find_elements_by_class_name('rw-si.add'))
    print("List_len: " + str(list_len) + '|', end='')
    while list_len != 0:
        driver.find_elements_by_class_name('rw-si.add')[0].click()
        bing_do_task()
        driver.get('https://www.bing.com///rewardsapp///flyout')
        sleep()
        driver.find_element_by_class_name('i-h.rw-sh.fp_row').click()
        list_len = len(driver.find_elements_by_class_name('rw-si.add'))
        print("List_len: " + str(list_len) + '|', end='')


def bing_do_task():
    sleep()  # eddit
    sleep()
    try:
        driver.find_element_by_id('rqStartQuiz')
        quiz = True
    except:
        quiz = False
        print('', end='')
    try:
        driver.find_element_by_id('btoption0')
        survery = True
    except:
        survery = False
        print('', end='')

    if survery == True:

        driver.find_element_by_id('btoption0').click()
        sleep()

    if quiz == True:
        driver.find_element_by_id('rqStartQuiz').click()
        sleep()
        try:
            driver.find_element_by_class_name('btCardImg')
            do_quiz_3()
        except:
            print('', end='')
        try:
            driver.find_elements_by_class_name("bt_cardText")
            do_quiz_1()
        except:
            print('', end='')
        try:
            driver.find_elements_by_class_name('rqOption')
            do_quiz_2()
        except:
            print('', end='')


def do_quiz_1():
    list_len = len(driver.find_elements_by_css_selector(
        'div.b_cards[iscorrectoption="True"]'))
    print("List_len: " + str(list_len) + ' |', end='')
    for i in range(3):  # 3 ?
        time.sleep(7)  # hin
        for t in range(len(driver.find_elements_by_css_selector('div.b_cards[iscorrectoption="True"]'))):
            sleep()

            try:
                driver.find_elements_by_css_selector(
                    'div.b_cards[iscorrectoption="True"]')[t].click()
                sleep()  # hinzugefügt
            except:
                print('something went wrong |', end='')


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
                print('The Cake is a lie |', end='')


def do_quiz_3():
    for d in range(10):
        sleep()
        button_quiz_3 = driver.find_elements_by_class_name(
            'btCardImg')
        sleep()
        button_quiz_3[1].click()


counter_acc = 0
for j in range(len(username_list)):
    driver = webdriver.Edge('msedgedriver.exe')
    driver.get('https://bing.com')
    login_bing(counter_acc)
    scan_daily_task()
    print('daily task done |', end='')
    bing_pc_search()
    print('bing search done |', end='')
    driver.quit()

    mobile_driver = get_mobile_driver()
    bing_mobile_login(counter_acc)
    bing_mobile_search()
    print('mobile search done |', end='')
    mobile_driver.quit()
    counter_acc = counter_acc + 1
# driver.find_element_by_id('id_rc').text()
