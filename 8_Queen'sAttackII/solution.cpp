#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles) {
    int m;
    int ans;
    int top,under,right,left,tr,ur,tl,ul;
    
    top = 0;
    right = 0;
    tr = 0;
    under = 0;
    left = 0;
    tl = 0;
    ul = 0;
    ur = 0;
    
    m = (n-1) * 2 + n - max(r_q,c_q) + min(r_q,c_q) - 1 + min(r_q-1,n-c_q) + min(n-r_q,c_q-1);
    
    for (int i=0;i<k;i++) {
        if (k==0) {
            break;
        }
        if (obstacles[i][0] == r_q) {
            if (obstacles[i][1] > c_q && (n-obstacles[i][1]+1) > right) {
                right = n-obstacles[i][1]+1;
            }
            else if (obstacles[i][1] < c_q && obstacles[i][1] > left) {
                left = obstacles[i][1];
            }
        }
        else if (obstacles[i][1] == c_q) {
            if (obstacles[i][0] > r_q && (n-obstacles[i][0]+1) > top) {
                top = n-obstacles[i][0]+1;
            }
            else if (obstacles[i][0] < r_q && obstacles[i][1] > under) {
                under = obstacles[i][0];
            }
        }
        else if (abs(obstacles[i][0]-r_q) ==  abs(obstacles[i][1]-c_q)) {
            if (obstacles[i][0]>r_q && obstacles[i][1]>c_q && n-max(obstacles[i][0],obstacles[i][1])+1 > tr) {
                tr = n-max(obstacles[i][0],obstacles[i][1])+1;
            }
            else if (obstacles[i][0]>r_q && obstacles[i][1]<c_q && min(n-obstacles[i][0]+1,obstacles[i][1]) > tl) {
                tl = min(n-obstacles[i][0]+1,obstacles[i][1]);
            }
            else if ((obstacles[i][0]<r_q && obstacles[i][1]>c_q) && min(obstacles[i][0],n-obstacles[i][1]+1) > ur) {
                ur = min(obstacles[i][0],n-obstacles[i][1]+1);
            }
            else if ((obstacles[i][0]<r_q && obstacles[i][1]<c_q) && min(obstacles[i][0],obstacles[i][1]) > ul) {
                ul = min(obstacles[i][0],obstacles[i][1]);
            }
        }
    }
    ans = m - right - left - top - under - tr - tl - ur -ul;
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int k = stoi(first_multiple_input[1]);

    string second_multiple_input_temp;
    getline(cin, second_multiple_input_temp);

    vector<string> second_multiple_input = split(rtrim(second_multiple_input_temp));

    int r_q = stoi(second_multiple_input[0]);

    int c_q = stoi(second_multiple_input[1]);

    vector<vector<int>> obstacles(k);

    for (int i = 0; i < k; i++) {
        obstacles[i].resize(2);

        string obstacles_row_temp_temp;
        getline(cin, obstacles_row_temp_temp);

        vector<string> obstacles_row_temp = split(rtrim(obstacles_row_temp_temp));

        for (int j = 0; j < 2; j++) {
            int obstacles_row_item = stoi(obstacles_row_temp[j]);

            obstacles[i][j] = obstacles_row_item;
        }
    }

    int result = queensAttack(n, k, r_q, c_q, obstacles);

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

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
