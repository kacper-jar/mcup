from mcup.core.config_assemblers import Assembler


class BashStartScriptAssembler(Assembler):
    """Class representing bash start script assembler."""
    @staticmethod
    def assemble(path: str, config):
        """Assemble the bash start script at the specified path."""

        java_flags = f"-Xms{config.configuration['initial-heap']}M -Xmx{config.configuration['max-heap']}M"

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
            java_command = f"java {java_flags} {aikar_flags} -jar {config.configuration['server-jar']} nogui"
        else:
            java_command = f"java {java_flags} -jar {config.configuration['server-jar']} nogui"

        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            script_content = f"""#!/usr/bin/env sh

cleanup() {{
    echo "Cleaning up..."
    pkill -f "{config.configuration['server-jar']}"
    exit 0
}}

trap cleanup INT TERM

if [ -z "$STY" ]; then
    if screen -list | grep -q "{config.configuration['screen-name']}"; then
        echo "Screen session '{config.configuration['screen-name']}' is already running!"
        echo "Use 'screen -r {config.configuration['screen-name']}' to attach to the existing session"
        echo "Or use 'screen -S {config.configuration['screen-name']} -X quit' to stop it first"
        exit 1
    fi

    if [ ! -f "{config.configuration['server-jar']}" ]; then
        echo "Error: {config.configuration['server-jar']} not found in current directory"
        exit 1
    fi

    echo "Starting server in screen session: {config.configuration['screen-name']}"
    echo "Use 'screen -r {config.configuration['screen-name']}' to attach to the session"
    echo "Use 'screen -S {config.configuration['screen-name']} -X quit' to stop the session"
    screen -dmS {config.configuration['screen-name']} "$0"
    exit 0
fi

restart_count=0
max_restarts={config.configuration['max-restarts']}

echo "Server starting in screen session..."
echo "Press CTRL + C to stop gracefully."

while true; do
    if [ $restart_count -ge $max_restarts ]; then
        echo "Maximum restart attempts ($max_restarts) reached. Exiting."
        break
    fi

    if [ ! -f "{config.configuration['server-jar']}" ]; then
        echo "Error: {config.configuration['server-jar']} not found. Exiting."
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
        echo "Restarting in {config.configuration['restart-delay']} seconds... (Press CTRL + C to stop)"
        sleep {config.configuration['restart-delay']} || break
    fi
done

echo "Server restart script finished."
"""

            config_file.write(script_content)
