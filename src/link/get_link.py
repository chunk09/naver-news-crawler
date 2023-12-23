import requests
from bs4 import BeautifulSoup

def get_links(url: str) -> list[str]:
  link_list: list[str] = []
  response: requests.Response

  try:
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    })
  except:
    print("Get error")

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a")

    i = 0

    try:
      for link in links:
        if i % 2 == 0:
        # print(title.text)
          url = link.get("href")

          if "article" in url:
            if "https" in url:
              link_list.append(url)
            else:
              link_list.append("https://n.news.naver.com" + url)
  
        i += 1
    except:
        pass

  return list(set(link_list)) # set() 중복 제거, 그 대신 순서가 바뀜