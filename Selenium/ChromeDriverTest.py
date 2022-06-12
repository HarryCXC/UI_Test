# 第三章 /ChromeDriverTest
# 引入selenium import webdriver

from selenium import webdriver

# 声明驱动对象并打开浏览器
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com/")



