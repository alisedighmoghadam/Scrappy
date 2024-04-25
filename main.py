from fetch.html_getter import HTMLGetter
if __name__=="__main__":
    test= HTMLGetter("https://google.com/search/about")
    test.show_robot_permissions()