//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int minValue(string s, int k){
       priority_queue<int>pq;//maxHeap
       map<int,int>mp;
       for(int i=0;i<s.size();i++){
           mp[s[i]]++;
       }
       for(auto pai:mp){
           pq.push(pai.second);
       }
       while(k>0){
           int t = pq.top();
           pq.pop();
           t-=1;
           k-=1;
           pq.push(t);
       }
       int ans = 0;
       while(pq.size()>0){
           ans+=(pq.top()*pq.top());
           pq.pop();
       }
       return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        int k;
        cin>>s>>k;
        
        Solution ob;
        cout<<ob.minValue(s, k)<<"\n";
    }
    return 0;
}
// } Driver Code Ends