#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <set>
#include <vector>
using namespace std;


void dfs(int matrix[][4], int row, int col, vector<int> &cluster) {
    cluster.push_back(0);
    matrix[row][col] = 1;
    for(int dy = -1; dy <= 1; ++dy) {
        int nextRow = row + dy;
        if(nextRow < 0 || nextRow > 3)
            continue;
        for(int dx = -1; dx <= 1; ++dx) {
            int nextCol = col + dx;
            if(nextCol < 0 || nextCol > 3)
                continue;
            if(matrix[nextRow][nextCol] == 0) {
                dfs(matrix, nextRow, nextCol, cluster);
            }
        }
    }
}

/*
 0 0 1 0
 0 1 1 1
 1 1 0 1
 0 1 1 0
 */
vector<vector<int> > matrixAdj(int matrix[][4], int rows) {
    vector<vector<int> > clusters;
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < 4; j++)
            if(matrix[i][j] == 0) {
                vector<int> cluster;
                dfs(matrix, i, j, cluster);
                clusters.push_back(cluster);
            }
    }
    return clusters;
}

/*
 {A, B, C}
 {C, E}
 {E, K}
 {L, M}
 {F, G, H}
 {F, I}
 {J}
 */
void mergeSets(vector<set<string> > &sets) {
    set<int> mergedIndexes;
    vector<set<string> > mergedSets;
    for(int i = 0; i < sets.size(); i++) {
        if(mergedIndexes.find(i) != mergedIndexes.end())
            continue;
        set<string> current = sets.at(i);
        set<string> intersection;
        for(int j = i+1; j < sets.size(); j++) {
            set<string> next = sets.at(j);
            set_intersection(current.begin(), current.end(), next.begin(), next.end(),
                             inserter(intersection, intersection.begin()));
            if(!intersection.empty()) {
                current.insert(next.begin(), next.end());
                mergedIndexes.insert(i);
                mergedIndexes.insert(j);
                intersection.clear();
            }
        }
        mergedSets.push_back(current);
    }
    for(auto ms: mergedSets) {
        for(auto s: ms)
            cout << s;
        cout << '\n';
    }
}

double postFixCalc(const string &expression) {
    stack<double> s;
    stringstream ss(expression);
    string item;
    double op1;
    double op2;
    while(getline(ss, item, ' ')){
        if(item == "+") {
            op1 = s.top();
            s.pop();
            op2 = s.top();
            s.pop();
            s.push(op1 + op2);
        }
        else if(item == "-") {
            op1 = s.top();
            s.pop();
            op2 = s.top();
            s.pop();
            s.push(op1 - op2);
        }
        else if(item == "*") {
            op1 = s.top();
            s.pop();
            op2 = s.top();
            s.pop();
            s.push(op1 * op2);
        }
        else if(item == "/") {
            op1 = s.top();
            s.pop();
            op2 = s.top();
            s.pop();
            s.push(op1 / op2);
        }
        else {
            s.push(stod(item));
        }
    }
    return s.top();
}

// input is all positive integers in order
int findSmallestMissingInt(int intSeq[], int arraySize) {
    int offset = intSeq[0] - 0;
    for(unsigned int i = 0; i < arraySize; i++) {
        if(intSeq[i] != i + offset)
            return intSeq[i-1] + 1;
    }
    return -1;
}

// input will include 'a' and not have missing letters between 'a' and farthest letter
char findDuplicateLetter(char charSeq[], int arraySize) {
    for(unsigned int i = 0; i < arraySize; i++) {
        int diff = charSeq[i] - 97;
        if(diff != i) {
            if(charSeq[diff] == charSeq[i])
                return charSeq[i];
            else {
                char tmp = charSeq[diff];
                charSeq[diff] = charSeq[i];
                charSeq[i] = tmp;
            }
        }
    }
    return NULL;
}

vector<set<string> > getSets(){
    vector<set<string> > sets;
    set<string> tmp;
    tmp.insert("A");
    tmp.insert("B");
    tmp.insert("C");
    sets.push_back(tmp);
    
    tmp.clear();
    tmp.insert("C");
    tmp.insert("E");
    sets.push_back(tmp);
    
    tmp.clear();
    tmp.insert("E");
    tmp.insert("K");
    sets.push_back(tmp);
    
    tmp.clear();
    tmp.insert("L");
    tmp.insert("M");
    sets.push_back(tmp);
    
    tmp.clear();
    tmp.insert("F");
    tmp.insert("G");
    tmp.insert("H");
    sets.push_back(tmp);
    
    tmp.clear();
    tmp.insert("F");
    tmp.insert("I");
    sets.push_back(tmp);
    
    tmp.clear();
    tmp.insert("J");
    sets.push_back(tmp);
    return sets;
}

int main(int argc, char** argv) {
    /*
     char letters[] = {'b', 'a', 'c', 'a', 'c'};
     int arraySize = (int)sizeof(charSeq)/sizeof(charSeq[0])
     char dup = findDuplicateLetter(letters);
     cout << dup << '\n';
     */
    
    /*
     int ints[] = {1, 2, 5};
     int arraySize = (int)sizeof(ints)/sizeof(ints[0]);
     int missing = findSmallestMissingInt(ints, arraySize);
     cout << missing << '\n';
     */
    
    /*
     double result = postFixCalc("3 5 +");
     cout << result << '\n';
     */
    /*
    vector<set<string> > sets = getSets();
    mergeSets(sets);
    */
    /*
     0 0 1 0
     0 1 1 1
     1 1 0 1
     0 1 1 0
     */
    int matrix[4][4];
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            matrix[i][j] = 1;
    matrix[0][0] = 0;
    matrix[0][1] = 0;
    matrix[0][3] = 0;
    matrix[1][0] = 0;
    matrix[2][2] = 0;
    matrix[3][0] = 0;
    matrix[3][3] = 0;
    vector<vector<int> > clusters = matrixAdj(matrix, 4);
    cout << clusters.size() << '\n';
}
