#pragma once
#include "repository.h"
#include "undoredo.h"

typedef struct {
	Repo* repo;
	UndoRedo* undoredo;
}Service;

typedef void (*SortFunction)(Service*, DynamicArray*);

/*
* Creates a structure of type service
* Input: a pointer to a Repo structure
* Output: a Service structure
*/
Service createService(Repo* repo, UndoRedo* undoredo);

/*
* Adds a product to the repository
* Input: a pointer to a Service structure and a Product structure
* Output: 1 if the product was added successfully, 0 if the product already exists in the repository
*/
int addService(Service* serv, Product p);

/*
* Deletes a product from the repository
* Input: a pointer to a Service structure, a string name and a string category
* Output: 1 if the product was deleted successfully, 0 if the product was not found
*/
int deleteService(Service* serv, char* name, char* category);

/*
* Updates the quantity of a product in the repository
* Input: a pointer to a Service structure, a string name and a string category, an integer new_quantity
* Output: 1 if the product was updated successfully, 0 if the product was not found
*/
int updateQuantityService(Service* serv, char* name, char* category, int new_quantity);

/*
* Updates the expiration date of a product in the repository
* Input: a pointer to a Service structure, a string name and a string category, a Date new_expiration
* Output: 1 if the product was updated successfully, 0 if the product was not found
*/
int updateExpirationService(Service* serv, char* name, char* category, Date new_expiration);

/*
* Returns a pointer to a Repo structure
* Input: a pointer to a Service structure
* Output: a pointer to a Repo structure, 
*/
Repo* getRepoService(Service* serv);

/*
* Undoes the last operation
* Input: a pointer to a Service structure
* Output: 1 if the operation was undone successfully, 0 if there are no more operations to undo
*/
int undoService(Service* serv);

/*
* Redoes the last operation
* Input: a pointer to a Service structure
* Output: 1 if the operation was redone successfully, 0 if there are no more operations to redo
*/
int redoService(Service* serv);


/*
* Filters the products from a given category that have the expiration date in less days than the number provided
* Input: a pointer to a Service structure, an integer provided by the user representing thr number of days, a char pointer
* representing the category and a pointer to an array with elements of type Product
* Output: an integer, representing the size of filtered array
*/
int expirationService(Service* serv, int days, char* category, Product* filtered);


/*
* A general filtering function
* Input: a pointer to a Service structure, a pointer to char representing the type of filtering, a pointer to an array
* with elements of type Product and a pointer to the function that does the actual filtering
* Output: an integer, representing the size of filtered array
*/
int filterService(Service* serv, char* string, Product* filtered, int (*op)(Service*, char*, Product* filtered));

/*
* Filters the products by name
* Input: a pointer to a Service structure, a string name and a pointer to a Product structure
* Output: the number of products that have the name in their name
*/
int filterByName(Service* serv, char* name, Product* filtered);

/*
* Filters the products by category
* Input: a pointer to a Service structure, a string category and a pointer to a Product structure
* Output: the number of products that have the category in their category
*/
int filterByCategory(Service* serv, char* category, Product* filtered);


/*
* Sorts the array descendingly by name
* Input: a pointer to a Service structure and a pointer to a dynamic array that will hold the sorted list
* Output: -
*/
void sortName(Service* serv, DynamicArray* sorted);

/*
* Sorts the array descendingly by category
* Input: a pointer to a Service structure and a pointer to a dynamic array that will hold the sorted list
* Output: -
*/
void sortCategory(Service* serv, DynamicArray* sorted);

/*
* The general sorting function
* Input: a pointer to a Service structure, a pointer to the according sorting function, defined through a new variable type
* and a pointer to a dynamic array that will hold the sorted list
*/
void sortService(Service* serv, SortFunction sortf, DynamicArray* sorted);

int getServiceSize(Service* serv);
