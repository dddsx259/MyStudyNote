#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>

#define NITER 1000000

int Count=0;

sem_t binarySem;		/* Use as a mutex */

void * ThreadAdd(void * a)
{
    int i, tmp;

    for(i = 0; i < NITER; i++)
    {
	    sem_wait(&binarySem);
	    tmp = ++Count;
	    sem_post(&binarySem);
	    //if (!(tmp % 100000))
			  //printf("\nThread %d\tcount value = %d", *(int *)a, tmp);
    }
	pthread_exit(NULL);
}

int main(int argc, char * argv[])
{
    pthread_t tid1, tid2;
    int id1=1, id2=2;

    if (sem_init(&binarySem, 0, 1) == -1)
    {
	    printf("Error initialize the semaphore\n");
	    exit(1);
    }

    if(pthread_create(&tid1, NULL, ThreadAdd, (void *)&id1))
    {
    	printf("ERROR creating thread 1\n");
    	exit(1);
    }

    if(pthread_create(&tid2, NULL, ThreadAdd, (void *)&id2))
    {
    	printf("ERROR creating thread 2\n");
    	exit(1);
    }

    if(pthread_join(tid1, NULL))	/* wait for the thread 1 to finish */
    {
    	printf("ERROR joining thread\n");
    	exit(1);
    }

    if(pthread_join(tid2, NULL))        /* wait for the thread 2 to finish */
    {
    	printf("ERROR joining thread\n");
    	exit(1);
    }

    if (Count < 2 * NITER)
        printf("\nBOOM! count is %d, should be %d.\n", Count, 2*NITER);
    else
        printf("\nOK! count is %d\n", Count);

    sem_destroy(&binarySem);

    pthread_exit(NULL);
}
