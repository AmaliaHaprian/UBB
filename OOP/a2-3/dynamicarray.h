#pragma once
#include "domain.h"

typedef void* TElem;

typedef struct {
    int cap;
    int size;
	TElem* elems;
} DynamicArray;

/*
* Creates a dynamic array
* Input: an integer cap, meaning the maximum capacity of the dynamic array
* Output: returns a pointer to a DynamicArray structure
*/
DynamicArray* createDynamicArray(int cap);

/*
* Destroys a dynamic array, freeing the memory allocated for it
* Input: a pointer to a DynamicArray structure
* Output: -
*/
void destroyArray(DynamicArray* da);

/*
* Adds an element to the dynamic array
* Input: a pointer to a DynamicArray structure and a TElem element
* Output: -
*/
void addElem(DynamicArray* da, TElem elem);

/*
* Deletes an element from the dynamic array
* Input: a pointer to a DynamicArray structure, a string name and a string category
* Output: 1 if the element was deleted successfully, 0 if the element was not found
*/
int deleteElem(DynamicArray* da, char* name, char* category);

TElem getElemOnPos(DynamicArray* arr, int idx);

int getSize(DynamicArray* da);