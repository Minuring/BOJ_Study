#include <iostream>
using namespace std;
int main() {
	int num, i;
	
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	cin >> num;

	for (i = num; i>0; i--) {
		cout << i << "\n";
	}
	return 0;
}