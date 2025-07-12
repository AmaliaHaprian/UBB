#include <stdio.h>
#include "domain.h"

Product createProduct(char* name, char* category, int quantity, Date expiration)
{
	Product p;
	strcpy(p.name, name);
	strcpy(p.category, category);
	p.name[sizeof(p.name) - 1] = '\0';
	p.category[sizeof(p.category) - 1] = '\0';
	p.quantity = quantity;
	p.expiration = expiration;
	return p;
}

char getName(Product p)
{
	return p.name ;
}

char getCategory(Product p)
{
	return p.category;
}

int getQuantity(Product p)
{
	return p.quantity;
}

Date getExpiration(Product p)
{
	return p.expiration;
}

void setName(Product *p, char name)
{   
	strcpy(p->name, name);
}

void setCategory(Product *p, char category)
{
	strcpy(p->category, category);

}

void setQuantity(Product* p, int quantity)
{
	p->quantity = quantity;
}

void setExpiration(Product* p, Date expiration)
{
	p->expiration = expiration;
}

void str(Product p)
{
	printf("Name: %s, Category: %s, Quantity: %d, Expiration: %d/%d/%d \n", p.name, p.category, p.quantity, p.expiration.day, p.expiration.month, p.expiration.year);
}
