# selenium 셀레니움에서 새 탭으로 전환

셀레니움을 쓸 때 새 탭을 열고 그 탭에서 작업할 일이 있으면 셀레니움 드라이버에게 새로 열린 탭에서 작업을 할 거라고 따로 알려줘야 한다


```python
from selenium import webdriver
driver = webdriver.Chrome()

#탭의 번호를 넣어서 전환한다
driver.switch_to.window(driver.window_handles[1])
```
