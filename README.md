# Windows App Test Automation

Simple Python desktop UI automation framework for Windows applications using **pywinauto**.

This repository includes two sample automated test cases:

- **WIN_APPS_001** - Notepad text entry verification
- **WIN_APPS_002** - Calculator addition verification

## Project Structure

```text
WinApps-Test-Automation/
├── Conf/
│   └── Config.ini
├── ExpectedResults/
│   └── WIN_APPS/
│       ├── WIN_APPS_001/
│       │   └── TestResult.txt
│       └── WIN_APPS_002/
│           └── TestResult.txt
├── TestScripts/
│   ├── Tests/
│   │   └── UnitTests/
│   │       ├── UnitTestsManager.py
│   │       └── WIN_APPS/
│   │           ├── WIN_APPS_001.py
│   │           ├── WIN_APPS_002.py
│   │           └── WIN_APPS_TestManager.py
│   └── Utils/
│       ├── Base/
│       │   ├── Test_Base.py
│       │   ├── Test_Config.py
│       │   ├── TestManager.py
│       │   └── WindowsApp_Test_Base.py
│       └── Managers/
│           ├── CommonFunctions.py
│           ├── ConfigManager.py
│           ├── FileManager.py
│           ├── GlosssaryManager.py
│           └── ReportManager.py
├── TestWinApps.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Windows 10 or Windows 11
- Python 3.10.x or 3.12.x
- Notepad and Calculator available on the machine
- Microsoft Word installed if you want automatic table-of-contents refresh and PDF report generation

## Important Notes

- This repository is a **standalone Windows App sample project** along with a basic automation framework.
- The included sample tests automate **Notepad** and **Calculator** only.
- The project still contains some utility modules such as database and process helpers, but the sample Notepad/Calculator tests do **not** use them.
 

## Recommended Tooling

The framework uses these tools:

- **PyCharm Community Edition** for editing and running tests
- **Pywinauto Recorder** for discovering UI elements and recording Windows UI interactions

Useful links:

- Python downloads: <https://www.python.org/downloads/>
- PyCharm Community Edition: <https://www.jetbrains.com/pycharm/download/#section=windows>
- Pywinauto Recorder: <https://pywinauto-recorder.readthedocs.io/en/latest/pywinauto_recorder_exe.html>
- Inspect Tools: <https://github.com/blackrosezy/gui-inspect-tool>
- PyWinauto Documentation: <https://pywinauto-recorder.readthedocs.io/en/latest/#>

## GUI Inspection Tools

These tools are useful when generating new desktop UI automation tests, especially for identifying:

- window titles
- control types
- automation ids
- control hierarchy
- accessible names and patterns

Recommended tools and download locations:

| Tool | Purpose | Download |
|---|---|---|
| **Inspect.exe** | Inspect Microsoft UI Automation and MSAA properties of desktop controls | <https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/> |
| **Accessibility Insights** | Modern accessibility and UI inspection tool; recommended replacement for many legacy inspection scenarios | <https://accessibilityinsights.io/downloads/> |
| **Spy++ (SPYXX.EXE)** | Inspect native Win32 windows, handles, classes, messages, and process/window relationships | <https://visualstudio.microsoft.com/vs/community/> |
| **Pywinauto Recorder** | Capture UI paths and generate pywinauto-style automation snippets | <https://pywinauto-recorder.readthedocs.io/en/latest/pywinauto_recorder_exe.html> |
| **SWAPY** | Legacy helper for generating pywinauto code ideas from desktop controls | <https://sourceforge.net/projects/swapy/> |
| **Windows SDK Archive** | Archive location for older Microsoft accessibility/inspection tools such as legacy **Inspect**, **AccEvent**, and **UI Spy** builds | <https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/> |

### Legacy tools in the local bundle


Some of these are legacy Microsoft accessibility utilities that may no longer have a current standalone public download page. When you need fresh copies, prefer:

1. the **Windows SDK**
2. the **Windows SDK archive**
3. **Visual Studio Community** for Spy++

### Best tools for authoring new tests

For this project, the most useful tools are:

1. **Pywinauto Recorder**
2. **Inspect.exe**
3. **Spy++**
4. **Accessibility Insights**

## Setup

Clone or download the repository, then open a PowerShell terminal in the project root folder and run:

```powershell
# 1. Navigate to the project root (adjust path to wherever you cloned the repo)
cd <path-to-repo>\WinApps-Test-Automation

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate the virtual environment
.venv\Scripts\Activate.ps1

# 4. Install dependencies into the virtual environment
python -m pip install -r requirements.txt
```

> **Note:** Use `python -m pip` instead of bare `pip` to ensure packages are installed into
> the active virtual environment and not a system-level Python interpreter.

If your PowerShell execution policy blocks `.ps1` scripts, run this first:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Manual package installation

If you prefer to install packages individually:

```powershell
python -m pip install pywinauto
python -m pip install Pillow
python -m pip install python-docx
python -m pip install docx2pdf
python -m pip install pywin32
python -m pip install WMI
```

`requirements.txt` is the preferred setup method because it pins versions and keeps the environment consistent.

## Optional PyCharm Workflow

If you want to follow the same IDE-driven workflow as the original documentation:

1. Install **PyCharm Community Edition**
2. Open the project root folder (`WinApps-Test-Automation/`) in PyCharm
3. Configure the interpreter to use:
   - the project virtual environment in `.venv/`, or
   - a compatible Python 3.10/3.12 interpreter with the required packages installed
4. Verify the correct interpreter is selected in the bottom-right corner of PyCharm before running tests

If you have multiple Python environments on the machine, double-check that PyCharm is not using an older or incompatible interpreter.

## Configuration

Runtime configuration is stored in [Config.ini](C:/Work/WinApps-Test-Automation/Conf/Config.ini).

Important sections:

- **[TestConfig]**
  - `PollWaitPeriod`: polling interval used by process/file wait helpers
  - `UnitTests`: keep this as `1` for this sample project
- **[Credentials]**
  - placeholder username/password values
  - retained for framework compatibility
- **[Database]**
  - placeholder MySQL settings
  - only relevant if you extend the framework with DB-backed tests
- **[Deployment]**
  - `BinFolder`: retained for compatibility with helper modules that launch binaries
- **[TestConf]**
  - `TestDelayInSeconds`: delay between individual test runs
- **[ReportGeneration]**
  - `Logs`: include logs in the report if available
  - `ExpectedResults`: include expected result files
  - `ActualResults`: include actual result files
  - `Screenshots`: include screenshots
  - `Glossary`: include glossary section
  - `PDFReport`: enable PDF conversion after DOCX generation

For the current sample tests, the most useful settings are `TestDelayInSeconds`, `Screenshots`, and `PDFReport`.

## Running the Tests

```powershell
cd C:\Work\WinApps-Test-Automation
.venv\Scripts\Activate.ps1
python TestWinApps.py
```

`TestWinApps.py` checks for required runtime packages before the framework loads. If a package is missing, it attempts to install it into the current Python environment automatically.

To disable automatic installation and only validate dependencies:

```powershell
python TestWinApps.py --no-install-deps
```

### Running from PyCharm

You can also run the suite from PyCharm by opening [TestWinApps.py](C:/Work/WinApps-Test-Automation/TestWinApps.py) and using **Run -> Run 'TestWinApps'**.

## How to generate new tests
1. Launch Pywinautorecorder
2. Identify the Icon in your Task Bar
3. Select the start recording option
4. Perform your activities.
5. Select stop recording option
6. pywinautorecorder has generated the python script and has pasted it to the clipboard.
7. Open Notepad or any editor, Paste the contents of the generated script
8. Modify the generated script and create a new test case using this framework, extend this framework to suit your requirements. 

## What the Tests Do

### WIN_APPS_001 - Notepad

1. Launches Notepad
2. Types `Hello World! This is an Automated Test.`
3. Takes a screenshot
4. Reads the text back from the editor
5. Compares the actual result with `ExpectedResults/WIN_APPS/WIN_APPS_001/TestResult.txt`

### WIN_APPS_002 - Calculator

1. Launches Calculator
2. Switches to Standard mode
3. Performs `7 + 6 + 7 = 20`
4. Takes a screenshot
5. Reads the displayed result
6. Compares the actual result with `ExpectedResults/WIN_APPS/WIN_APPS_002/TestResult.txt`

## Outputs

After execution:

- Screenshots are saved under `TestResults/WIN_APPS/<TestID>/`
- Actual result files are saved under `TestResults/WIN_APPS/<TestID>/`
- A Word report is generated at `TestResults/WinTestReport.docx`
- The Word report includes an `Index` / table-of-contents page
- If `PDFReport = 1` and Microsoft Word is available, a PDF report is generated at `TestResults/WinTestReport.pdf`

## Reporting Notes

- DOCX report generation uses `python-docx`
- PDF conversion uses `docx2pdf`
- Automatic TOC refresh and reliable PDF generation on Windows typically require **Microsoft Word**
- If Word is unavailable, the project may still generate the DOCX report, but PDF creation or automatic TOC refresh can fail
- When report conversion cannot be completed, details are written to the runtime log

## Compatibility Notes

Based on issues noted in the original framework documentation:

- Avoid Python 3.13 for this style of legacy Windows automation unless you have validated all dependencies
- If your machine already has other Python testing frameworks or IDE interpreters configured, ensure the correct interpreter is selected before running
- If test execution behaves differently across machines, check:
  - Python version
  - selected interpreter
  - installed Office/Word availability
  - package versions from [requirements.txt](C:/Work/WinApps-Test-Automation/requirements.txt)
