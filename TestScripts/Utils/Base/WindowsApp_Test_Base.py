# Import Required Libraries
from TestScripts.Utils.Base.Test_Base import *

class WindowsApp_Test_Base(Test_Base):
    """Extension point for generic Windows desktop application tests."""

    def RunTest(self):
        logging.info("WindowsApp_Test_Base::RunTest() - Execute the Test")
        super().RunTest()
