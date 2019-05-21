# imageSpider
an image spider of baidu based on python selenium version Chrome

## Direction<br>
before use, make sure you get everything in need<br>
### 1. python 3.x (not sure if 2.x works)<br>	 
with modules installed by pip:<br>		 
> $ pip install selenium<br>	 
> $ pip install argparse<br>	 
### 2. Chrome & chromedriver<br>
make sure your chromedriver's version get correct with your current Chrome Browser<br>
teleport for chromedriver: http://npm.taobao.org/mirrors/chromedriver/ <br>
and the chromedriver.exe into where your Chrome and python locates:<br>
me for example:<br>
C:\Program Files (x86)\Google\Chrome\Application <br>
C:\Users\Shinelon\AppData\Local\Programs\Python\Python37 <br>
### 3. run the code <br>
> $ python spider.py --key_word=husky --number=50 --dst_dir=./sample/husky --save_name=husky

here are the samples(already deleted the bad images): <br>
![preview](./preview.png)
