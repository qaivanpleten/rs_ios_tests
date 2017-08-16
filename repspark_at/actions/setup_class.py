from appium import webdriver

class setUpClass('???????????????'):
    #@classmethod  I'm not sure if I should use classmethod here
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        return '???????????'


    #@classmethod  I'm not sure if I should use classmethod here
    def tearDownClass(cls):
        cls.driver.quit()

        return '??????????'