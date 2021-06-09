from selenium import webdriver
import time
import login_data
import random

path_wortlist = 'wordlist.txt'
bing_username = login_data.bing_tim_username()
bing_password = login_data.bing_tim_password()
bing_pc_search_count = 31
bing_mobile_search_count = 20


def bing_pc_search():
    words = open(path_wortlist).read().split('\n')
    bing_search_field = driver.find_element_by_id('sb_form_q')
    time.sleep(1)
    bing_search_field.send_keys(random.choice(words) + ' ')
    time.sleep(1)
    bing_search_field.submit()
    time.sleep(1)


def login_bing():
    driver.get('https://www.bing.com/')
    time.sleep(10)
    try:
        driver.find_element_by_id('bnp_btn_accept').click()
    except:
        print('error 23123 no cookie button found')
    time.sleep(1)
    driver.find_element_by_id('id_s').click()
    time.sleep(2)
    driver.find_element_by_id('i0116').send_keys(bing_username)
    time.sleep(1)
    driver.find_element_by_id('idSIButton9').click()
    time.sleep(2)
    try:
        driver.find_element_by_id('msaTile').click()
        time.sleep(5)
    except:
        print('its not jonas')
    driver.find_element_by_id('i0118').send_keys(bing_password)
    time.sleep(1)
    driver.find_element_by_id('idSIButton9').click()


def get_mobile_driver():
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    return webdriver.Chrome('chromedriver.exe', options=chrome_options)


def bing_mobile_login():
    mobile_driver.get('https://www.bing.com/')
    time.sleep(8)
    try:
        mobile_driver.find_element_by_id('bnp_btn_accept').click()
    except:
        print('error 1903481729471 no cookie button found')
    time.sleep(1)
    mobile_driver.find_element_by_id('mHamburger').click()
    time.sleep(2)
    mobile_driver.find_element_by_id('hb_s').click()
    time.sleep(1)
    mobile_driver.find_element_by_id('i0116').send_keys(bing_username)
    time.sleep(1)
    mobile_driver.find_element_by_id('idSIButton9').click()
    time.sleep(2)
    try:
        mobile_driver.find_element_by_id('msaTile').click()
        time.sleep(5)
    except:
        print('its not jonas')
    mobile_driver.find_element_by_id('i0118').send_keys(bing_password)
    time.sleep(1)
    mobile_driver.find_element_by_id('idSIButton9').click()
    time.sleep(3)


def bing_mobile_search():
    words = open(path_wortlist).read().split('\n')
    bing_search_mobile_field = mobile_driver.find_element_by_id('sb_form_q')
    time.sleep(1)
    bing_search_mobile_field.send_keys(random.choice(words) + ' ')
    time.sleep(3)
    bing_search_mobile_field.submit()
    time.sleep(1)


def bing_do_task():
    time.sleep(3)
    try:
        driver.find_element_by_id('rqStartQuiz')
        quiz = True
    except:
        quiz = False
        print('no quiz')
    try:
        driver.find_element_by_id('btoption0')
        survery = True
    except:
        survery = False
        print('no survey ')

    if survery == True:

        driver.find_element_by_id('btoption0').click()
        time.sleep(5)
    for z in range(1):
        print(z)
        if quiz == True:
            driver.find_element_by_id('rqStartQuiz').click()
            try:
                driver.find_element_by_id('rqAnswerOption0')
                quiz_2 = True
                break
            except:
                print('quiz 1 ')
            button_quiz = driver.find_elements_by_class_name('bt_cardText')
            time.sleep(3)
            for i in range(3):
                time.sleep(4)
                for i in range(len(button_quiz)):
                    time.sleep(3)
                    try:
                        button_quiz = driver.find_elements_by_class_name(
                            'bt_cardText')
                        button_quiz[i].click()
                    except:
                        print('error1001')
    if quiz_2 == True:
        for j in range(3):
            time.sleep(3)
            for w in range(4):
                try:
                    time.sleep(2)
                    button_quiz_2 = driver.find_elements_by_class_name(
                        'rqOption')
                    button_quiz_2[w].click()

                except:
                    print('a wizzard has appeard')


def do_bing_daily_task():
    counter_bing_task = 0
    counter_bing_task_2 = 0
    for z in range(7):
        time.sleep(4)
        driver.get('https://www.bing.com///rewardsapp///flyout')
        time.sleep(4)
        complet_element = driver.find_elements_by_class_name('complete')
        length_complet = len(complet_element)
        promo_count = driver.find_elements_by_class_name('promo_cont')
        if length_complet == 3 or len(promo_count) == 0:
            try:
                driver.find_element_by_class_name('i-h').click()
                print(z)
                time.sleep(3)
                print(counter_bing_task_2)
                promo_count = driver.find_elements_by_class_name('promo_cont')
                time.sleep(1)
                promo_count[0].click()
                counter_bing_task_2 = counter_bing_task_2 + 1
                bing_do_task()
            except:
                print('error 74861896')

        else:
            try:
                promo_count = driver.find_elements_by_class_name('promo_cont')
                promo_count[counter_bing_task].click()
                counter_bing_task = counter_bing_task + 1
                bing_do_task()
            except:
                length_complet == 3
                z = 3
                print('eror 3123718903717')


#driver = webdriver.Edge('msedgedriver.exe')
driver = webdriver.Chrome('chromedriver.exe')
login_bing()
for i in range(bing_pc_search_count):
    bing_pc_search()
print('pc Search done')
do_bing_daily_task()
print('daily task finish')
driver.quit()

mobile_driver = get_mobile_driver()
bing_mobile_login()
for x in range(bing_mobile_search_count):
    bing_mobile_search()
print('mobile search done ')
mobile_driver.quit()


# https://www.bing.com/search?q=Was%20ist%20Sport?&rnoreward=1&mkt=DE-DE&FORM=ML12JG&skipopalnative=true&rqpiodemo=1&filters=BTEPOKey:%22REWARDSQUIZ_DEDE_MicrosoftRewardsQuizDS20210526%22%20BTROID:%22Gamification_DailySet_DEDE_20210526_Child2%22%20BTROEC:%220%22%20BTROMC:%2230%22
# https://www.bing.com/search?q=Europa&rnoreward=1&mkt=DE-DE&FORM=ML12JG&skipopalnative=true&rqpiodemo=1&filters=BTEPOKey:%22REWARDSQUIZ_DEDE_ThisOrThat_Europe_Capitals_B_M_S_EB_20210607%22%20BTROID:%22Gamification_DailySet_DEDE_20210607_Child2%22%20BTROEC:%220%22%20BTROMC:%2250%22%20BTROQN:%220%22
# https://www.bing.com/search?q=Kochen%20lernen%20Videos&rnoreward=1&mkt=DE-DE&FORM=ML12JG&skipopalnative=true&rqpiodemo=1&filters=BTEPOKey:%22REWARDSQUIZ_DEDE_MicrosoftRewardsQuizDS20210609%22%20BTROID:%22Gamification_DailySet_DEDE_20210609_Child2%22%20BTROEC:%220%22%20BTROMC:%2230%22
# https://www.bing.com/search?q=Kochen%20lernen%20Videos&rnoreward=1&mkt=DE-DE&FORM=ML12JG&skipopalnative=true&rqpiodemo=1&filters=BTEPOKey:%22REWARDSQUIZ_DEDE_MicrosoftRewardsQuizDS20210609%22%20BTROID:%22Gamification_DailySet_DEDE_20210609_Child2%22%20BTROEC:%220%22%20BTROMC:%2230%22
