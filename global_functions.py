def close_browser(self,tc_name):
    """Close browser"""
    try:
        self.login.close_browser()
    except Exception as e:
        print("Exception= '{0}'".format(e.message))
