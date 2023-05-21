#include <iostream>
#include <functional>
#include <algorithm>
#include <fstream>
using namespace std;
int main() {
    ifstream ifs("input-7.txt");
    ofstream ofs;
    ofs.open("answer7.txt");
    int n;
    int x; 
    ifs >> n >> x;
    int a[100000];
    for (int i = 0; i < n; i++) ifs >> a[i];
    std::sort(a, a + n, std::greater<int>());
    int max = 0, sum = 0;
    for (int i = 0; i < n-1; i++) {
        if (a[i] >= x) continue;
        for (int j = i+1; j < n; j++) {
            sum = a[i] + a[j];
            if (sum > x) continue;
            if (sum > max) max = sum;
            if (sum == x) {
                ofs << x;
                return 0;
            }
            break;
        }
        if(a[i]+a[i+1]<max) break;
    }
    ofs << max;
}
