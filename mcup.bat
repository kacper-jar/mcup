@echo off
setlocal

set "MCUP_ENTRY_PACKAGE=mcup"

where python 1>nul 2>nul
if errorlevel 1 (
    echo Error: Python3 is not installed.
    exit /b 1
)

python -m %MCUP_ENTRY_PACKAGE% %*