#include <bits/stdc++.h>
using namespace std;


int main(){
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int a, b , c;

	int t;
	cin >> t;

	while(t--){
		cin >> a >> b >> c;

		if((b*b) - (4*a*c) < 0)
			cout << "imaginary" << endl;
		else cout << "real" << endl;
	}

	return 0;
}
