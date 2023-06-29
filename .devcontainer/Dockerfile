FROM patfiredragon/rosi-container:latest

RUN echo "source /workspaces/rosi_python_api/catkin_ws/devel/setup.bash" >> /root/.bashrc

RUN apt-get -y install libcanberra-gtk-module \
                       libcanberra-gtk3-module \
                       python-opencv
