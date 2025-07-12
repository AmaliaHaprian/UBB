#pragma once
#include <stdio.h>

typedef struct {
	int month;
	int day;
	int year;
} Date;

typedef struct {
	char name[20];
	char category[20];
	int quantity;
	Date expiration;

} Product;

Product createProduct(char* name, char* category, int quantity, Date expiration);


// Getters
char getName(Product p);
char getCategory(Product p);
int getQuantity(Product p);
Date getExpiration(Product p);

// Setters
void setName(Product* p, char name);
void setCategory(Product* p, char category);
void setQuantity(Product* p, int quantity);
void setExpiration(Product* p, Date expiration);

void str(Product p);