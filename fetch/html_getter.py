import urllib.error
import urllib.request as req
import fetch.fetch_utils as utils
class HTMLGetter:
    def __init__(self,url):

        self.url=url
        self.robots_txt=self.get_robot()


    #todo write a function to get a simple html
    def get(self):
        req.urlopen(self.url)

    #todo write a function to get html with a header

    #todo write a fucntion to get robot.txt
    def get_robot(self):
        try:
            base_url=utils.base_urls(self.url)
            return req.urlopen(base_url+"/robots.txt")
        except urllib.error.HTTPError as err:
            print(err)

    def show_robot_permissions(self):
        if self.robots_txt is not None:
            permissions = utils.permission_parser(self.robots_txt,return_type="allowed")
            for permission in permissions:
                print(permission+b'\n')
        else:
            print("ERROR: Robot Permissions not found!")