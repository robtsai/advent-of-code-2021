#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream myfile;
	myfile.open("input_files/problem1.txt");

	string myText;

	int n = 0;
	int arr[100000];

	while (getline (myfile, myText)) {
		int num = stoi(myText);
		arr[n] = num;
		n++;
	}

	cout << "There are " << n << " entries" << endl;

	// Part 1

	int numincreasing = 0;

	for (int i=1; i<n; i++) {
		if (arr[i] > arr[i-1]) {
			numincreasing += 1;
		}
	}

	cout << "part 1: There are " << numincreasing << " items that increase." << endl;

	// Part 2 

	int windowincreasing = 0;
	int otherwaytocalc = 0;

	for (int i=3; i<n; i++) {
		int cursum = arr[i] + arr[i-1] + arr[i-2];
		int lagsum = arr[i-1] + arr[i-2] + arr[i-3]; 
		int diff = cursum - lagsum;
		if (diff > 0) {
			windowincreasing += 1;
		}
		// you can test just the endpoints also
		if (arr[i] > arr[i-3]) {
			otherwaytocalc += 1;
		}
	}

	cout << "part 2:  There are " << windowincreasing << " sliding window increases." << endl;
	cout << "part 2:  There are " << otherwaytocalc << " sliding window increases." << endl;

	return 0;
}