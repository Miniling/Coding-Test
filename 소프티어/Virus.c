#include <stdio.h>

int main(void){

    // 마리수 K, 증가율 P, 총 시간 N
	long long k,p,n;

	scanf("%d %lld %lld",&k,&p,&n);

	for(int i=1;i<=n;i++){
		k = (k*p)%1000000007;
	}
	printf("%lld", k);

	return 0;
}