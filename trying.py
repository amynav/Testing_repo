from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
import datetime

logname = "Trying"+datetime.date.today().strftime("%d-%m-%Y")+".log"
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)


chrome_driver_path = "C:/Support/chromedriver.exe"
logging.info(chrome_driver_path)
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://www.python.org")
search_tab = driver.find_element_by_xpath("//input[(@id='id-search-field') and (@name='q')]")
print("id of bsearch tab is: " + search_tab.get_attribute('id'))
logging.info("id of bsearch tab is: " + search_tab.get_attribute('id'))
search_tab.clear()
search_tab.send_keys("python 2.7")
go_btn = driver.find_element_by_xpath("//button[(@type='submit') and (contains(text(),'GO'))]")
go_btn.click()
#ques = driver.find_element_by_xpath("//a[@value='Questions')]")
#print("question tab got" + ques)
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()
#driver.quit()