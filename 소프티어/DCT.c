#include <stdio.h>

int main(void)
{
	int DCT[8];
	int sort = 0;

	// 배열의 각 자리에 한 글자씩 저장
	for(int i=0; i<8; i++) {
		scanf("%d", &DCT[i]);
	}

	for(int i=0; i<7; i++) {
		if(DCT[i] == DCT[i+1]-1) {
			sort = 1;
		}
		else if(DCT[i] == DCT[i+1]+1) {
			sort = -1;
		} else {
			sort = 0;
			printf("mixed");
			break;
		}
	}

	if(sort==1)	printf("ascending");
	else if(sort==-1)	printf("descending");


	return 0;
}
