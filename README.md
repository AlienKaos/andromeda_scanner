 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗███████╗██████╗  █████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██╔████╔██║█████╗  ██║  ██║███████║    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  ██║  ██║██╔══██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██████╔╝██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                              
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'                                                                                                                

============================================
Andromeda Scanner - Basic Usage Instructions
============================================

1. Clone the Repository:
   Download the Andromeda Scanner tool by cloning the repository from GitHub.
   ```bash
   git clone https://github.com/AlienKaos/andromeda_scanner.git
   ```

2. Navigate to the Directory:
   Change into the directory containing the Andromeda Scanner script.
   ```bash
   cd Andromeda-Scanner
   ```

3. Run the Script:
   Use the following command format to run the script:
   ```bash
   python andromeda_scanner.py <host> -p <port_range> [-t]
   ```

    <host>: The IP address or domain name of the target you want to scan.
   -p <port_range>**: The range of ports you want to scan, specified as `start-end`. For example, `1-1024`.
   -t (optional): Use this flag to enable threading for faster scanning.

4. Examples:
   - Scan a Single Port:
     ```bash
     python andromeda_scanner.py 192.168.1.1 -p 80
     ```
   - Scan a Range of Ports Sequentially:
     ```bash
     python andromeda_scanner.py 192.168.1.1 -p 1-1024
     ```
   - Scan a Range of Ports with Threading:
     ```bash
     python andromeda_scanner.py 192.168.1.1 -p 1-1024 -t
     ```

5. View the Output:
   The script will display the open ports and their associated services on the console.

6. Need Help?:
   Run the script with the `-h` flag to see the help message with all available options.
   ```bash
   python andromeda_scanner.py -h
   ```

Enjoy using Andromeda Scanner!
