#include<iostream>
#include<omp.h>
using namespace std;

class BinSearch
{
	int a[10] , n , key , low , high;
	public : 
			void display();
			void accept();
			void sort();
			void search();
}obj;

void BinSearch :: display()
{
	cout<<"\n Array is : ";
	for(int i = 0 ; i < n ; i ++)
	{
		cout <<" "<<a[i];
	}
}

void BinSearch :: accept()
{
	cout<<"\n Enter The number of elements you want : ";
	cin>>n;
	
	for(int i = 0 ; i < n ; i ++)
	{
		cout <<"\n val : ";
		cin>>a[i];
	}
	display();
}

void BinSearch :: sort()
{
	for(int i = 0 ; i < n ; i++)
	{
		for(int j = i+1 ; j < n ; j++)
		{
			if (a[i]>a[j])
			{
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	display();
}

void BinSearch :: search()
{
	low = 0 ;
	high = n-1;
	int mid = ((low+high)/2)+1;
	
	cout<<"\n Enter Key to search : ";
	cin>>key;
	
	if(key<a[0] || key>a[high])
	{
		cout<<"\n Invalid key \n";
	}
	else	
	{	
		#pragma omp parallel sections
		{
		#pragma omp section
		while(low <= high && a[mid] != key)
		{
			if (a[mid]>key)
				high = mid-1;
			else
				low = mid+1;
			mid = (low+high)/2;
		} 
		}
		if (a[mid]==key)
		{
			cout<<"key found at loaction "<<mid;
			//code for duplicate will come here ...	
		}
		else
			cout<<"key not found";
	}


}

int main()
{
	double st;
	st = omp_get_wtime();
	obj.accept();
	obj.sort();
	obj.search();
	cout<<"\n Required time is time : "<<omp_get_wtime() - st;
	cout<<"\n";
	return 0;
}
