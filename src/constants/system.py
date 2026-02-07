"""
Docstring for constants.system

For system formatting
"""

class ExitCode: # Static Value
    APP_SESSION: str = "A"
    CLIENT_SESSION: str = "C"
    SERVER_SESSION: str = "S"

    SESSION_SUCCESS: str = "0"
    SESSION_ERROR: str = "1"

class Infomation:
    APP_NAME: str = "Metalias"
    PROGRAM_NAME: str = "metalias"
    PROJECT_NAME: str = "Metalias"
    PRODUCT_NAME: str = "Metatosh Metalias for macOS on ARM-based"

class Factory:
    SERIAL_CODE: str = "M-D-9PATRICK"

    VERSION_NUMBER: str = "0.1.0"
    VERSION_TYPE: str = "Development"
    VERSION_CODE: str = "D-AA-000001"

    COMPATIBLE_SYSTEM: str = "posix"

class Session:
    STATUS_COMPLETE: str = "COMPLETE"
    STATUS_INCOMPLETE: str = "INCOMPLETE"
    STATUS_WORKING: str = "IN PROCESS"
    STATUS_NONE: str = "UNDEFINED"