from mcup.core.config_assemblers import Assembler


class BatchStartScriptAssembler(Assembler):
    """Class representing batch start script assembler."""

    @staticmethod
    def assemble(path: str, config):
        """Assemble the batch start script at the specified path."""

        java_flags = f"-Xms{config.configuration['initial-heap']}M -Xmx{config.configuration['max-heap']}M"

        jar_flag = "-jar" if config.configuration['server-args-instead-of-jar'] is False else ""

        if config.configuration['use-aikars-flags']:
            aikar_flags = (
                "-XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:+ParallelRefProcEnabled "
                "-XX:+PerfDisableSharedMem -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC "
                "-XX:G1HeapRegionSize=8M -XX:G1HeapWastePercent=5 -XX:G1MaxNewSizePercent=40 "
                "-XX:G1MixedGCCountTarget=4 -XX:G1MixedGCLiveThresholdPercent=90 "
                "-XX:G1NewSizePercent=30 -XX:G1RSetUpdatingPauseTimePercent=5 "
                "-XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15 "
                "-XX:MaxGCPauseMillis=200 -XX:MaxTenuringThreshold=1 -XX:SurvivorRatio=32 "
                "-Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true"
            )
            java_command = f"java {java_flags} {aikar_flags} {jar_flag} \"%SERVER_JAR%\" nogui"
        else:
            java_command = f"java {java_flags} {jar_flag} \"%SERVER_JAR%\" nogui"

        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            script_content = f"""@echo off
setlocal enabledelayedexpansion

set "SERVER_JAR={config.configuration['server-jar']}"
set "SERVER_JAR_CLEAN={config.configuration['server-jar']}"
set "SCREEN_NAME={config.configuration['screen-name']}"
set "MAX_RESTARTS={config.configuration['max-restarts']}"
set "RESTART_DELAY={config.configuration['restart-delay']}"
set "USE_AIKARS_FLAGS={str(config.configuration['use-aikars-flags']).lower()}"

set "CLEANUP_DONE=false"

if "%DETACHED_SESSION%"=="true" goto :main_loop

if not exist "%SERVER_JAR_CLEAN%" (
    echo Error: %SERVER_JAR_CLEAN% not found
    exit /b 1
)

echo Starting server in new console session: %SCREEN_NAME%
echo A new console window will open for the server
echo Close that window or press CTRL+C in it to stop the server

start "%SCREEN_NAME%" cmd /c "set DETACHED_SESSION=true&& set SERVER_JAR=%SERVER_JAR%&& set SCREEN_NAME=%SCREEN_NAME%&& set MAX_RESTARTS=%MAX_RESTARTS%&& set RESTART_DELAY=%RESTART_DELAY%&& set USE_AIKARS_FLAGS=%USE_AIKARS_FLAGS%&& cd /d \"%CD%\"&& call \"%~f0\""
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
"""

            config_file.write(script_content)