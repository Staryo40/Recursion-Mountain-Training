typedef struct {
    int *list;
    int length;
} ArrayList;

int LCG(int seed, int repeat, int range);

int generateRandomInt(int range, int repeat);

ArrayList generateRandomList(int size, int range);

void printList(ArrayList list);