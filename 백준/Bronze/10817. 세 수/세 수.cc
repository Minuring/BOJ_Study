#include <iostream>
using namespace std;
int main() {
	int a, b, c, mid;
	cin >> a >> b >> c;

	if (a > b) {
		if (a > c) {
			if (b > c) {
				mid = b;
			}
			else {
				mid = c;
			}
		}
		if (a < c) {
			mid = a;
		}
	}

	if (a < b) {
		if (a > c) {
			mid = a;
		}
		else {
			if (b > c) {
				mid = c;
			}
			else {
				mid = b;
			}
		}
	}
	cout << mid;
	return 0;
}