# Import Required Libraries
import logging
import time

from pywinauto import Desktop
from pywinauto.application import Application


class WindowManager:
    """Helpers for locating newly opened top-level windows for desktop apps."""

    PROFILE_NOTEPAD = "notepad"
    PROFILE_CALCULATOR = "calculator"

    APP_PROFILES = {
        PROFILE_NOTEPAD: {
            "titlePattern": ".*Notepad.*",
            "className": "Notepad",
            "childCriteria": {"control_type": "Document"},
        },
        PROFILE_CALCULATOR: {
            "titlePattern": ".*Calculator.*",
            "className": "ApplicationFrameWindow",
            "childCriteria": None,
        },
    }

    @staticmethod
    def GetVisibleWindows(titlePattern=".*", backend="uia", className=None, childCriteria=None):
        """Return visible top-level windows that satisfy the supplied filters."""
        logging.info("WindowManager::GetVisibleWindows()")
        desktop = Desktop(backend=backend)
        candidates = desktop.windows(title_re=titlePattern, visible_only=True)
        return [candidate for candidate in candidates if WindowManager._MatchesWindow(candidate, className, childCriteria)]

    @staticmethod
    def GetExistingWindowHandles(titlePattern=".*", backend="uia", className=None, childCriteria=None):
        """Capture current window handles so a newly opened window can be identified later."""
        logging.info("WindowManager::GetExistingWindowHandles()")
        return {
            candidate.handle
            for candidate in WindowManager.GetVisibleWindows(titlePattern, backend, className, childCriteria)
        }

    @staticmethod
    def FindWindow(titlePattern=".*", existingHandles=None, timeoutSeconds=15, backend="uia",
                   readyTimeout=5, className=None, childCriteria=None):
        """Find a matching top-level window, preferring a newly opened one when possible."""
        logging.info("WindowManager::FindWindow()")
        if existingHandles is None:
            existingHandles = set()

        deadline = time.time() + timeoutSeconds
        while time.time() < deadline:
            candidates = WindowManager.GetVisibleWindows(titlePattern, backend, className, childCriteria)
            newCandidates = [candidate for candidate in candidates if candidate.handle not in existingHandles]

            if len(newCandidates) >= 1:
                return WindowManager._GetReadyWindow(newCandidates[-1].handle, backend, readyTimeout)

            if not existingHandles and len(candidates) == 1:
                return WindowManager._GetReadyWindow(candidates[0].handle, backend, readyTimeout)

            if len(candidates) >= 1:
                return WindowManager._GetReadyWindow(candidates[-1].handle, backend, readyTimeout)

            time.sleep(0.5)

        raise RuntimeError(
            "Unable to find the application window that matches the supplied filters. "
            "titlePattern={0}, className={1}, childCriteria={2}".format(titlePattern, className, childCriteria)
        )

    @staticmethod
    def GetAppProfile(profileName):
        """Return a named application profile containing the filters used for window lookup."""
        logging.info("WindowManager::GetAppProfile()")
        normalizedName = profileName.lower()
        if normalizedName not in WindowManager.APP_PROFILES:
            raise RuntimeError("Unknown application profile: {0}".format(profileName))
        return WindowManager.APP_PROFILES[normalizedName]

    @staticmethod
    def GetExistingWindowHandlesForProfile(profileName, backend="uia"):
        """Capture current window handles for a named application profile."""
        logging.info("WindowManager::GetExistingWindowHandlesForProfile()")
        profile = WindowManager.GetAppProfile(profileName)
        return WindowManager.GetExistingWindowHandles(
            profile["titlePattern"],
            backend=backend,
            className=profile.get("className"),
            childCriteria=profile.get("childCriteria")
        )

    @staticmethod
    def FindWindowForProfile(profileName, existingHandles=None, timeoutSeconds=15, backend="uia", readyTimeout=5):
        """Find a window using the filters from a named application profile."""
        logging.info("WindowManager::FindWindowForProfile()")
        profile = WindowManager.GetAppProfile(profileName)
        return WindowManager.FindWindow(
            profile["titlePattern"],
            existingHandles=existingHandles,
            timeoutSeconds=timeoutSeconds,
            backend=backend,
            readyTimeout=readyTimeout,
            className=profile.get("className"),
            childCriteria=profile.get("childCriteria")
        )

    @staticmethod
    def LaunchAndFindWindow(executablePath, titlePattern=".*", backend="uia", waitForIdle=False,
                            timeoutSeconds=15, readyTimeout=5, className=None, childCriteria=None):
        """Start an application and return the matching ready window."""
        logging.info("WindowManager::LaunchAndFindWindow()")
        existingHandles = WindowManager.GetExistingWindowHandles(
            titlePattern,
            backend=backend,
            className=className,
            childCriteria=childCriteria
        )
        Application(backend=backend).start(executablePath, wait_for_idle=waitForIdle)
        return WindowManager.FindWindow(
            titlePattern,
            existingHandles=existingHandles,
            timeoutSeconds=timeoutSeconds,
            backend=backend,
            readyTimeout=readyTimeout,
            className=className,
            childCriteria=childCriteria
        )

    @staticmethod
    def LaunchAndFindWindowForProfile(executablePath, profileName, backend="uia", waitForIdle=False,
                                      timeoutSeconds=15, readyTimeout=5):
        """Start an application and return the ready window for a named profile."""
        logging.info("WindowManager::LaunchAndFindWindowForProfile()")
        existingHandles = WindowManager.GetExistingWindowHandlesForProfile(profileName, backend=backend)
        Application(backend=backend).start(executablePath, wait_for_idle=waitForIdle)
        return WindowManager.FindWindowForProfile(
            profileName,
            existingHandles=existingHandles,
            timeoutSeconds=timeoutSeconds,
            backend=backend,
            readyTimeout=readyTimeout
        )

    @staticmethod
    def _MatchesWindow(candidate, className, childCriteria):
        """Check whether a wrapper matches the optional class-name and child-control filters."""
        logging.info("WindowManager::_MatchesWindow()")

        if className is not None and candidate.class_name() != className:
            return False

        if not childCriteria:
            return True

        try:
            descendants = candidate.descendants(**childCriteria)
            return len(descendants) >= 1
        except Exception:
            return False

    @staticmethod
    def _GetReadyWindow(handle, backend, readyTimeout):
        """Return a Desktop window specification for the supplied handle and wait until it is ready."""
        logging.info("WindowManager::_GetReadyWindow()")
        window = Desktop(backend=backend).window(handle=handle)
        window.wait("ready", timeout=readyTimeout)
        return window