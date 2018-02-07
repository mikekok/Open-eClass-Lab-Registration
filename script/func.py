# Dependencies
import config
import requests
from bs4 import BeautifulSoup as bs

# Session Setup
s = requests.Session()

# Login to your account
def login(username, password):
  payload = {
    'pass': password,
    'submit': '',
    'uname': username
  }
  s.get(config.URL)
  s.post(config.URL, data=payload)
  return

# Verify successful lab registration
def isRegistered():
  sourceTMP = s.get('%smodules/group/?course=%s' %(config.URL, config.COURSE))
  soupTMP = bs(sourceTMP.content, 'lxml')
  for group in soupTMP.find_all('td'):
    if (config.DATE['day'] in group.text and config.DATE['time']+'-' in group.text and 'η ομάδα μου' in group.text):
      return True
  return False

# Register for a lab
def register(day, time):
  # Labs Page Source Code
  groupsHTML = s.get('%smodules/group/?course=%s' %(config.URL, config.COURSE))
  # Beautiful Soup Setup
  soup = bs(groupsHTML.content, 'lxml')
  # Labs' Info Scraping
  a = ''
  for group in soup.find_all('td'):
    if (day in group.text and time+'-' in group.text and not 'η ομάδα μου' in group.text):
      reg_ele = group.find_next_siblings('td')[3]
      a = reg_ele.find('a')['href']
  # Registration
  if (a): s.get('%smodules/group/%s' %(config.URL, a))
  return
