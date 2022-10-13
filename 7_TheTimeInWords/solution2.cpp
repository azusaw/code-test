#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'timeInWords' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER m
 */

string numToWords(int n) {
    
    string num[21] = {
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                    "ten",
                    "eleven",
                    "twelve",
                    "thirteen",
                    "fourteen",
                    "quarter",
                    "sixteen",
                    "seventeen",
                    "eighteen",
                    "nineteen",
                    "twenty"
    };

    if (n<=20) return num[n-1];
    return num[19] + " " + num[n-21];
}

string timeInWords(int h, int m) {
    vector<string> res;
    string ans;
    
    if (m==0) {
        res = {numToWords(h),"o' clock"};
    }
    else if (m%15==0) {
        res.push_back(m==30?"half":"quarter");
        res.push_back(m!=45?"past":"to");
        res.push_back(m!=45?numToWords(h):numToWords(h+1));
    }
    else {
        res.push_back(m<30?numToWords(m):numToWords(60-m));
        res.push_back(m==1||m==59?"minute":"minutes");
        res.push_back(m<30?"past":"to");
        res.push_back(m<30?numToWords(h):numToWords(h+1));
    }
    
    for(auto &e: res) {
        ans += e + " ";
    }
    ans.pop_back();
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string h_temp;
    getline(cin, h_temp);

    int h = stoi(ltrim(rtrim(h_temp)));

    string m_temp;
    getline(cin, m_temp);

    int m = stoi(ltrim(rtrim(m_temp)));

    string result = timeInWords(h, m);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
