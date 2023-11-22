import urllib.request

import re

url = input("Enter the website without any forward-slash at the end: ")

mobileNumbPattern = re.compile(r"\d\d\d\d\d\d\d\d\d\d")

emailPattern = re.compile(r"[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z0-9._]+")

linkPattern = re.compile(r'href=["\'](\.\./.*?)["\']')

webPages = [url]

visitedPages = []

while(len(webPages) != 0):
    
    currUrl = webPages.pop()

    if(currUrl in visitedPages):
        continue

    try:
        print(f"crawling: {currUrl}")

        data = urllib.request.urlopen(currUrl)

        visitedPages.append(currUrl)

        html = data.read().decode('utf-8')

        links = linkPattern.findall(html)
        
        for link in links:
            if(not(
                link.endswith(".PDF") or 
                link.endswith(".pdf") or 
                link.endswith(".docx") or 
                link.endswith(".png") or 
                link.endswith(".jpg") or
                link.endswith(".jpeg") or
                link.endswith(".mp4") or
                link.endswith(".css") or
                link.endswith(".zip") or
                link.endswith(".JPG"))):
                    webPages.append(url+link[2:])
        
        foundPhoneNumbs = mobileNumbPattern.findall(html)

        f1 = open("crawled-phn-numbs.txt", "a")

        for phnNumb in foundPhoneNumbs:
             f1.write(phnNumb)
             f1.write("\n")

        f1.close()

        foundEmails = emailPattern.findall(html)

        f2 = open("crawled-emails.txt", "a")

        for email in foundEmails:
             f2.write(email)
             f2.write("\n")

        f2.close()

    except Exception as e:
        print(f"Error Crawling {currUrl}: {str(e)}")
        




