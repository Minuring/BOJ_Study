#include <iostream>
using namespace std;
int main() {
	int a, b, t, i;

	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	cin >> t;

	for (i = 0; i < t; i++) {
		cin >> a >> b;
		cout << a + b << "\n";
	}
	return 0;
}