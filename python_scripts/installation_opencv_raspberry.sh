#/bin/bash
mkdir opencv 
cd opencv
sudo mkdir /var/rep
sudo mount 10.2.7.10:/var/local/rep /var/rep
sudo apt-key add /var/rep/PublicKey
sudo apt-get update
sudo apt-get install git
git clone copy@10.2.7.10:/var/local/git/opencv
git clone copy@10.2.7.10:/var/local/git/opencv_contrib
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
cd opencv
git checkout $cvVersion
cd opencv_contrib
git checkout $cvVersion
cd opencv
rm CMakeLists.txt
cd ..
sudo apt-get install streamer && sudo apt-get install imagemagick
mkdir build
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
