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
    if (n==0) return "";
    else if (n==1) return "one";
    else if (n==2) return "two";
    else if (n==3) return "three";
    else if (n==4) return "four";
    else if (n==5) return "five";
    else if (n==6) return "six";
    else if (n==7) return "seven";
    else if (n==8) return "eight";
    else if (n==9) return "nine";
    else if (n==10) return "ten";
    else if (n==11) return "eleven";
    else if (n==12) return "twelve";
    else if (n==13) return "thirteen";
    else if (n==15) return "quarter";
    else if (n==20) return "twenty";
    else if (n==30) return "half";
    else if (n>=14 && n<=19) return numToWords(n-10)+"teen";
    else return (numToWords(20) + " " + numToWords(n-20));
}

string minuteToWords(int m) {
    string words;
    int t;
    
    if (m<=30) t = m;
    else t = 60 - m;
    
    if (t==0) return " o' clock";
    else {
        if (t==1) words = numToWords(t) + " minute";
        else if (t!=15 && t!=30) words = numToWords(t) + " minutes";
        else words = numToWords(t); //15,30
    }
    if (m<=30) return words + " past ";
    else return words + " to ";
    
}

string timeInWords(int h, int m) {
    if (m==0) return numToWords(h) + minuteToWords(m);
    else if (m<=30) return minuteToWords(m) + numToWords(h);
    else {
        if (h==12) return minuteToWords(m) + numToWords(1);
        else return minuteToWords(m) + numToWords(h+1);
    }
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
