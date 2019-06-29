#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

vector<int>parent(100),rank1(100);

void make_set(int v)
{
    parent[v]=v;
    rank1[v]=0;
}

int find_set(int v)
{
    if(v!=parent [v])//first find set 3 er parent ki 3 nijei kina,as parent so;again chack 2 er parent 2 kina,as no
        parent[v]=find_set(parent[v]);//find 2 er parent which is 1 again go to the loop and check 1 er parent ki 1 kina
    return (parent[v]);//return 3//as 1 is the parent of its own so return 1
}//here to check the edge whether it make a cycle or not

void union_set(int a,int b)
{
    a=find_set(a);
    b=find_set(b);

    if(a!=b)
    {
    if(rank1[a]>rank1[b])
        parent[b]=a;
    else
    {
        parent[a]=b;

    }
    if(rank1[a]==rank1[b])
         ///increase the rank
        rank1[b]++;
    }
}

class Edge
{
public:

    int u,v,weight;
    Edge(int w,int x,int y)
    {
        u=x;
        v=y;
        weight=w;
    }

    bool operator<(Edge const& other)///vitore change krleo jate bahire change na hoe tai constr
    {
        return weight<other.weight;///1st one is the weight of edge,2nd is the wt of the parameter thet was given
    }

};

int main()
{
    int n,e;
    vector<Edge>edges,result;
    int cost=0;


    edges.push_back(Edge(4,1,2));
    edges.push_back(Edge(1,2,4));
    edges.push_back(Edge(6,1,3));
    edges.push_back(Edge(3,4,5));
    edges.push_back(Edge(2,3,4));
    edges.push_back(Edge(5,1,6));
    edges.push_back(Edge(9,6,4));
    edges.push_back(Edge(9,3,5));

    n = 6;
    for(int i=0;i<n;i++)
    {
        make_set(i);
    }

    sort(edges.begin(),edges.end());


    for(int i=0;i<edges.size();i++)
    {
        if(find_set(edges[i].u)!=find_set(edges[i].v))
        {
            cost+=edges[i].weight;
            result.push_back(edges[i]);
            union_set(edges[i].u,edges[i].v);
        }
    }
    printf("%d \n",cost);


}

