#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo bash -c 'echo -e "<!DOCTYPE html>\n<html>\n\t<p>test file</p>\n</html>" > /data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/	location/i \tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
