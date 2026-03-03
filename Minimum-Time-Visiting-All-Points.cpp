1int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
2    int ans =0;
3    for(int i=1;i<pointsSize;i++)
4    {
5        ans+=fmax(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]));
6    }
7    return ans;
8}