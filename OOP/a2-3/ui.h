#pragma once
#include "service.h"

//typedef void (*SortFunction)(Service*, DynamicArray*);

typedef struct {
	Service service;
} UI;

UI createUI(Service s);

void menu();
void addUi(Service *serv);
void deleteUi(Service* serv);
void updateQuantityUi(Service* serv);
void updateExpirationUi(Service* serv);

void printRepo(DynamicArray* da);

void undoUI(Service* serv);
void redoUI(Service* serv);

void expirationSoon(Service* serv);

void filter(Service* serv);

void sortUI(Service* serv);
