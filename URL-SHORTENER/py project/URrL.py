import pyshorteners

url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print('shorten url:')
    print(s.tinyurl.short(url))

shortenurl(url)
