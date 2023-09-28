#include <iostream>
using namespace std;
int main() {
	int num, i, sum=0;
	cin >> num;

	for (i = 0; i <= num; i++) {
		sum += i;
	}
	cout << sum;
	return 0;
}