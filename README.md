# JustDial_Scapper
This is a data scraper based on BeautifulSoup and Selenium frameworks suitable for dynamic scraping. This scraper is suitable for the site which has lazy loading features such as data loads and populates on user scrolling. It will extract all the data until the scroll is complete and save it as a JSON file.
 <br>    
**Installation:**  
Install Python3  
Install BeautifulSoup  
Install Selenium  
Install webdriver that support your browser<br>

Run the file :
>python3 -W ignore justdial.py
<br>
There will be a new chrome window with the website required to extract the data, so you have to scroll until all data get loaded. after sometime you can check a  file (data.json) is created which contains the extracted data. 
This is just for one page lazy loading it can be extended to extract the data of all pages corresponding to particular website.
