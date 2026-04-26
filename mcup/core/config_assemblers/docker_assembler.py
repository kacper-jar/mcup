import json
import shlex
from mcup.core.config_assemblers import Assembler


class DockerAssembler(Assembler):
    """Class representing Dockerfile assembler."""

    @staticmethod
    def assemble(path: str, config):
        """Assemble the Dockerfile at the specified path."""

        java_version = config.configuration.get("java-version", "21")
        server_jar = config.configuration.get("server-jar", "server.jar")
        jar_flag = "-jar" if config.configuration.get('server-args-instead-of-jar') is False else ""
        initial_heap = config.configuration.get("memory-initial", "1G")
        max_heap = config.configuration.get("memory-max", "2G")

        entrypoint = ["java", f"-Xms{initial_heap}", f"-Xmx{max_heap}"]

        if jar_flag:
            entrypoint.append(jar_flag)

        entrypoint.extend(shlex.split(server_jar))
        entrypoint.append("nogui")

        port = config.configuration.get("port", "25565")

        dockerfile_content = f"""FROM azul/zulu-openjdk-alpine:{java_version}-jre
WORKDIR /app
COPY . .
EXPOSE {port}
ENTRYPOINT {json.dumps(entrypoint)}
"""

        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as f:
            f.write(dockerfile_content)
