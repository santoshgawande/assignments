import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
import xml.etree.ElementTree as et


class PythonRegister(unittest.TestCase,Options):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.loksatta.com")
        d=driver.find_element_by_xpath("/html/body/div[7]/article/div[1]/div[1]/h1/a").get_attribute("href")
        driver.get(d)
        title=driver.find_element_by_xpath("//*[@id='headline']").text

        #popup=driver.find_element_by_xpath("//*[@id='x']").clear
        para= driver.find_element_by_xpath("//div[@id='rightsec']/p")
        para2= driver.find_element_by_xpath("//div[@id='rightsec']/p[2]")
        para3= driver.find_element_by_xpath("//div[@id='rightsec']/p[3]")
        para4= driver.find_element_by_xpath("//div[@id='rightsec']/p[4]")
        time.sleep(5)
     
        print("Title:\n")
        print(title)
        print("Paragraph:\n")
        print(para.text)
        print(para2.text)
        print(para3.text)
        print(para4.text)
        #print(d)
        print("comment:\n")
        
        # create the file structure
        data = et.Element('data')   
        htmldata = et.SubElement(data, 'htmldata')
        heading = et.SubElement(htmldata,"heading")
        contents = et.SubElement(htmldata,"contents")
        heading.set("name","heading")
        contents.set("name","contents")
        heading.text = title
        #print(m)

        contents.text =para2.text

        '''tree = et.parse('news.xml')
        a = root.find('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(b, 'c')
        c.text = 'text3'
        '''
        # create a new XML file with the results
        mydata = et.tostring(data)
        myfile = open("news.xml", "w")
        #myfile.write('<?xml version="1.0" encoding="UTF-8"?>')  
        myfile.write(mydata)  

    def tearDown(self):
         self.driver.close()


if __name__ == "__main__":
    unittest.main()