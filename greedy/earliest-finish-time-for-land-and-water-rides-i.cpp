class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        int t=4001,mlt=4001,mwt=4001;
        for(int i=0;i<landStartTime.size();i++){
            int lt=landStartTime[i]+landDuration[i];
            for(int j=0;j<waterStartTime.size();j++){
                int tt;
                if(waterStartTime[j]<=lt)  tt=lt+waterDuration[j];
                else tt=waterStartTime[j]+waterDuration[j];
                mlt=min(mlt,tt);
            }
        }
        for(int i=0;i<waterStartTime.size();i++){
            int wt=waterStartTime[i]+waterDuration[i];
            for(int j=0;j<landStartTime.size();j++){
                int tt;
                if(landStartTime[j]<=wt)  tt=wt+landDuration[j];
                else tt=landStartTime[j]+landDuration[j];
                mwt=min(mwt,tt);
            }
        }
        return min(mwt,mlt);
        
    }
};