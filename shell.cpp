#include <unistd.h> 
#include <bits/stdc++.h> 

using namespace std;

string strip(string s) {
    string proc;
    for(char c : s)
        if(c != ' ')
        {
            proc.push_back(c);
            break;
        }
    return s;
}

void parse(string cmd) {
    // for(char s : cmd)
    // cout<<cmd<<endl;
}

int main(int argc, char* argv[]) {
    string cmd; 

    while(1) 
    {
        cout << "sched> ";
        getline(cin, cmd);
        if(cmd == "exit")
        {
            cout << "EXITING ...\n";
            exit(EXIT_SUCCESS);
        }
        parse(cmd);
    }

    return 0;
}