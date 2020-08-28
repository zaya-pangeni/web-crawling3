from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\HP\Desktop\chromedriver.exe')
driver.get("https://www.getprice.com.au/")

products = driver.find_elements_by_xpath('//div[@class="desc"]')

number1=len(products)

with open("shopping.txt","w") as f:
    for i in range(number1):
      f.write(products[i].text + "\n")

driver.close()