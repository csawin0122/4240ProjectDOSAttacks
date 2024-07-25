SETUP INFORMATION FOR FORK BOMB AND SERVER ATTACK
_________________________________________________

Firstly, this was tested and run on a Virtual Machine running Ubuntu 22.04.
Once the package has been installed from GitHub, there will be 2 folders.
The first folder is the ForkBomb folder that contains the C code for the Fork Bomb.
The second folder is the ServerAttack folder that contains the python code for the Server Attack.
This was made to be simple and easy, from installation to attack.

FORK BOMB
________________________

The only set up needed to be able to run the Fork Bomb code is compiling and executing.
You can compile however you like or you can use the base command: ggc fork.c
To run it, if you compiled using the base command above, use: ./a.out
Once you hit enter, processes will spawn endlessly (based on system limits).
To stop the code from running, simply use a system interrupt (such as CTRL C)

To see that the attack is working, you can open a System Monitor tool to view
CPU and Memory levels before, during, and after the attack.
You should also notice the speed of your machine decrease significantly.


SERVER ATTACK
____________________________

Before we can run the code located in the ServerAttack folder,
we need to make sure that Apache2 is installed and running on our VM.
This was tested and run on Apache/2.4.52 (Ubuntu) version.
We can run 'sudo apt install apache2' to install apache2 to our system.
We can then test if our apache2 server is running in two ways:
	1) We can run the command: 'sudo systemctl status apache2',
	   which should says Active in green if set up correctly.
	2) We can open a search engine and type the loopback address
	   (127.0.0.1) in the search bar to see the Apache2 Default Page.
If the server is not set up correctly, we can run the command:
	'sudo systemctl start apache2' to start the server
	'sudo systemctl restart apache2' to restart the server
	'sudo systemctl stop apache2' to stop the server
If none of the above commands work. Removing and Reinstalling is the best bet.

Once the server is set up and ready to go, there is no set up with the code.
All we need to do to run is the code is the command: python3 ServerAttack.py

To see that the attack works, we can have both the home page and terminal pulled up,
and start the attack. If we refresh the apache2 home page, you should see it unable to load properly. Once the attack is stopped, the page should load instantly.
A common issue I ran into during this attack was browser cache. 
Watch out for it, as it can trick you into thinking the attack is not working,
or working when it shouldn't be.