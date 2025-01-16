#include <stdio.h>
#include <stdlib.h>
#include "ArrayList.h"

/// @brief 
/// @param l 
/// @return 
ArrayList mergeSort(ArrayList l){
    // Base case
    if (l.length == 1){
        return l;
    }

    // Dividing the list
    int firstLength = l.length/2;
    int *firsthalf = (int *)malloc(sizeof(int) * firstLength);
    for (int i = 0; i < firstLength; i++){
        firsthalf[i] = l.list[i];
    }
    ArrayList firstList = {firsthalf, firstLength};

    int secondLength = l.length - l.length/2;
    int *secondhalf = (int *)malloc(sizeof(int) * secondLength);
    int j = l.length/2;
    for (int i = 0; i < secondLength; i++){
        secondhalf[i] = l.list[j];
        j++;
    }
    ArrayList secondList = {secondhalf, secondLength};

    // Recursion
    ArrayList sortedFirst = mergeSort(firstList);
    ArrayList sortedSecond = mergeSort(secondList);

    // Combining sorted lists from recursion
    ArrayList res;
    int *resList = (int *)malloc(sizeof(int) * l.length);
    res.list = resList;
    res.length = l.length;
    int firstNumer = 0;
    int secondNumer = 0;

    for (int i = 0; i < l.length; i++){
        if (firstNumer == firstLength){
            res.list[i] = sortedSecond.list[secondNumer]; 
            secondNumer++;
        } else if (secondNumer == secondLength){
            res.list[i] = sortedFirst.list[firstNumer];
            firstNumer++;
        } else {
            if (sortedFirst.list[firstNumer] <= sortedSecond.list[secondNumer]){
                res.list[i] = sortedFirst.list[firstNumer];
                firstNumer++;
            } else {
                res.list[i] = sortedSecond.list[secondNumer];
                secondNumer++;
            }
        }
    }

    printf("Sorted list = ");
    printList(res);

    free(firsthalf);
    free(secondhalf);

    return res;
}

int main (){
    ArrayList list = generateRandomList(11, 100);
    printList(list);
    ArrayList sorted = mergeSort(list);
    printList(sorted);
    return 0;
}