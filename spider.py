#coding=utf-8
import os
import requests
import re
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def spider(url, number ,dst_dir, save_name):    
    if(not os.path.exists(dst_dir)):
        os.mkdir(dst_dir)
        print("no %s exists and now created one...")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable_gpu')
    driver = webdriver.Chrome(options=options)
    dst_list = os.listdir(dst_dir)    
    i = len(dst_list)  
    if(i>number):
        print("current number of images is beyond the need")
        return
    driver.get(url)
    first_pic = driver.find_element_by_class_name("imgitem").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    while(i<number):
        i+=int(1)
        try:
            pic = driver.find_element_by_class_name("currentImg").get_attribute("src")
        except Exception as err:
            print("cannot get any more images from the current website\n")
            break
        try: 
            r = requests.get(pic, timeout=5)
        except Exception as err:
            print("download failed: \n%s"%(err))
            continue
        with open(dst_dir+'/%s_%04d.jpg'%(save_name,i), 'wb') as f:
            f.write(r.content)        
            print("downloaded %d images already: %s"%(i,pic))    
        next_page = driver.find_element_by_class_name("img-next").click()
        time.sleep(3)   
        driver.switch_to.window(driver.window_handles[1])
    driver.quit()
    print("\n download accomplished >>")
    
    
parser = argparse.ArgumentParser(description='Image Spider')
parser.add_argument('--key_word',dest='key_word',required=True,help='key word')
parser.add_argument('--number',dest='number',default=50,type=int,help='number of images to download')
parser.add_argument('--dst_dir',dest='dst_dir',required=True, help='out path to save the images')
parser.add_argument('--save_name',dest='save_name',required=True,help='save name')
args = parser.parse_args() 

if __name__ == '__main__':
    spider("http://image.baidu.com/search/index?tn=baiduimage&word="+args.key_word, args.number, args.dst_dir, args.save_name)
