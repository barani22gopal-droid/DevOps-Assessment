                                                     **Docker Practical Assessment **
 
Project 1: Application Containerization 

NGINX is a high-performance web server widely used for hosting websites on Linux servers. 

This document explains how to install, configure, and host a static website using NGINX on Ubuntu systems. 

1.Install NGINX 

sudo apt update = Update package lists and existing packages = Update package lists  

sudo apt install nginx –y = Install NGINX 

sudo systemctl status nginx = Check NGINX status 

sudo systemctl start nginx 

sudo systemctl enable nginx 

 
2. Create Website Directory  

sudo mkdir -p /var/www/Dockertest= Create a directory 

sudo chown -R $USER:$USER /var/www/mywebsite= Set ownership and permissions 

sudo chmod -R 755 /var/www/mywebsite 

3. Create Website HTML File 

nano /var/www/mywebsite/index.html 

open 
    <h4>Welcome to DevOps</h4> 
    
    <h1><center></center>I am Barani Gopal</h1> </center>
    

4. Create NGINX Server Block 

sudo nano /etc/nginx/sites-available/nginx 

open 

server { 

   listen 8087; 
   
   server_name localhost;  
   
   root /var/www/mywebsite; 
   
   index index.html; 
   
   location / { 
   
   try_files $uri $uri/ =404;   
    } 

} 

sudo ln -s /etc/nginx/sites-available/mywebsite /etc/nginx/sites-enabled/= Enable the Website 

sudo nginx –t= Test 

sudo systemctl reload nginx= reload NGINX 

5. Firewall 

sudo apt install ufw  

sudo ufw allow 80=http 

sudo ufw allow 22 =ssh connection 

sudo ufw allow 8087 =host port 

sudo ufw reload 

sudo ufw start  

sudo ufw status 

Host 

sudo curl http://localhost:8087 

 
6. Create Dockerfile 

nano Dockerfile= Create a file named Dockerfile

open 

FROM nginx:latest = Use nginx image 

COPY . /usr/share/nginx/html = Copy your website files to nginx folder 

EXPOSE 80 = Expose port 80  
 
docker build -t nginximage = Build Docker Image 

docker images= Check the image 

docker run -d -p 8080:80 --name nginxcontainer nginximage =Run the Container in Background 

docker ps=Check the container 
 
7. Login to Docker Hub 

docker login -u username

username: 

password: 

docker tag nginximage baranigopal/ nginximage:v1 = Tag the Image 

docker push baranigopal / nginximage:v1= Push Image to Docker Hub 

docker pull baranigopal / nginximage:v1= pull Image to Docker Hub 


8.Git and GitHub 

Open ----Git Bash 

folder download after clone to git. 

git clone  https://github.com/barani22gopal-droid/DevOps-Assessment.git	 

git init 

after the DevOps-Assessment repo name show in window  

git add . 

git commit -m“Project 1” 

git push  

git pull

giy status

Git repo url:

https://github.com/barani22gopal-droid/DevOps-Assessment.git


<img width="1915" height="962" alt="image" src="https://github.com/user-attachments/assets/39b73be0-2b9c-46c0-bf99-94d4264353fd" />


Output :


• Proof that the site is accessible via the browser. 


 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b5115b14-cd6d-4ab4-b272-1fe8a8966ab0" />
 


• Proof that Dockerfile  of building the image. 


<img width="1918" height="551" alt="image" src="https://github.com/user-attachments/assets/1d782b59-51ab-4d9b-8232-9514fd6704b7" />






                                                                                Project 2 
                                                                                Data Persistence 

Objective Demonstrate how to manage stateful data in a containerized environment to prevent data loss during container lifecycles 
Using NGINX : 

1.Create Project Directory: 

sudo mkdir -p /var/www/assessment  

cd /var/www/assessment 

ls 

2.Create Python Application 

sudo nano myapp.py 

open 

import time 

from datetime import datetime 

LOG_FILE = "/tmp/log.txt"  

while True: 

    with open(LOG_FILE, "a") as f: 

        f.write(“Hi all ,I am barni gopal {datetime.now()}\n") 

print(“All the best”) 

time.sleep(5) 

3.Create Dockerfile 

sudo nano Dockerfile 

FROM python:3.11-slim = Use an official Python base image 

WORKDIR /app = Set working directory inside the container 

COPY . . = Copy the current folder contents into the container 

ENTRYPOINT ["python", "myapp.py"] = Run your Python script 

4. after we using to create image,volume and container 

docker build –t openpy . = Build Docker Image 

docker volume create barani = Create Docker Volume Storage 

5.docker exec -it conpython1 cat /tmp/log.txt 

docker volume ls =volume li sudo docker run -d --name conpython1 -v barani:/tmp openpy 

 = Run Container with Volume 

Output: 

Container first run  

<img width="1911" height="412" alt="Screenshot 2026-01-08 124259" src="https://github.com/user-attachments/assets/b5f25afd-4820-4a7e-bc20-e5bbb2d0f5a3" />

 

Remove the container then only it run  

sudo docker stop conpython1 = stop the container  

sudo docker rm -f conpython1= remove the container 

6.We are creating second container : 

docker exec -it conpython2 cat /tmp/log.txt 

 

Output: 

<img width="1914" height="898" alt="Screenshot 2026-01-08 124914" src="https://github.com/user-attachments/assets/d7adfe4e-ffd7-4373-a675-1ede5d5be860" />
 

 

 

 

 

 

 

docker logs conpython2 

<img width="1917" height="766" alt="Screenshot 2026-01-08 140627" src="https://github.com/user-attachments/assets/40edcf30-da43-400e-a30f-78f67e05641a" />

 

 

7.Docker hub tag and push  

docker tag openpy baranigopal/openpy:v1 = tag 

docker push baranigopal/openpy:v1 =push to docker hub 

Output : 

<img width="1891" height="496" alt="Screenshot 2026-01-08 135814" src="https://github.com/user-attachments/assets/39cda9d7-a827-4715-a435-b3cdcd35be47" />
 
 

8.Git and Github Repo: 

git pull origin main 

git status 

git add . 

git commit –m “project 2 completed” 

git push origin main 

Output: 

<img width="1919" height="971" alt="Screenshot 2026-01-08 141051" src="https://github.com/user-attachments/assets/c879fec2-3490-4518-bcb0-dab3a3a123d9" />



 
 
 
 
 

 

 

 

 
