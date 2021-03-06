__author__ = 'Gino'


class WorldContext(object):
    # WIP. Needed? Useful? Can we think about useful data?

    def __init__(self, driver, stage, mobile=False):
        self.stage = stage
        self.mobile = mobile
        self.currentPage = None
        self.userName = None
        self.userPassword = None
        self.userEmail = None
        self.driver = driver
        self.logged_account = None

    def create_page_object(self, page_object):
        return page_object(driver=self.driver, env=self.env, mobile=self.mobile)
