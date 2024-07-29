import yt_dlp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def download_youtube_video(url, save_path='./vids'):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best',
        'noplaylist': True  # Download only the video, not the playlist
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"Downloaded successfully!")



def get_links(channel_url:str = "https://m.youtube.com/@SwaroopVITB"):
    # Set up Selenium WebDriver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    # Fetch the page
    driver.get(channel_url)

    # Extract the page source
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all anchor tags
    anchors = soup.find_all('a', id= 'video-title')
    href_list = [a.get('href') for a in anchors if a.get('href')]
    driver.quit()
    return href_list

def download_content(url_list:list, n:int, path = '.'):
    print("Links are being downloaded!")
    for i in range(n):
        print(f"DOWNLOADING {i+1} of {n}")
        download_youtube_video(f"https://www.youtube.com{url_list[i]}", save_path= path)



if __name__ == "__main__":
    urls =  get_links()
    download_content(urls, 1, "./vids")