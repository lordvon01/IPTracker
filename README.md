# IPTracker
To track your WAN IP and notify you if it changes.

To build the docker container properly. The following folder/file structure is required.

Create a folder in etc/docker called "iptracker"
![image](https://github.com/user-attachments/assets/2602f294-592a-4cad-898a-39efcb87beff)

Under "iptracker" folder create a folder called "app"
![image](https://github.com/user-attachments/assets/efcc1ddd-907e-4398-bdf4-0c9609181f78)

Copy all the files into the root of "iptracker" folder
change into the "app" folder and create a new directory called "templates"
Copy the 2 .py files into the "app" directory
![image](https://github.com/user-attachments/assets/8a1f3971-ee26-4805-a277-d79d153e65d4)

Copy the index.html into the templates folder
![image](https://github.com/user-attachments/assets/6a5fbc48-e224-4f35-8d58-f4c310130dee)

Edit the .env file if email notifications needs to be enabled.
![image](https://github.com/user-attachments/assets/81b3d579-4ed8-4f88-8c81-0c546636ab3b)

Once all the files are staged run the the following commands.

sudo docker build -t iptracker .

Once the container is built run the following command to bring up the container.

sudo docker run -d -p 5000:5000 --name iptracker --env-file smtpsettings.env iptracker

This should start the container and you can browse to http://IPADDRESS:5000 and access the web page.
