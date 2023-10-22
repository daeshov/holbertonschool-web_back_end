# For Node_js_basic

# Use Ubuntu 18.04 base image
FROM ubuntu:18.04

# This will stop openssh-server installer from opening a dialog,
# which would require human input
ENV DEBIAN_FRONTEND=noninteractive

# Update APT and upgrade currently installed software
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - 
RUN apt-get install -y nodejs

# Install SSH so we can connect to the container
RUN apt-get install -y openssh-server

# Install other software as needed
# Example:
# RUN apt-get install -y nodejs npm
# RUN npm install -g create-react-app
# RUN apt-get install -y python3 python3-pip
# RUN pip3 install flask

# Make python3.7 the default python3 - it it exists, remove it, then create it
RUN if [ -e /usr/bin/python3 ]; then rm /usr/bin/python3; fi && ln -s /usr/bin/python3.7 /usr/bin/python3

# Update pip
RUN python3 -m pip install --upgrade pip

# Copy your requirements file into the container
COPY requirements.txt .

# Install the Python packages using pip3
RUN pip3 install --no-cache-dir -r requirements.txt

# Start the SSH service
RUN service ssh start

# Setup git config - replace with your info
RUN git config --global user.email "jdarahthomas@gmail.com"
RUN git config --global user.name "daeshov"

# Example of how to include your SSH key for GitHub:
# COPY host-machine-github-private-key /root/.ssh/github-private-key
# RUN chmod 600 /root/.ssh/github-private-key
# RUN echo 'eval `ssh-agent -s`' >> /root/.bashrc
# RUN echo 'ssh-add ~/.ssh/github' >> /root/.bashrc

# Run the SSH service on container startup
CMD ["/usr/sbin/sshd", "-D"]