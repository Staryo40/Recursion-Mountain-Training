#include <stdio.h>
#include <stdlib.h>
#include "ArrayList.h"

int LCG(int seed, int repeat, int range){
    if (repeat == 0){
        return (seed % range) + 1;
    }
    int newseed = ((9091 * seed + 896712) % range) + 1;
    if (newseed < 0){
        newseed = -newseed;
    }
    return LCG(newseed, repeat-1, range);
}

int generateRandomInt(int range, int repeat){
    int seed = 1234567;
    int res = LCG(seed, repeat, range);
    return res;
}

ArrayList generateRandomList(int size, int range){
    int *list = (int *) malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++){
        list[i] = generateRandomInt(range, i);
    } 
    ArrayList array = {list, size};
    return array;
}

void printList(ArrayList list){
    printf("[");
    for (int i = 0; i < list.length; i++){
        printf("%d", list.list[i]);
        if (i != list.length-1){
            printf(",");
        }
    }
    printf("]\n");
}