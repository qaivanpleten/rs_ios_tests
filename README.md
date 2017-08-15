# Authotest python scripts to test IOs app with Appium

# Basic instalation 

1. Install XCode
2. Install Python
3. Install Appium https://www.youtube.com/watch?v=meU4TzI3KNM

4. Create/Upload project with app, wich will be tested
5. Create project for tests. In our case it will be project in Pycharm. Or download the project from GitHub. 
6. Run the test scripts

# Appium configuration to manual testing

1. Run Appium
2. Run XCode simulator
3. Start new Apium server session
4. Configure capabilities. E.g.

{
  "platformName": "iOS",
  "platformVersion": "10.3",
  "deviceName": "IPhone Simulator",
  "app": "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"
}

5. Save it. 
6. Start Appium emulator session

# Example of setUpClass

    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
# How to make pull request 
1. Create new branch 
2. Make changes in code
3. Commit changes
3.1 Add Commit Message. E.g fix #isue_number
4. Push changes
5. On github.com click on Compare & pull request
6. Add reviewers
7. Create pull request
