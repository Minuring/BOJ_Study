#include <iostream>
using namespace std;
int main() {
	int y, r;
	cin >> y;
	if (y % 4 == 0 && y % 100 != 0) {
		r = 1;
	}else if (y % 4 == 0 && y % 400 == 0) {
		r = 1;
	}
	else {
		r = 0;
	}
	cout << r;
	return 0;
}