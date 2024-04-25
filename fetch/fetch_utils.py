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
    route=f"{parsed.path}"
    return route

## this function parse robot.txt file and returns three lists which contains allowed, disallowed, and sitemap path. it mostly get the permissions based on the given robot.
#example:
#       input= raw robots.txt and name of the robot
#       output= allowed list, disallowed list, and sitemaps
def permission_parser(raw,robot_name=b"*",return_type="all"):
    lines = raw.read().split(b'\n')

    allowed=[]
    disallowed=[]
    sitemap=[]
    read= False
    for line in lines:
        if line.startswith(b'#') or line==b'':
            continue

        if line.startswith(b"User-agent") and line.endswith(robot_name):
            read=True
            continue
        elif line.startswith(b"Sitemap:"):
            sitemap.append(line.replace(b':', b'').split(b" ")[1])
            read=False
        elif line.startswith(b"User-agent") and not line.endswith(robot_name):
            read=False

        if read:
            parsed_line = line.replace(b':', b'').split(b" ")
            if parsed_line[0] == b"Allow":
                allowed.append(parsed_line[1])
            else:
                disallowed.append(parsed_line[1])
    return_type=return_type.lower()

    if return_type== "all":
        return allowed,disallowed,sitemap
    elif return_type == "allowed":
        return allowed
    elif return_type == "disallowed":
        return disallowed
    elif return_type == "sitemap":
        return sitemap
    else:
        raise ValueError("ERROR: The entered return type is not correct. Please select from all, allowed, disallowed, or sitemap.")