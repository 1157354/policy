from selenium import webdriver
from selenium.webdriver import ActionChains

brower = webdriver.Chrome('/Users/tian/Downloads/chromedriver')
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
brower.get(url)
brower.switch_to.frame('iframeResult')
source = brower.find_element_by_css_selector('#draggable')
target = brower.find_element_by_css_selector('#droppable')
actions = ActionChains(brower)
actions.drag_and_drop(source,target)
actions.perform()
