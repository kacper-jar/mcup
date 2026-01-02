# Creating Your First Server

This guide will walk you through the process of setting up your very first Minecraft server using `mcup`. 
We will create a Paper server, one of the most popular and performant server software options available.

## Check Availability

Before we begin, it's helpful to see what server options are available. 
You can view a list of all supported server types and versions by running:

```bash
mcup server list
```

This command outputs a list of server types (like `vanilla`, `paper`, `neoforge`) 
and their corresponding supported versions (e.g., `1.20.1`, `1.19.4`).

## Create the Server

Let's create the server. We'll specify the server type (`paper`) and the version (`1.20.1`). 
You can also specify a directory where you want the server to be created; 
if you don't, it will default to the current directory.

Run the following command:

```bash
mcup server create paper 1.20.1 ./my-survival-server
```

This tells `mcup` to:

-   Create a **Paper** server.
-   Use version **1.20.1**.
-   Place all files in a new folder named `my-survival-server`.

## Configuration

Once the command runs, `mcup` will check if your installed Java version is compatible 
and then begin the interactive configuration wizard.

### EULA Acceptance

You must accept the [Minecraft EULA](https://account.mojang.com/documents/minecraft_eula) (End User License Agreement)
to run a server. `mcup` automatically sets this to `true` in the configuration,
but you are responsible for reading and complying with the agreement.

### Server Properties

Next, you will configure basic `server.properties` settings. 
Press ++enter++ or type ++y++ to accept the default values (shown in the defaults preview) or type ++n++ to type your own.
These core settings are presented for all server types.

### Advanced Configuration

Depending on the server type, `mcup` may prompt for additional configuration files. 
For example, Paper 1.20.1 servers require:

-   **Bukkit Configuration** (`bukkit.yml`)
-   **Spigot Configuration** (`spigot.yml`)
-   **Paper Global Configuration** (`configs/paper-global.yml`)
-   **Paper World Defaults** (`configs/paper-world-defaults.yml`)

Refer to the specific server documentation for details on these files.

### Start Script Configuration

Finally, you will configure the startup script. This script handles starting and auto-restarting your server.
You may be asked for:

-   **Screen name**: The screen session name for the running server.
-   **Heap Size (MB)**: Initial and maximum memory allocation for the JVM.
-   **Aikar's Flags**: Whether to use [Aikar's optimization flags](https://docs.papermc.io/paper/aikars-flags) (highly recommended for performance).
-   **Restart Settings**: Maximum restart attempts and delay between restarts.

## Running the Server

After configuration, `mcup` downloads the necessary files and generates the configuration files and start script.

Navigate to your new server directory:

```bash
cd my-survival-server
```

!!! note
    On Linux or macOS, ensure the start script is executable:
    ```bash
    chmod +x start.sh
    ```

To start your server, run the generated script for your operating system:

=== "Linux / macOS"
    ```bash
    ./start.sh
    ```

=== "Windows"
    ```bat
    start.bat
    ```

**Congratulations!** Your server should now be starting up.

You can view its console by running `screen -r <screen-name>`.
You can detach from the screen view by pressing ++ctrl+a++ then ++d++, 
or stop the server by pressing ++ctrl+c++ inside the screen session.

For next steps, please see the [next guide](next-steps.md).
