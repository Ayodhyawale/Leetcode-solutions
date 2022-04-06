class Solution {
public:
    int threeSumMulti(vector<int>& arr, int t) {
        int n=arr.size();
        const long int m=1e9+7;
        int res=0;
         unordered_map<int,int> mp;
        
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            { int x=arr[i]+arr[j]; x=(t-x);
                res=(res%m+mp[x]%m)%m;
             
            }
 mp[arr[i]]++;       }
        return res;
    }
};