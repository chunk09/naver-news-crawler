from link import get_link as gl
from bs4 import BeautifulSoup
import requests
import csv

URL = "https://news.naver.com/"

# def get_sublinks(link: str) -> list[str]:
#   sub_links = gl.get_links(link)
#   return sub_links

def main():
  mainlinks = gl.get_links(URL)
  sublinks: list[str] = []
  links: list[str] = []

  f = open('news.csv','w', newline='')
  wr = csv.writer(f)

  for mainlink in mainlinks:
    for sublink in gl.get_links(mainlink):
      sublinks.append(sublink)

  links = list(set(mainlinks + sublinks))

  i = 0

  for link in links:
    i += 1

    try:
      response = requests.get(link, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
      })

      if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.select("#title_area")

        for title in titles:
          print("title:", title.text)
          print("link:", link, end="\n\n")

          wr.writerow([i, title.text, link])
    except:
      pass

if __name__ == "__main__":
  main()
