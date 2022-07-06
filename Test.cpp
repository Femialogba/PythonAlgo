#include <bits/stdc++.h>

using namespace std;

string to_binary(int x) {
	string s;
	while(x > 0) {
		s += (x % 2 ? '1' : '0');
		x /= 2;
	}
	reverse(s.begin(), s.end());
	return s;
}

int main() {
	cout << "13 = " << to_binary(13) << endl; // 1101
	
	int x = 53;
	int y = 28;
	cout << "x = " << to_binary(x) << ", y = " << to_binary(y) << endl;
	
	cout << "AND, OR, XOR:" << endl;
	cout << to_binary(x & y) << " " << to_binary(x | y) << " " << to_binary(x ^ y) << endl;
}
//In comments, Rezwan.Arefin01 suggested a simpler way
//to print a number in binary format. cout << bitset<8>(x); prints 
// a number after converting it into a bitset, which can be printed. 
//There will be more info about bitsets in part 2.