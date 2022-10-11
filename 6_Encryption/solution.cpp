#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string encryption(string s) {    
    double root = sqrt(s.size());
    int column = ceil(root);
    int row = ceil(s.size()/double(column));
    string res;
    
    for (int i=0;i<column;i++) {
        for (int j=0;j<row;j++) {
            if(i+column*j < s.size()) {
                res += s[i+column*j];
            }
        }
        res+=" ";
    }
    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = encryption(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
