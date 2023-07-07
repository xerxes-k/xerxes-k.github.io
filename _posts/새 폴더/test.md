```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
```


```python
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome()

driver.get("http://localhost:8888/tree")
driver.find_element(By.CSS_SELECTOR, '#password_input').send_keys('token')
driver.find_element(By.CSS_SELECTOR, '#login_submit').click()
nblist = driver.find_element(By.CSS_SELECTOR, '#notebook_list')
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(nblist))
row = driver.find_elements(By.CSS_SELECTOR, '.item_link')
main = driver.current_window_handle
for b in row:
    if b.text.endswith('ipynb'):
        b.click()
        # time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        menubar = driver.find_element(By.CSS_SELECTOR, '#filelink')        
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(menubar))
        driver.find_element(By.CSS_SELECTOR, '#filelink').click()
        dropdown = driver.find_elements(By.CSS_SELECTOR, '.dropdown-submenu')[2]        
        actions = ActionChains(driver)
        actions.move_to_element(dropdown).perform()
        md = driver.find_element(By.CSS_SELECTOR, '#download_markdown')        
        md.click()
        
        time.sleep(3)
        
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(main)   
        
```


    ---------------------------------------------------------------------------

    StaleElementReferenceException            Traceback (most recent call last)

    Cell In[41], line 14
         12 main = driver.current_window_handle
         13 for b in row:
    ---> 14     if b.text.endswith('ipynb'):
         15         b.click()
         16         # time.sleep(3)
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webelement.py:90, in WebElement.text(self)
         87 @property
         88 def text(self) -> str:
         89     """The text of the element."""
    ---> 90     return self._execute(Command.GET_ELEMENT_TEXT)["value"]
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webelement.py:395, in WebElement._execute(self, command, params)
        393     params = {}
        394 params["id"] = self._id
    --> 395 return self._parent.execute(command, params)
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webdriver.py:346, in WebDriver.execute(self, driver_command, params)
        344 response = self.command_executor.execute(driver_command, params)
        345 if response:
    --> 346     self.error_handler.check_response(response)
        347     response["value"] = self._unwrap_value(response.get("value", None))
        348     return response
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\errorhandler.py:245, in ErrorHandler.check_response(self, response)
        243         alert_text = value["alert"].get("text")
        244     raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
    --> 245 raise exception_class(message, screen, stacktrace)
    

    StaleElementReferenceException: Message: stale element reference: stale element not found
      (Session info: chrome=114.0.5735.199); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#stale-element-reference-exception
    Stacktrace:
    Backtrace:
    	GetHandleVerifier [0x00DDA813+48355]
    	(No symbol) [0x00D6C4B1]
    	(No symbol) [0x00C75358]
    	(No symbol) [0x00C787A1]
    	(No symbol) [0x00C799E1]
    	(No symbol) [0x00C79A80]
    	(No symbol) [0x00C9D2FD]
    	(No symbol) [0x00CBA73C]
    	(No symbol) [0x00C99A36]
    	(No symbol) [0x00CBAA94]
    	(No symbol) [0x00CCC922]
    	(No symbol) [0x00CBA536]
    	(No symbol) [0x00C982DC]
    	(No symbol) [0x00C993DD]
    	GetHandleVerifier [0x0103AABD+2539405]
    	GetHandleVerifier [0x0107A78F+2800735]
    	GetHandleVerifier [0x0107456C+2775612]
    	GetHandleVerifier [0x00E651E0+616112]
    	(No symbol) [0x00D75F8C]
    	(No symbol) [0x00D72328]
    	(No symbol) [0x00D7240B]
    	(No symbol) [0x00D64FF7]
    	BaseThreadInitThunk [0x75E30419+25]
    	RtlGetAppContainerNamedObjectPath [0x778C662D+237]
    	RtlGetAppContainerNamedObjectPath [0x778C65FD+189]
    


475bafb3bc6d163000bc1a873c01412598a743299505b0e5


```python
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
url_list = []
driver.get("http://localhost:8888/tree")
driver.find_element(By.CSS_SELECTOR, '#password_input').send_keys('475bafb3bc6d163000bc1a873c01412598a743299505b0e5')
driver.find_element(By.CSS_SELECTOR, '#login_submit').click()
nblist = driver.find_element(By.CSS_SELECTOR, '#notebook_list')
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(nblist))
row = driver.find_elements(By.CSS_SELECTOR, '.item_link')
for b in row:
    url = str(b.get_attribute('href'))
    if url.endswith('ipynb'):
        url_list.append(url)
        
for i in url_list:    
    driver.get(i)
    # driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    menubar = driver.find_element(By.CSS_SELECTOR, '#filelink')        
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(menubar))
    driver.find_element(By.CSS_SELECTOR, '#filelink').click()    
    dropdown = driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[3]        
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(dropdown))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()
    md = driver.find_element(By.CSS_SELECTOR, '#download_markdown')        
    md.click()
    
    time.sleep(3)
    
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # driver.get("http://localhost:8888/tree")
```


    ---------------------------------------------------------------------------

    UnexpectedAlertPresentException           Traceback (most recent call last)

    Cell In[57], line 21
         19 # driver.switch_to.window(driver.window_handles[1])
         20 time.sleep(1)
    ---> 21 menubar = driver.find_element(By.CSS_SELECTOR, '#filelink')        
         22 WebDriverWait(driver, 3).until(EC.element_to_be_clickable(menubar))
         23 driver.find_element(By.CSS_SELECTOR, '#filelink').click()    
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webdriver.py:740, in WebDriver.find_element(self, by, value)
        737     by = By.CSS_SELECTOR
        738     value = f'[name="{value}"]'
    --> 740 return self.execute(Command.FIND_ELEMENT, {"using": by, "value": value})["value"]
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webdriver.py:346, in WebDriver.execute(self, driver_command, params)
        344 response = self.command_executor.execute(driver_command, params)
        345 if response:
    --> 346     self.error_handler.check_response(response)
        347     response["value"] = self._unwrap_value(response.get("value", None))
        348     return response
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\errorhandler.py:244, in ErrorHandler.check_response(self, response)
        242     elif "alert" in value:
        243         alert_text = value["alert"].get("text")
    --> 244     raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
        245 raise exception_class(message, screen, stacktrace)
    

    UnexpectedAlertPresentException: Alert Text: {Alert text : 
    Message: unexpected alert open: {Alert text : }
      (Session info: chrome=114.0.5735.199)
    Stacktrace:
    Backtrace:
    	GetHandleVerifier [0x00DDA813+48355]
    	(No symbol) [0x00D6C4B1]
    	(No symbol) [0x00C75358]
    	(No symbol) [0x00CCCDAD]
    	(No symbol) [0x00CBA536]
    	(No symbol) [0x00C982DC]
    	(No symbol) [0x00C993DD]
    	GetHandleVerifier [0x0103AABD+2539405]
    	GetHandleVerifier [0x0107A78F+2800735]
    	GetHandleVerifier [0x0107456C+2775612]
    	GetHandleVerifier [0x00E651E0+616112]
    	(No symbol) [0x00D75F8C]
    	(No symbol) [0x00D72328]
    	(No symbol) [0x00D7240B]
    	(No symbol) [0x00D64FF7]
    	BaseThreadInitThunk [0x75E30419+25]
    	RtlGetAppContainerNamedObjectPath [0x778C662D+237]
    	RtlGetAppContainerNamedObjectPath [0x778C65FD+189]
    



```python

```
