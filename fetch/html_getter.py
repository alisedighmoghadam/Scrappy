import urllib.request as req
import fetch_utils as utils
class HTMLGetter:
    def __init__(self,url):

        self.url=url
        self.robot_permissions=self.get_robot()

    #todo write a function to get a simple html
    def get(self):
        req.urlopen(self.url)

    #todo write a function to get html with a header

    #todo write a fucntion to get robot.txt
    def get_robot(self):
        base_url=utils.base_urls(self.url)
        return req.urlopen(base_url+"/robot.txt")
