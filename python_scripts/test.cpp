#include <iostream>
#include "opencv2/opencv.hpp"
using namespace std;
using namespace cv;
int main(int argc, char* argv[]){
	const char *out_file=argv[1];
	Mat output;
	VideoCapture cp(0);
	if(!cp.isOpened()){
	cout <<"Gabim";
	return -1;
	}
	cp >> output;
	if(output.empty()){
	cout <<"Error";
	return -1;
	}
	imwrite(out_file,output);
	return 0;
}
