#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time, datetime, os
import json
from getpass import getpass
from apscheduler.schedulers.blocking import BlockingScheduler
from halo import Halo
from pyvirtualdisplay import Display

Q1_table = {
    "是，医院已确诊、正在治疗": 'a45ee799-9d9e-4347-953c-b14bdd53578e',
    "是，曾经确诊、现已治愈": '08278ee8-9bd8-45d2-9397-310ecddbf9d3',
    "否，正在进行医学隔离观察、待确诊或待排除": '4e205912-7304-4e35-b4c3-f9b95c9078e2',
    '否，未感染': '6fb3abcd-1aa3-4b6f-8254-62426dd36f37'
}
Q2_table = {
    "是，有身处湖北": "1395efb6-1d47-49b1-adac-64ae647425d5",
    "否，没有身处湖北": "16b61a88-9102-45f2-bbee-57ea3af8810f"
}

Q3_table = {
    "是，有接触": "b55d5245-2bae-4d0d-8292-86761e7f15f6",
    "否，无接触": "e87d35b4-1b2c-4153-90bd-67efd6367007"
}

Q4_table = {
    "有症状，现已排除感染或疑似感染": "cff697a9-97dd-4061-aaa9-e22afd4a8f5a",
    "有症状，尚未排除感染或疑似感染": "bc71f6d7-e996-4427-9fab-d44b954e6b17",
    "无以上状况": "c111ad09-e63a-484d-b88f-7f0b6a6c979b"
}

class clockin(object):

    def __init__(self, config):
        self.StudentId = config['StudentId']
        self.Name = config['Name']
        self.StuCard = config['StuCard']
        # self.Sex = config['Sex']
        # self.SpeType = config['SpeType']
        # self.CollegeNo = config['CollegeNo']
        # self.SpeGrade = config['SpeGrade']
        # self.SpecialtyName = config['SpecialtyName']
        # self.ClassName = config['ClassName']
        self.MoveTel = config['MoveTel']
        self.FaProvince = config["FaProvince"]
        self.FaCity = config["FaCity"]
        self.FaCounty = config["FaCounty"]
        self.FaComeWhere = config["FaComeWhere"]
        self.ProvinceName = config["ProvinceName"]
        self.CityName = config["CityName"]
        self.CountyName = config["CountyName"]
        self.ComeWhere = config["ComeWhere"]
        self.Q1 = config["Q1"]
        self.Q2 = config["Q2"]
        self.Q3 = config["Q3"]
        self.Q4 = config["Q4"]
        self.other = config["other"]
        self.login_url = "http://xgsys.swjtu.edu.cn/SPCP/Web/UserLogin.aspx"
        display = Display(visible=0, size=(1920, 1440))
        display.start()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1440)
        # self.default = False

    def is_Element(self, element):
        try:
            self.driver.find_element_by_class_name(element)
            return True
        except:
            return False

    def login(self):
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(30)


        self.driver.find_element_by_id('StudentId').send_keys(self.StudentId)
        time.sleep(0.4)
        self.driver.find_element_by_id('Name').send_keys(self.Name)
        time.sleep(0.4)
        self.driver.find_element_by_id('IdCard').send_keys(self.StuCard)
        time.sleep(0.4)
        code = self.driver.find_element_by_id('code-box').text
        time.sleep(0.4)
        self.driver.find_element_by_id('codeInput').send_keys(code)
        time.sleep(0.4)
        self.driver.find_element_by_id('Submit').click()
        self.driver.implicitly_wait(5)

        # logging double layui
        # flag1 = self.is_Element('layui-layer-btn0')
        # flag2 = self.is_Element('layui-layer-btn1')
        #
        # if flag1:
        #     if flag2:
        #         if self.default:
        #             self.driver.find_element_by_id('layui-layer1').click()  # 先找到父节点，防止失焦
        #             self.driver.find_element_by_class_name('layui-layer-btn0').click()
        #             self.driver.implicitly_wait(5)
        #             return 'un_uid_and_continue'  # 测试用
        #         else:
        #             self.driver.close()
        #             return 'un_uid_and_exit'
        #     else:
        #         self.driver.find_element_by_id('layui-layer1').click()  # 先找到父节点，防止失焦
        #         self.driver.find_element_by_class_name('layui-layer-btn0').click()
        #         self.driver.close()
        #         return 'is_writted'

        # no-id return layui, have done return
        # print(self.driver.current_window_handle)
        # self.driver.switch_to.window(self.driver.current_window_handle)

        flag1 = self.is_Element('layui-layer-btn0')
        flag2 = self.is_Element('layui-layer-btn1')

        if flag1 and flag2:
            self.driver.close()
            return 'un_uid_and_exit'

        self.driver.find_element_by_id("platfrom2").click()
        if self.is_Element('layui-m-layerchild.layui-m-anim-scale'):  # 空格需置换成.
            self.driver.close()
            return "is_writted"

        return

    # 极端情况测试
    # def for_iter(self):
    #     time.sleep(3)
    #     test_flag = self.is_Element('layui-layer-btn0')
    #     if test_flag:
    #         self.driver.find_element_by_id('layui-layer1').click()  # 先找到父节点，防止失焦
    #         self.driver.find_element_by_class_name('layui-layer-btn0').click()
    #         self.driver.close()
    #         return 'is_writted'

    def select_one(self, name, text):
        s = Select(self.driver.find_element_by_name(name))
        s.select_by_visible_text(text)

    def is_selected(self, name):
        element_ls = self.driver.find_elements_by_name(name)
        for ele in element_ls:
            if ele.is_selected():
                return True
        return False

    def fillin(self):

        # if self.driver.find_element_by_name("radioSEX").is_enabled():
        #     if not self.driver.find_element_by_name("radioSEX").is_selected():
        #         self.driver.find_element_by_id("NSex" if self.Sex == "男" else "RSex").click()
        #     time.sleep(0.4)

        # if self.driver.find_element_by_id('SpeType').is_enabled():
        #     if not self.driver.find_element_by_id('SpeType').is_selected():
        #         self.select_one('SpeType', self.SpeType)
        #     time.sleep(0.4)
        # if self.driver.find_element_by_id('CollegeNo').is_enabled():
        #     if not self.driver.find_element_by_id('CollegeNo').is_selected():
        #         self.select_one('CollegeNo', self.CollegeNo)
        #     time.sleep(0.4)
        # if self.driver.find_element_by_id('SpeGrade').is_enabled():
        #     if not self.driver.find_element_by_id('SpeGrade').is_selected():
        #         self.select_one('SpeGrade', self.SpeGrade)
        #     time.sleep(0.4)
        # if self.driver.find_element_by_id('SpecialtyName').is_enabled():
        #     if len(self.driver.find_element_by_id('SpecialtyName').get_attribute('value')) == 0:
        #         self.driver.find_element_by_id('SpecialtyName').clear()
        #         self.driver.find_element_by_id('SpecialtyName').send_keys(self.SpecialtyName)
        #     time.sleep(0.4)
        #
        # if self.driver.find_element_by_id('ClassName').is_enabled():
        #     if len(self.driver.find_element_by_id('ClassName').get_attribute('value')) == 0:
        #         self.driver.find_element_by_id('ClassName').clear()
        #         self.driver.find_element_by_id('ClassName').send_keys(self.ClassName)
        #     time.sleep(0.4)

        if len(self.driver.find_element_by_id('MoveTel').get_attribute('value')) == 0:
            self.driver.find_element_by_id('MoveTel').clear()
            self.driver.find_element_by_id('MoveTel').send_keys(self.MoveTel)
        time.sleep(0.4)

        if not self.driver.find_element_by_name('Province').is_selected():
            self.select_one('Province', self.ProvinceName)
            time.sleep(0.4)
            if not self.driver.find_element_by_name('City').is_selected():
                self.select_one('City', self.CityName)
                time.sleep(0.4)
                if not self.driver.find_element_by_name('County').is_selected():
                    self.select_one('County', self.CountyName)
                    time.sleep(0.4)

        if len(self.driver.find_element_by_name('ComeWhere').get_attribute('value')) == 0:
            self.driver.find_element_by_name('ComeWhere').clear()
            self.driver.find_element_by_name('ComeWhere').send_keys(self.ComeWhere)
        time.sleep(0.4)

        if not self.driver.find_element_by_name('FaProvince').is_selected():
            self.select_one('FaProvince', self.FaProvince)
            time.sleep(0.4)
            if not self.driver.find_element_by_name('FaCity').is_selected():
                self.select_one('FaCity', self.FaCity)
                time.sleep(0.4)
                if not self.driver.find_element_by_name('FaCounty').is_selected():
                    self.select_one('FaCounty', self.FaCounty)
                    time.sleep(0.4)

        if len(self.driver.find_element_by_name('FaComeWhere').get_attribute('value')) == 0:
            self.driver.find_element_by_name('FaComeWhere').clear()
            self.driver.find_element_by_name('FaComeWhere').send_keys(self.FaComeWhere)
        time.sleep(0.4)

        if not self.is_selected("radio_1"):
            self.driver.find_element_by_id(Q1_table[self.Q1]).click()
        time.sleep(0.4)
        if not self.is_selected("radio_2"):
            self.driver.find_element_by_id(Q2_table[self.Q2]).click()
        time.sleep(0.4)
        if not self.is_selected("radio_3"):
            self.driver.find_element_by_id(Q3_table[self.Q3]).click()
        time.sleep(0.4)
        if not self.is_selected("radio_4"):
            self.driver.find_element_by_id(Q4_table[self.Q4]).click()
        time.sleep(0.4)
        if len(self.driver.find_element_by_name("Other").get_attribute('value')) == 0:
            self.driver.find_element_by_id('Other').clear()
            self.driver.find_element_by_id('Other').send_keys(self.other)
        time.sleep(0.4)

        self.driver.find_element_by_id('ckCLS').click()

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('SaveBtnDiv').click()


def main(config):
    print("\n[Time] %s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("开始创建登记任务")
    spinner = Halo(text='Loading', spinner='dots')
    spinner.start('正在创建登记实例...')
    ci = clockin(config)
    spinner.succeed('创建登记实例成功')

    spinner.start(text='登录...')

    try:
        log = ci.login()
        if log == 'un_uid_and_continue':
            spinner.info('学号不存在，测试登录')
        elif log == 'un_uid_and_exit':
            spinner.fail('学号不存在，请修改配置')
            return
        spinner.succeed('登陆成功')
    except Exception as err:
        spinner.fail(str(err))
        return

    if log == 'is_writted':
        spinner.info('今日已登记，无需再次登记')
        return

    # log = ci.for_iter()
    # if log == 'is_writted':
    #     spinner.info('今日已登记，无需再次登记')
    #     return

    spinner.start(text='打卡中...')

    try:
        ci.fillin()
        spinner.succeed('打卡成功')
        time.sleep(5)
        ci.driver.close()
    except Exception as err:
        spinner.fail(str(err))
        spinner.fail('打卡失败')
        return


if __name__ == '__main__':
    if os.path.exists('./config.json'):
        configs = json.loads(open('./config.json', 'r', encoding='utf-8').read())
        hour = configs["schedule"]["hour"]
        minute = configs["schedule"]["minute"]
    else:
        print('请先建立config文件...')
        exit()
    # else:
    #     StudentId = input("输入学号: ")
    #     Name = input("输入姓名：")
    #     StuCard = getpass('输入身份证后6位: ')
    #     print("请输入定时时间（默认每天8:00）")
    #     hour = input("hour: ") or 8
    #     minute = input("minute: ") or 0

    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(main, 'cron', args=[configs['parameters']], minute='*/1')
    scheduler.add_job(main, 'cron', args=[configs['parameters']], hour=hour, minute=minute)
    print('已启动定时程序，每天 %02d:%02d 为您打卡' % (int(hour), int(minute)))
    print('Press Ctrl+{0} to exit'.format('break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()