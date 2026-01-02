# Next Steps

Congratulations! You have successfully installed and started your first Minecraft server using `mcup`.
Now that your server is running, here are some recommended steps to manage and customize it.

## Setup Firewall & Port Forwarding

By default, Minecraft servers listen on port `25565`. 
For players outside your local network to connect, you need to allow traffic through this port.

### Allow Access in Firewall

Ensure your computer's firewall is not blocking incoming connections on the server port.

-   **Linux (UFW):** `sudo ufw allow 25565/tcp 25565/udp`
-   **Windows:** Allow the Java binary through Windows Defender Firewall.
-   **macOS:** Configure the built-in application firewall in System Settings.

### Port Forwarding

If you are hosting the server at home behind a router, 
you will need to "port forward" port `25565` or other you chose from your router to your computer's local IP address. 
The steps for this vary depending on your router model; 
consult your router's manual or look up a guide for your specific model.

## Install Plugins

If you created a server type that supports plugins (like **Paper** or **Spigot** for example), 
you can extend the functionality of your server.

1.  **Stop the server** if it is running.
2.  Navigate to the `plugins` folder inside your server directory.
3.  Download `.jar` plugin files from reputable sources (e.g., [SpigotMC](https://www.spigotmc.org/), [Hangar](https://hangar.papermc.io/), [Modrinth](https://modrinth.com)).
4.  Place the `.jar` files into the `plugins` folder.
5.  **Start the server** to load the plugins.

## Install Mods

If you created a modded server (like **Fabric** or **NeoForge**), you can install mods to change the game experience.

1.  **Stop the server** if it is running.
2.  Navigate to the `mods` folder inside your server directory (create it if it doesn't exist).
3.  Download `.jar` mod files from sources like [Modrinth](https://modrinth.com/).
4.  Ensure the mods are compatible with your server version.
5.  Place the `.jar` files into the `mods` folder.
6.  **Start the server** to load the mods.

## Administration & Security

### Enabling Whitelist

If you want to create a private server for friends, it is highly recommended to enable the whitelist.

1.  In your server console, run: `whitelist on`.
2.  Add players to the whitelist: `whitelist add <username>`.
3.  Only listed players will be able to join.

### Automated Backups

Your server "world" is precious. Regular backups are essential to prevent data loss from griefing or corruption.

-   **Manual:** Regularly copy the `world` folder (and `world_nether`, `world_the_end`) to a safe location.
-   **Automated:** Install a backup plugin or mod (e.g., DriveBackupV2, FTB Backups) to handle this automatically on a schedule.
