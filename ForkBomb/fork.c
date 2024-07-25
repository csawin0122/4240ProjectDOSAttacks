#include <unistd.h>

int main()
{
	// continuously spawn processes
	while(1)
	{
		fork();
	}
	return 0;
}
