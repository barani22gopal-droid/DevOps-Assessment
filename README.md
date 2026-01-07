Docker Practical Assessment 
 
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
<h1>Welcome to Barani's Website</h1> 

    <p>Hosted using NGINX on Linux</p> 

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
docker login 
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

Git repo url:
https://github.com/barani22gopal-droid/DevOps-Assessment.git

• Proof that the site is accessible via the browser. 

 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b5115b14-cd6d-4ab4-b272-1fe8a8966ab0" />

• Proof that Dockerfile  of building the image. 

<img width="1918" height="551" alt="image" src="https://github.com/user-attachments/assets/1d782b59-51ab-4d9b-8232-9514fd6704b7" />

 
 
 
 
 

 

 

 

 
