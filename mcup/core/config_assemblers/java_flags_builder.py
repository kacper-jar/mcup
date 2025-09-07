from mcup.core.status import StatusCode, Status


class JavaFlagsBuilder:
    """Utility class for building Java command line flags."""

    @staticmethod
    def build_memory_flags(initial_heap: int, max_heap: int) -> str:
        """Build memory allocation flags."""
        return f"-Xms{initial_heap}M -Xmx{max_heap}M"

    @staticmethod
    def build_aikars_flags() -> str:
        """Build Aikar's optimization flags."""
        return (
            "-XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:+ParallelRefProcEnabled "
            "-XX:+PerfDisableSharedMem -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC "
            "-XX:G1HeapRegionSize=8M -XX:G1HeapWastePercent=5 -XX:G1MaxNewSizePercent=40 "
            "-XX:G1MixedGCCountTarget=4 -XX:G1MixedGCLiveThresholdPercent=90 "
            "-XX:G1NewSizePercent=30 -XX:G1RSetUpdatingPauseTimePercent=5 "
            "-XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15 "
            "-XX:MaxGCPauseMillis=200 -XX:MaxTenuringThreshold=1 -XX:SurvivorRatio=32 "
            "-Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true"
        )

    @staticmethod
    def build_java_command(config: dict) -> tuple[str, Status]:
        """Build complete Java command from configuration."""
        try:
            java_flags = JavaFlagsBuilder.build_memory_flags(
                config['initial-heap'],
                config['max-heap']
            )

            jar_flag = "-jar" if not config.get('server-args-instead-of-jar', False) else ""

            if config.get('use-aikars-flags', False):
                aikar_flags = JavaFlagsBuilder.build_aikars_flags()
                java_command = f"java {java_flags} {aikar_flags} {jar_flag} {config['server-jar']} nogui"
            else:
                java_command = f"java {java_flags} {jar_flag} {config['server-jar']} nogui"

            return java_command, Status(StatusCode.SUCCESS)

        except KeyError as e:
            return "", Status(StatusCode.ERROR_CONFIG_MISSING_REQUIRED_KEYS, e)
        except Exception as e:
            return "", Status(StatusCode.ERROR_JAVA_FLAGS_GENERATION_FAILED, str(e))
