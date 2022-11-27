# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP
    <br> 34.83.255.32:8000
2. SSH username
    <br> andy
3. SSH password or key.
    <br> Public and Private Key Files “team03-testuser” and “team03-testuser.pub” are uploaded, please refer to credentials folder.
    <br> Password for “sudo ssh”: CSC648!@#Team03
4. Database URL or IP and port used.
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.
    <br> Host: 34.83.255.32 Port: 3306
5. Database username
    <br> playdateadmin
6. Database password
    <br> Pl@yd@te03
7. Database name (basically the name that contains all your tables)
    <br> playdate
8. Instructions on how to use the above information.
    <br><strong>8.1 Connect To Our App Server</strong>
    <br> You can put the key files in the folder: ~/.ssh of your local computer.
    <br> When connect to the server, use command:
    
    <br> $ sudo ssh -i ~/.ssh/team03-testuser andy@34.83.255.32
    <br> password for this sudo ssh is: CSC648!@#Team03
    
    <br> Project directory is: /projectdir
    <br> (If you have created your own key files with a password before, you shall first enter your own password, then enter ours.)
    
    <strong>8.2 Connect To Our App Database Server</strong>
    <br> There are three ways to connect to our Database Server:
    
    <br><strong> 8.2.1. Directly connect to our DB server with command:</strong>
    <br> $ mysql -h 34.83.255.32 -u playdateadmin -p
    <br> Password: Pl@yd@te03
    
    <br><strong> 8.2.2 First ssh to our app server, then login our DB server with command:</strong>
    <br> $ mysql -u playdateadmin -p
    <br> Password: Pl@yd@te03
    
    <br><strong> 8.2.3 Connect to our DB server with MySQL workbench: </strong>
    <br> In your workbench, set “Hostname” as “34.83.255.32”, set “Port” as “3306”, set “Username” as “playdateadmin”, set “Password” as “Pl@yd@te03”, then connect.

    
# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.
