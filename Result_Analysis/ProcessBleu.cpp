/*input
2
adjasd
asdfjhk kjlashd
*/
/*

author : Avi Mallick

          CSE'15 SUST

*/
#include <bits/stdc++.h>
//#include <sstream>
//#include <cstdlib>
//#include <cctype>
//#include <cmath>
//#include <algorithm>
//#include <set>
//#include <queue>
//#include <stack>
//#include <list>
//#include <iostream>
//#include <fstream>
//#include <numeric>
//#include <string>
//#include <vector>
//#include <cstring>
//#include <map>
//#include <iterator>
//#include<numeric>
// #include<complex>
#define pii                   pair<int,int>
#define tii                   pair<int,pair<int,int> >
#define mkp                   make_pair
#define fs                    first
#define sc                    second
#define pb                    push_back
#define ppb                   pop_back()
#define pcase(x)              printf("Case #%d: ",x)
#define hi                    cout<<"hi"<<endl;
#define mod                   1000000007
// #define inf                   1e18+1
#define pi                    acos(-1.0)
#define mem(arr,x)            memset((arr), (x), sizeof((arr)));
#define FOR(i,x)              for(int i=0;i<(x); i++)
#define FOR1(i,x)             for(int i = 1; i<=(x) ; i++)
#define jora(a,b)             make_pair(a,b)
#define tora(a,b,c)           jora(a,jora(b,c))
#define sf1(a)                scanf("%d",&a)
#define sf2(a,b)              scanf("%d %d",&a,&b)
#define sf3(a,b,c)            scanf("%d %d %d",&a,&b,&c)
#define pf1(a)                printf("%d\n",a);
#define pf2(a,b)              printf("%d %d\n",a,b)
#define pf3(a,b,c)            printf("%d %d %d\n",a,b,c)
#define sf1ll(a)              scanf("%lld",&a)
#define sf2ll(a,b)            scanf("%lld %lld",&a,&b)
#define sf3ll(a,b,c)          scanf("%lld %lld %lld",&a,&b,&c)
#define pf1ll(a)              printf("%lld\n",a);
#define pf2ll(a,b)            printf("%lld %lld\n",a,b)
#define pf3ll(a,b,c)          printf("%lld %lld %lld\n",a,b,c)
#define N 7*100000+5
#define level 26
#define eps 1e-9

// #define mat vector<vector<int> >
// #define m 6
using namespace std;
typedef long long lint;
vector<string>machineGeneratedSummary;
vector<string>humanGeneratedSummary;
vector<double>bleuScores;
string getFileName(string filePath,int id,string extensionName)
{
	string idString ="";
	while(id>0)
	{
		idString.push_back((char)id%10+'0');
		id/=10;
	}
	reverse(idString.begin(),idString.end());
	return filePath+idString+extensionName;
}
int main()
{
	ifstream infile;
	infile.open("~/Desktop/DeepNewsPaper/BLEU.txt");
	int cnt = 0;
	string  line;
	double sum = 0.0;
	double tot = 0.0;
	while(!infile.eof())
	{
		getline(infile,line);
		
		if(cnt>=5)
		{

				if(cnt%5==0)
				{
					stringstream ss(line);
					double bleu;
					ss>>bleu;
					bleuScores.push_back(bleu);
					tot+=1.0;
					sum+=bleu;
				}
				if(cnt%5==1)
				{
					machineGeneratedSummary.push_back(line);
			
				}
				if(cnt%5==2)
				{
					humanGeneratedSummary.push_back(line);
				
					
				}
			
		}
			cnt++;
	}
	cout<<sum/tot<<endl;
		infile.close();
		bleuScores.pop_back();
		//getBleuAverage();
		ofstream offile;
		offile.open("~/Desktop/DeepNewsPaper/hyp.txt");
		for(int i=0;i<machineGeneratedSummary.size();i++)
		{

			
			offile<<machineGeneratedSummary[i]<<endl;
		}
			offile.close();
		offile.open("~/Desktop/DeepNewsPaper/ref.txt");
		for(int i=0;i<humanGeneratedSummary.size();i++)
		{

			
			offile<<humanGeneratedSummary[i]<<endl;
		}
			offile.close();

	}