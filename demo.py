from selenium.webdriver import Chrome
from time import sleep
import unittest


class TestHello(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.base_url = 'http://192.168.0.238/'
        self.driver.maximize_window()
        self.driver.set_script_timeout(10)
        self.driver.implicitly_wait(10)

    def test_hello(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('ddzx')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('123')
        driver.find_element_by_tag_name('button').click()
        sleep(1)
        except_name = '调度中心负责人'
        actual_name = driver.find_element_by_xpath('//div[@class="info"]').text
        self.assertEqual(except_name, actual_name)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
