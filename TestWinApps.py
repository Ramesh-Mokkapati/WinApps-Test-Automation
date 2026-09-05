# Import Required Libraries
import importlib.util
import subprocess
import sys


REQUIRED_PACKAGES = (
    ("pywinauto", "pywinauto==0.6.8"),
    ("PIL", "Pillow==10.4.0"),
    ("docx", "python-docx==1.1.2"),
    ("docx2pdf", "docx2pdf==0.1.8"),
    ("win32com", "pywin32==306"),
    ("mysql", "mysql-connector-python==9.4.0"),
    ("wmi", "WMI==1.5.1"),
    ("pywinauto_recorder", "pywinauto-recorder==0.6.8"),
)


def _is_module_available(module_name):
    return importlib.util.find_spec(module_name) is not None


def ensure_runtime_dependencies(auto_install=True):
    """Ensure required third-party packages are available before importing the framework."""
    missing_packages = [
        package_name
        for module_name, package_name in REQUIRED_PACKAGES
        if not _is_module_available(module_name)
    ]

    if not missing_packages:
        return

    if not auto_install:
        raise RuntimeError(
            "Missing required packages: {0}. Install them with: {1} -m pip install -r requirements.txt".format(
                ", ".join(missing_packages),
                sys.executable
            )
        )

    print("Missing dependencies detected. Installing: " + ", ".join(missing_packages))
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            "Automatic dependency installation failed. Run '{0} -m pip install -r requirements.txt' manually.".format(
                sys.executable
            )
        ) from exc


ensure_runtime_dependencies(auto_install="--no-install-deps" not in sys.argv)

from TestScripts.Utils.Managers.ReportManager import *
from TestScripts.Tests.UnitTests.UnitTestsManager import *


class TestWinApps:
    """Entry point to the Windows application testing framework."""

    m_TestResults = []

    def __init__(self):
        logging.info("TestWinApps::TestWinApps()")
        self.m_CF = CommonFunctions()
        self.m_UnitTests = UnitTestsManager()

    def RunTests(self):
        """Execute all configured tests."""
        logging.info("TestWinApps::RunTests() - Executing all Unit Tests")
        self.m_UnitTests.RunTests()

    def GetTestResults(self):
        """Retrieve all test results for report generation."""
        logging.info("TestWinApps::GetTestResults() - Retrieving All Unit Test Results")
        self.m_TestResults.extend(self.m_UnitTests.GetTestResults())

    def GenerateReports(self):
        """Generate the test report."""
        logging.info("TestWinApps::GenerateReports() - Generate Report")
        rm = ReportManager()
        rm.WriteReport(self.m_TestResults)


if __name__ == '__main__':
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename='Test.log',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    testWinApps = TestWinApps()
    testWinApps.RunTests()
    testWinApps.GetTestResults()
    testWinApps.GenerateReports()

