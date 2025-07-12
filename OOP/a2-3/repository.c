#include "repository.h"
#include "domain.h"
#include <stdlib.h>
#include <string.h>
#include <time.h>

Repo* createRepo(int cap)
{
	Repo* repo=(Repo*) malloc(sizeof(Repo));
	if (repo == NULL)
		return NULL;

	repo->products=createDynamicArray(cap);
	if (repo->products == NULL)
	{
		free(repo);
		return NULL;
	}
	return repo;
}

void destroy(Repo* repo)
{
	if (repo == NULL || repo->products == NULL) return;
	for (int i = 0; i < repo->products->size; i++)
		free(repo->products->elems[i]);
	destroyArray(repo->products);
	free(repo);
}

int addProduct(Repo* repo, Product p)
{
	int ok = 1;
	for (int i = 0; i < repo->products->size; i++)
	{
		Product* currentProduct = (Product*)repo->products->elems[i];
		if (strcmp(currentProduct->name, p.name) == 0 && strcmp(currentProduct->category, p.category) == 0)
		{
			ok = 0;
			currentProduct->quantity += p.quantity;
			return 0;
		}
	}
	if (ok == 1)
	{
		Product* newProduct = (Product*)malloc(sizeof(Product));
		if (newProduct == NULL)
			return 0;
		*newProduct = p;
		addElem(repo->products, newProduct);
		return 1;
	}	
}

int deleteProduct(Repo* repo, char* name, char* category)
{
	return deleteElem(repo->products, name, category);
	
}

int updateQuantity(Repo* repo, char* name, char* category, int new_quantity)
{
	for (int i = 0; i < repo->products->size; i++)
	{
		Product* currentProduct = (Product*)repo->products->elems[i];
		if (strcmp(currentProduct->name, name) == 0 && strcmp(currentProduct->category, category) == 0)
		{
			currentProduct->quantity = new_quantity;
			return 1;
		}
	}
	return 0;
}

int updateExpiration(Repo* repo, char* name, char* category, Date new_expiration)
{
	for (int i = 0; i < repo->products->size; i++)
	{
		Product* currentProduct = (Product*)repo->products->elems[i];
		if (strcmp(currentProduct->name, name) == 0 && strcmp(currentProduct->category, category) == 0)
		{
			currentProduct->expiration = new_expiration;
			return 1;
		}
	}
	return 0;
}

Repo* getRepo(Repo* repo)
{
	return repo;
}

void generate_products(Repo* repo)
{
	char dairy[6][20] = { "milk","cheese","yogurt","butter","cream", "fruit yogurt"};
	char sweets[5][20] = { "chocolate","candy","cake","biscuits","icecream" };
	char meat[5][20] = { "beef","pork","chicken","turkey","duck" };
	char fruit[5][20] = { "apple","banana","orange","grape","kiwi"};
	char category_options[5][20] = { "dairy","sweets","meat","fruit" };
	int cnt = 0;
	while (cnt < 10) {
		char name[20];
		char category[20];
		
		strcpy(category, category_options[rand()%4]);
		if (strcmp(category, "dairy") == 0)
			strcpy(name, dairy[rand() % 6]);
		if (strcmp(category, "sweets") == 0)
			strcpy(name, sweets[rand() % 5]);
		if (strcmp(category, "meat") == 0)
			strcpy(name, meat[rand() % 5]);
		if (strcmp(category, "fruit") == 0)
			strcpy(name, fruit[rand() % 5]);
		int quantity = rand() % 10+1; 
		Date expiration = generateRandomFutureDate(400);
		Product p = createProduct(name, category, quantity, expiration);

		int ok = 1;
		for (int i = 0;i < repo->products->size;i++)
		{
			Product* currentProduct = (Product*)repo->products->elems[i];
			if (strcmp(currentProduct->name, p.name) == 0 && strcmp(currentProduct->category, p.category) == 0)
				ok = 0;
		}
		if (ok == 1)
		{
			Product* newProduct = (Product*)malloc(sizeof(Product));
			*newProduct = p;
			addElem(repo->products, newProduct);
			cnt++;
		}
	}
}

Product findProduct(Repo* repo, char* name, char* category)
{
	for (int i = 0; i < repo->products->size; i++)
	{
		Product* currentProduct = (Product*)repo->products->elems[i];
		if (strcmp(currentProduct->name, name) == 0 && strcmp(currentProduct->category, category) == 0)
			return *currentProduct;
	}
}

Date generateRandomFutureDate(int maxDays)
{
	time_t t = time(NULL);
	struct tm current_time;
	localtime_s(&current_time, &t);

	// Generate a random number of days to add
	int daysToAdd = rand() % maxDays + 1;

	// Add the random number of days to the current date
	current_time.tm_mday += daysToAdd;
	mktime(&current_time); // Normalize the time structure

	Date futureDate;
	futureDate.day = current_time.tm_mday;
	futureDate.month = current_time.tm_mon + 1;
	futureDate.year = current_time.tm_year + 1900;

	return futureDate;
}

Repo* copyRepo(Repo* repo)
{
	Repo* newRepo = createRepo(repo->products->cap);
	if (newRepo == NULL)
		return NULL;
	for (int i = 0; i < repo->products->size;i++)
		addElem(newRepo->products, repo->products->elems[i]);
	return newRepo;
}

TElem getElemRepo(Repo* repo, int inx)
{
	return getElemOnPos(repo->products, inx);
}

int getRepoSize(Repo* repo)
{
	return repo->products->size;
}
