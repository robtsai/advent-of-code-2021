#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <boost/algorithm/string/split.hpp>
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::istringstream;
using std::ifstream;


int main() {
	ifstream myfile;
	myfile.open("input_files/problem2.txt");
	string mytext;

	vector<string> dir_vec;
	vector<int> unit_vec;

	int n = 0;

	while (getline (myfile, mytext)) {
        istringstream mystream(mytext);

        string direction;
        string units;

        getline(mystream, direction, ' ');
        getline(mystream, units, ' ');

        dir_vec.push_back(direction);
        unit_vec.push_back(stoi(units));

        n++;
	}

	int horizontal = 0;
	int depth = 0;

	for (int i=0; i<n; i++) {
		if (dir_vec[i] == "forward") {
			horizontal += unit_vec[i];
		} else if (dir_vec[i] == "down") {
			depth += unit_vec[i];
		} else if (dir_vec[i] == "up") {
			depth -= unit_vec[i];
		}
	}

	cout << "horizontal " << horizontal << endl;
	cout << "depth " << depth << endl;
	cout << "part 1 answer: " << horizontal * depth << endl;
}