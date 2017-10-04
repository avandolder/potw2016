#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int n;
	int *ns;
	
	scanf("%d", &n);
	ns = (int*)malloc(n * sizeof(int));
	for (int i = 0; i < n; i++) {
		ns[i] = 0;
	}
	
	for (int i = 0; i < n; i++) {
		int j;
		
		scanf("%d", &j);
		if (ns[j - 1]) {
			printf("%d", j);
			break;
		}
		
		ns[j - 1] = 1;
	}
	
	free(ns);
	
	return EXIT_SUCCESS;
}
