/*
ID: neel.pa1
LANG: C++11
TASK: numtri
*/
#include<string.h>
#include<stdio.h>
#define MAX_N 1005

int a[MAX_N][MAX_N];
int dp[MAX_N][MAX_N];

int max(int a, int b)
{
  return a > b ? a : b;
}

int dfs(int i,int j,int end)
{
  if(dp[i][j] != -1)
  {
    return dp[i][j];
  }
  else if(i <= end)
  {
    return dp[i][j] = a[i][j] + max(dfs(i+1,j,end), dfs(i+1,j+1,end));
  }
  else
  {
    return 0;
  }
}

int main () {
  FILE *fin  = fopen ("numtri.in", "r");
  FILE *fout = fopen ("numtri.out", "w");
  int r,i,j;

  memset(dp, -1, sizeof dp);

  fscanf(fin,"%d",&r);

  for(i = 1;i<=r;i++)
    for(j = 1;j<=i;j++)
      fscanf(fin,"%d",&a[i][j]);

  fprintf(fout,"%d\n", dfs(1,1,r));

  fclose(fin);
  fclose(fout);
  return 0;
}