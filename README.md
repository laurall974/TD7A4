# TD7 - Cloud computing
## 🌟 Goal

We want to create a container with flask that connects to a mongodb which runs on another container. Fetches data and shows it on a webpage on your host machine.

Use Docker to reads a text file on your host and shows the content on a web page. Any changes in the content of this file should be shown by refreshing the web page.

Make the database persistent.

## 👷 Prerequisites

1. First fork this repository then clone it on your computer.

2. Download Docker if you don't have it. Check  `docker --version`

## 🗒 Without docker compose 

1. Create a bridge network : 
    `docker network create --driver bridge <network-name>`

2. Create a mongoDB container : 
    - Pull the official image from the Docker repository : `docker pull mongo`
    - Start the MongoDB container, specifying the network : `docker run -d --network <network-name> --name <container-mongo-name> mongo`

3. Build Flask image :
    - Go to the repository folder : `cd <path-to-repository>`
    - Build your flask app : `docker build -t flaskapp . `

4. Create a volume : `docker volume create mongodb_data`

5. Start the Flask container : `docker run -d --network <network-name> --name <container-flask-name> -p 5000:5000 -v mongodb_data:/data/db -v <your-path>/host_file:/app/data flaskapp`
 

The text file `text.txt` is the one you need to modify to display something else on your browser. 

Check the result : http://localhost:5000/text & http://localhost:5000

You can also veirfy mounts : `docker inspect <container-mongo-name>`

## 🗒 With docker compose
This one will be very quick. 

1. Go to the repository folder : `cd <path-to-repository>`

2. Run : `docker compose up -d`



  




