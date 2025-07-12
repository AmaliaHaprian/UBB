#include "dynamicarray.h"
#include <stdlib.h>

DynamicArray* createDynamicArray(int cap)
{
	DynamicArray* da = (DynamicArray*)malloc(sizeof(DynamicArray));
	if (da == NULL)
		return NULL;
	da->cap = cap;
	da->size = 0;
	da->elems =(TElem*)malloc(sizeof(TElem) * cap);
	if (da->elems == NULL)
	{
		free(da);
		return NULL;
	}
	return da;

}

void destroyArray(DynamicArray* da)
{
	if (da == NULL)
		return;
	if (da->elems == NULL)
		return;
	//for (int i = 0; i < da->size; i++)
	//	free(da->elems[i]);
	free(da->elems);
	da->elems = NULL;

	free(da);
	da = NULL;
}

void addElem(DynamicArray* da, TElem elem)
{
	if (da == NULL)
		return;
	if (da->elems == NULL)
		return;

	if (da->size == da->cap)
	{
		// resize
		TElem* newElems = malloc(sizeof(TElem) * da->cap * 2);
		if (newElems == NULL)
			return;
		for (int i = 0; i < da->size; i++)
			newElems[i] = da->elems[i];
		free(da->elems);
		da->elems = newElems;
		da->cap *= 2;
	}
	da->elems[da->size++] = elem;
}

int deleteElem(DynamicArray* da, char* name, char* category)
{
	if (da == NULL)
		return;
	if (da->elems == NULL)
		return;
	for (int i = 0; i < da->size; i++)
	{
		Product* p = (Product*)da->elems[i];
		if (strcmp(p->name, name) == 0 && strcmp(p->category, category) == 0)
		{
			free(p);
			for (int j = i; j < da->size - 1; j++)
				da->elems[j] = da->elems[j + 1];
			da->size--;
			return 1;
		}
	}
	return 0;
}

TElem getElemOnPos(DynamicArray* arr, int idx)
{
	if (arr == NULL || arr->elems == NULL)
		return NULL;
	return arr->elems[idx];
}

int getSize(DynamicArray* da)
{
	return da->size;
}

void updateElem(DynamicArray* da, char* name, TElem elem)
{
	if (da == NULL)
		return;
	if (da->elems == NULL)
		return;
	for (int i = 0; i < da->size - 1; i++)
	{
		Product* p = (Product*)da->elems[i];
		if (strcmp(p->name, name) == 0)
		{
			da->elems[i] = elem;
		}
	}
}