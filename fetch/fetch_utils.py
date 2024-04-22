from urllib.parse import urlparse

## this function returns base url.
# example:
#       input= https://google.com/cascasc/vdavda
#       output= https://google.com
def base_urls(url):
    parsed=urlparse(url)
    base=f"{parsed.scheme}://{parsed.netloc}"
    return base

## this function returns route of the url
# example:
#       input= https://google.com/cascasc/vdavda
#       output= /cascasc/vdavda
def route_url(url):
    parsed=urlparse(url)
    route=f"{parsed.}"