import re
from mcup.core.status import StatusCode, Status


class ScriptTemplateManager:
    """Manages script templates with validation."""

    @staticmethod
    def get_bash_template() -> str:
        """Get bash script template."""
        return '''#!/usr/bin/env sh

cleanup() {{
    echo "Cleaning up..."
    pkill -f "{server_jar}"
    exit 0
}}

trap cleanup INT TERM

if [ -z "$STY" ]; then
    if screen -list | grep -q "{screen_name}"; then
        echo "Screen session '{screen_name}' is already running!"
        echo "Use 'screen -r {screen_name}' to attach to the existing session"
        echo "Or use 'screen -S {screen_name} -X quit' to stop it first"
        exit 1
    fi

    if [ ! -f "{server_jar_clean}" ]; then
        echo "Error: {server_jar_clean} not found"
        exit 1
    fi

    echo "Starting server in screen session: {screen_name}"
    echo "Use 'screen -r {screen_name}' to attach to the session"
    echo "Use 'screen -S {screen_name} -X quit' to stop the session"
    screen -dmS {screen_name} "$0"
    exit 0
fi

restart_count=0
max_restarts={max_restarts}

echo "Server starting in screen session..."
echo "Press CTRL + C to stop gracefully."

while true; do
    if [ $restart_count -ge $max_restarts ]; then
        echo "Maximum restart attempts ($max_restarts) reached. Exiting."
        break
    fi

    if [ ! -f "{server_jar_clean}" ]; then
        echo "Error: {server_jar_clean} not found. Exiting."
        break
    fi

    echo "Starting server (attempt $((restart_count + 1)))..."

    {java_command}
    exit_code=$?

    restart_count=$((restart_count + 1))

    if [ $exit_code -eq 0 ]; then
        echo "Server stopped normally."
        break
    else
        echo "Server crashed with exit code $exit_code"
        echo "Restarting in {restart_delay} seconds... (Press CTRL + C to stop)"
        sleep {restart_delay} || break
    fi
done

echo "Server restart script finished."
'''

    @staticmethod
    def get_batch_template() -> str:
        """Get batch script template."""
        return '''@echo off
setlocal enabledelayedexpansion

set "SERVER_JAR={server_jar}"
set "SERVER_JAR_CLEAN={server_jar_clean}"
set "SCREEN_NAME={screen_name}"
set "MAX_RESTARTS={max_restarts}"
set "RESTART_DELAY={restart_delay}"
set "USE_AIKARS_FLAGS={use_aikars_flags}"

set "CLEANUP_DONE=false"

if "%DETACHED_SESSION%"=="true" goto :main_loop

if not exist "%SERVER_JAR_CLEAN%" (
    echo Error: %SERVER_JAR_CLEAN% not found
    exit /b 1
)

echo Starting server in new console session: %SCREEN_NAME%
echo A new console window will open for the server
echo Close that window or press CTRL+C in it to stop the server

start "%SCREEN_NAME%" cmd /c "set DETACHED_SESSION=true&& set SERVER_JAR=%SERVER_JAR%&& set SCREEN_NAME=%SCREEN_NAME%&& set MAX_RESTARTS=%MAX_RESTARTS%&& set RESTART_DELAY=%RESTART_DELAY%&& set USE_AIKARS_FLAGS=%USE_AIKARS_FLAGS%&& cd /d \\"%CD%\\"&& call \\"%~f0\\""
exit /b 0

:main_loop
title %SCREEN_NAME%
set /a restart_count=0

echo Server starting in console session...
echo Press CTRL + C to stop gracefully.

:restart_loop
if !restart_count! geq %MAX_RESTARTS% (
    echo Maximum restart attempts ^^^(%MAX_RESTARTS%^^^) reached. Exiting.
    goto :cleanup
)

if not exist "%SERVER_JAR_CLEAN%" (
    echo Error: %SERVER_JAR_CLEAN% not found. Exiting.
    goto :cleanup
)

set /a attempt=!restart_count! + 1
echo Starting server ^^^(attempt !attempt!^^^)...

{java_command}
set "exit_code=!errorlevel!"

set /a restart_count=!restart_count! + 1

if !exit_code! equ 0 (
    echo Server stopped normally.
    goto :cleanup
) else (
    echo Server crashed with exit code !exit_code!
    echo Restarting in %RESTART_DELAY% seconds... ^^^(Press CTRL + C to stop^^^)

    timeout /t %RESTART_DELAY% /nobreak >nul 2>&1
    if errorlevel 1 goto :cleanup

    goto :restart_loop
)

:cleanup
if "%CLEANUP_DONE%"=="false" (
    set "CLEANUP_DONE=true"
    echo Cleaning up...
    taskkill /f /im java.exe /fi "WINDOWTITLE eq %SCREEN_NAME%*" 2>nul
)

echo Server restart script finished.
if "%DETACHED_SESSION%"=="true" (
    echo Press any key to close this window...
    pause >nul
)
exit /b 0
'''

    @staticmethod
    def validate_template_variables(template: str, config: dict) -> Status:
        """Validate all template variables are available in config."""
        variables = re.findall(r'(?<!\{)\{([^{}]+)\}(?!\})', template)
        missing_vars = []

        for var in variables:
            if var not in config:
                missing_vars.append(var)

        if missing_vars:
            return Status(StatusCode.ERROR_CONFIG_MISSING_REQUIRED_KEYS, missing_vars)

        return Status(StatusCode.SUCCESS)
