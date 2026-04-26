from mcup.core.config_assemblers import Assembler


class DockerComposeAssembler(Assembler):
    """Class representing docker-compose.yml assembler."""

    @staticmethod
    def assemble(path: str, config):
        """Assemble the docker-compose.yml at the specified path."""

        service_name = config.configuration.get("service-name", "minecraft-server")
        container_name = config.configuration.get("container-name", "minecraft-server")
        port = config.configuration.get("port", 25565)

        uid = config.configuration.get("uid", 1000)
        gid = config.configuration.get("gid", 1000)

        docker_compose_content = f"""services:
  {service_name}:
    build: .
    container_name: {container_name}
    user: "{uid}:{gid}"
    ports:
      - "{port}:{port}"
    volumes:
      - .:/app
    restart: unless-stopped
    stdin_open: true
    tty: true
"""

        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as f:
            f.write(docker_compose_content)
