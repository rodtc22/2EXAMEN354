#include <bits/stdc++.h>
using namespace std;

template <typename T> ostream& operator << (ostream &os, const vector<T> &v) { os << "["; for (int i = 0 ;i < v.size() ;i++) {if (i) os << ", "; os << v[i];} os << "]"; return os;}
template <typename T> istream& operator >> (istream &is, vector<T> &v) { for (T &x : v) is >> x; return is;}
template <typename A, typename B> ostream& operator << (ostream &os, const pair<A,B>& p) { return os << "(" << p.first <<", " << p.second << ")"; }
template <typename A, typename B> istream& operator >> (istream &is, pair<A,B> &p) { return is >> p.first >> p.second; }

#define		fastio      	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define		runio			freopen("in","r", stdin), freopen("out", "w", stdout);
#define		all(_)      	(_).begin(), (_).end()
#define		sz(_)     		int(_.size())
#define		endl			'\n'
typedef		long long		ll;
typedef		pair<int,int>	pii;
const		ll				mod = 1e9 + 7;
const		ll				inf = 1e9;
const		double 			eps = 1e-9;
const		int 			N = 2e5 + 2;
int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};

struct datos{
	ll x = 0, fx, nuevo = 0;
	string xbin, cruce, mutacion;
};

ostream& operator << (ostream& os, const datos & d) {
	return os << d.x << " ; " << d.fx << " ; " << d.xbin << " ; " << d.cruce << " ; " << d.mutacion << " , " << d.nuevo 	;
}

const int M = 40;

string to_bin(ll x) {
	return bitset<M>(x).to_string();
}

ll to_dec (string x) {
	ll acu = 0;
	for (char c : x) {
		acu = acu << 1;
		if (c == '1')
			acu |= 1;
	}
	return acu;
}

void f_cruce (vector<datos> &ar, int k) {
	int n = ar.size();
	for (int i = 0 ;i < n ;i+=2) {
		string a = ar[i].xbin, b = ar[i+1].xbin;
		string c = a.substr(0,k) + b.substr(k, M-k);
		string d = b.substr(0,k) + a.substr(k, M-k);
		ar[i].cruce  = c;
		ar[i+1].cruce = d;
	}
}

void f_mutacion (vector<datos> &ar, int k) {
	for (auto &x : ar) {
		string s = x.cruce;
		char c = (s[k-1] == '0'? '1' : '0');
		s[k-1] = c;
		x.mutacion = s;
	}
}

void f_nueva_generacion (vector<datos> &ar) {
	for (auto &x : ar)
		x.nuevo = to_dec(x.mutacion);
}

void f_actualiza_generacion (vector<datos> v, vector<ll> &ar) {
	for (int i = 0 ;i < ar.size(); i++ ) {
		ar[i] = v[i].nuevo;
	}
}

ll funcion (ll x) {
	return x * x + 4;
}

void mostrar (vector<datos> v) {
	for (auto x : v) cout << x.x << endl; cout << endl;
	for (auto x : v) cout << x.fx << endl; cout << endl;
	for (auto x : v) cout << x.xbin << endl; cout << endl;
	for (auto x : v) cout << x.cruce << endl; cout << endl;
	for (auto x : v) cout << x.mutacion << endl; cout << endl;
	for (auto x : v) cout << x.nuevo << endl; cout << endl;
	cout << endl;
}

void f (vector<ll> &ar) {
	sort(ar.rbegin(),ar.rend());
	vector<datos> v;
	for (ll x : ar) {
		datos d;
		d.x = x;
		d.fx = funcion(d.x);
		d.xbin = to_bin(d.fx);
		v.push_back(d);
	}

	f_cruce(v, 35);
	f_mutacion(v, 34);
	f_nueva_generacion(v);
	f_actualiza_generacion(v, ar);

	for (auto x : v) cout << x << endl; 
	cout << endl;

}


int main () {
	int n; cin >> n;
	vector<ll> ar(n); cin >> ar;
	for (int gen = 1 ; gen <= 4 ; gen++) {
		cout << "=========== GENERACION " << gen << " ===========" << endl;
		f(ar);

	}

	return 0;
}

/*
It's your road and yours alone.
Others may walk it with you, but no one can walk it for you
Do it yourself!
*/