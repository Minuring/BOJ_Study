#include <iostream>
using namespace std;
int main() {
	int num;

	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	cin >> num;

	for (int i = 1; i <= num; i++) {

		for (int j = 0; j < (num - i); j++) {
			cout << " ";
		}
		
		for (int s = 0; s < i; s++) {
			cout << "*";
		}

		cout << "\n";
	}
	return 0;

}