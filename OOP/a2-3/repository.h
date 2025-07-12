#pragma once
#include "domain.h"
#include "dynamicarray.h"

typedef struct {
	DynamicArray* products;
}Repo;

/*
Creates a pointer to an object on type Repository
Input: an integer cap, meaning the maximum capacity of the repository
Output: returns a pointer to a Repo structure
*/
Repo* createRepo(int cap);

/*
* Destroys a repository, freeing the memory allocated for it
* Input: a pointer to a Repo structure
* Output: -
*/
void destroy(Repo* repo);

/*
* Adds a product to the repository
* Input: a pointer to a Repo structure and a Product structure
* Output: 1 if the product was added successfully, 0 if the product already exists in the repository
*/
int addProduct(Repo* repo, Product p);

/*
* Deletes a product from the repository
* Input: a pointer to a Repo structure, a string name and a string category
* Output: 1 if the product was deleted successfully, 0 if the product was not found
*/
int deleteProduct(Repo* repo, char* name, char* category);

/*
* Updates the quantity of a product in the repository
* Input: a pointer to a Repo structure, a string name and a string category, an integer new_quantity
* Output: 1 if the product was updated successfully, 0 if the product was not found
*/
int updateQuantity(Repo* repo, char* name, char* category, int new_quantity);

/*
* Updates the expiration date of a product in the repository
* Input: a pointer to a Repo structure, a string name and a string category, a Date new_expiration
* Output: 1 if the product was updated successfully, 0 if the product was not found
*/
int updateExpiration(Repo* repo, char* name, char* category, Date new_expiration);

/*
* Returns a pointer to a Repo structure
* Input: a pointer to a Repo structure
* Output: a pointer to a Repo structure
*/
Repo* getRepo(Repo* repo);

/*
* Generates a list of products
* Input: a pointer to a Repo structure
* Output: -
*/
void generate_products(Repo* repo);

/*
* Finds a product through it's unique identifiers: name and category
* Input: a pointer to a Repo structure, 2 pointers to char, representing the name and category
* Output: the desired variable of type Product
*/
Product findProduct(Repo* repo, char* name, char* category);

/*
* Generates a random date in the future
* Input: the number of maximum days in the future
* Output: a random variable of type Date
*/
Date generateRandomFutureDate(int maxDays);

/*
* Generates a deep copy of the repo
* Input: a pointer to a Repo structure
* Output: a new Repo structure, with the same attributes as the copied one
*/
Repo* copyRepo(Repo* repo);

TElem getElemRepo(Repo* repo, int inx);

int getRepoSize(Repo* repo);



