#/bin/bash
sudo apt-get -y install python-dev
sudo apt-get -y install libavresample-dev
sudo apt-get -y install libgstreamer1.0-dev
sudo apt-get -y install libgstreamer-plugins-base1.0-dev**
sudo apt-get -y install python-numpy
sudo apt-get -y install libtbb2
sudo apt-get -y install libtbb-dev
sudo apt-get -y install libjpeg-dev
sudo apt-get -y install libpng-dev
sudo apt-get -y install libtiff-dev
sudo apt-get -y install libjasper-dev
sudo apt-get -y install libdc1394-22-dev
sudo apt-get -y install pylint
sudo apt-get -y install pylint3
sudo apt-get -y install python-tk
sudo apt-get -y install python3-tk
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-numpy
cd /home/pi/opencv/build
cmake -D CMAKE_BUILD_TYPE=Release -D BUILD_EXAMPLES=OFF -D BUILD_DOCS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_TESTS=OFF -D WITH_QT=OFF -D WITH_GTK=ON -D OPENCV_GENERATE_PKCONFIG=ON -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules ./
make -j4
sudo make install
