#include <cjson/cJSON.h>

/*
For programmers: This script will save and load card data in JSON format, which we will discuss later.
For laypeople: The code in this file saves and loads the cards that you see in the game, but in binary :3


For programmers, part 2:
I'm thinking of the following structure:
// Array[Dict[ID, data]]

where...

###  "Array" is an array of 3 elements (3 "LODs": small, medium, large.)
###  "Dict" is just a HashTable
###  ID is the name of the card (so not really a numeric ID... just a unique identifier for the dictionary's keys :3)
###  Data is bytecode (binary, raw info for the images; to be served as input for OpenGL)


so it's actually more like:
// Array<HashTable<char*, void*>>


*/ 


void save_card_data()
{
    FILE *fp = fopen("data.json", "w");
    if (fp == NULL) {
        printf("ERROR 2: Unable to open the file :(\n");
        return 1;
    }
        
    cJSON *json = cJSON_Parse(string);


    fclose(fp);
    return

}



void load_card_data()
{
    FILE *fp = fopen("data.json", "r");
    if (fp == NULL) {
        printf("ERROR 2: Unable to open the file :(\n");
        return 1;
    }
        
    cJSON *json = cJSON_Parse(string);


    fclose(fp);
    return
}
