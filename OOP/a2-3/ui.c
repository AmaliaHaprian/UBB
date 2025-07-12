#include "ui.h"
#include <stdio.h>
#include <stdlib.h>
#include "service.h"
#include "validator.h"
#include <string.h>
#include "dynamicarray.h"

UI createUI(Service serv)
{
	UI ui;
	ui.service = serv;
	return ui;
}

void menu()
{
	printf("\n");
	printf("  -----Menu----- \n");
	printf("  1. Add product\n");
	printf("  2. Delete product\n");
	printf("  3. Update product quantity\n");
	printf("  4. Update product expiration date\n");
	printf("  5. Filter products\n");
	printf("  6. Undo Last Operation\n");
	printf("  7. Redo Last Operation\n");
	printf("  8. Display products that expire soon\n");
	printf("  9. Sort\n");
	printf("\n");
}

char* categoryUI() {
	int ok = 0;
	while (ok == 0) {
		printf("Category (dairy /sweets /meat/ fruit): ");
		char category[20];
		scanf("%s", category);
		if (validate_category(category) == 1)
		{ok = 1;
		return category;
		}
		else
		{
			printf("Invalid category!\n");
			return categoryUI();
		}
	}
}

Date dateUI() {
	int ok = 0;
	while (ok == 0)
	{
		printf("Expiration date: ");
		Date date;
		scanf("%d %d %d", &date.day, &date.month, &date.year);
		if (validate_date(date) == 1)
		{
			ok = 1;
			return date;
		}
		else {
			printf("Invalid date!\n");
			return dateUI();
		}
	}
}

void addUi(Service *serv)
{
	char name[20];
	char category[20];
	int quantity;
	Date expiration;

	printf("Name: ");
	scanf(" %[^\n]", name);
	
	strcpy(category, categoryUI());
	
	printf("Quantity: ");
	scanf("%d", &quantity);

	expiration = dateUI();
	printf("\n");

	Product p = createProduct(name, category, quantity, expiration);
	int res= addService(serv, p);
	if (res == 0)
		printf("Product already exists! Quantity updated\n");
	else
		printf("Product added successfully!\n");
}

void deleteUi(Service* serv)
{
	char name[20],category[20];
	printf("Name of product you want to delete: ");
	scanf(" %[^\n]", name);
	printf("Category of product you want to delete: ");
	scanf("%s", category);
	printf("\n");

	int res=deleteService(serv, name, category);
	if (res == 0)
		printf("Product not found!\n");
	else
		printf("Product deleted successfully!\n");
}

void updateQuantityUi(Service* serv)
{
	char name[20], category[20];
	int quantity;
	printf("Name of product you want to update: ");
	scanf(" %[^\n]", name);
	printf("Category of product you want to update: ");
	scanf("%s", category);
	printf("New quantity: ");
	scanf("%d", &quantity);
	printf("\n");
	int res = updateQuantityService(serv, name, category, quantity);
	if (res == 0)
		printf("Product not found!\n");
	else
		printf("Product updated successfully!\n");
}

void updateExpirationUi(Service* serv)
{
	char name[20], category[20];
	Date expiration;

	printf("Name of product you want to update: ");
	scanf(" %[^\n]", name);

	printf("Category of product you want to update: ");
	scanf("%s", category);

	printf("New expiration date: ");
	expiration = dateUI();

	printf("\n");
	int res = updateExpirationService(serv, name, category, expiration);
	if (res == 0)
		printf("Product not found!\n");
	else
		printf("Product updated successfully!\n");
}

void printRepo(DynamicArray* da)
{
	printf("Products: \n");
	for (int i = 0;i < da->size;i++)
	{
		Product* product = (Product*)da->elems[i];
		str(*product);
	}
}

void option_error()
{
	printf("Invalid option!\n");
}


void undoUI(Service* serv)
{
	int res;	
	res = undoService(serv);
	if (res == 0)
		printf("\nNo more operations to undo!\n");
	else
		printf("\nUndo successful!\n");
}

void redoUI(Service* serv)
{
	int res;
	res = redoService(serv);
	if (res == 0)
		printf("\nNo more operations to redo!\n");
	else
		printf("\nRedo successful!\n");
}
void expirationSoon(Service* serv)
{
	int days;
	printf("Enter number of days: ");
	scanf("%d", &days);

	//char* category = categoryUI();
	char category[20];
	printf("Enter category: ");
	while (getchar() != '\n');
	fgets(category, sizeof(category), stdin);
	category[strcspn(category, "\n")] = 0;
	
		Product* filtered = (Product*)malloc(sizeof(Product) * getServiceSize(serv));
		if (filtered == NULL)
		{
			printf("Memory allocation failed!\n");
			return;
		}
		int size_filtered = expirationService(serv, days, category, filtered);
		if (size_filtered == 0)
			printf("No products found!\n");
		else
		{
			printf("Filtered products: \n");
			for (int i = 0; i < size_filtered; i++)
				str(filtered[i]);
		}
		free(filtered);
}

void filter(Service* serv)
{
	char command[20];
	char string[20];
	printf("What do you want to filter the products by?");
	scanf("%s", command);

	Product* filtered = (Product*)malloc(sizeof(Product) * getServiceSize(serv));
	int size_filtered;

	if (filtered == NULL)
	{
		printf("Memory allocation failed!\n");
		return;
	}

	if (strcmp(command, "name") == 0)
	{
		printf("Enter string: ");
		while (getchar() != '\n');
		fgets(string, sizeof(string), stdin);
		string[strcspn(string, "\n")] = 0;
		size_filtered = filterService(serv, string, filtered, filterByName);
	}
	else if (strcmp(command, "category") == 0)
	{
		printf("Enter category: ");
		while (getchar() != '\n');
		fgets(string, sizeof(string), stdin);
		string[strcspn(string, "\n")] = 0;
		size_filtered = filterService(serv, string, filtered, filterByCategory);
	}
	if (size_filtered == 0)
		printf("No products found!\n");
	else
	{
		printf("Filtered products: \n");
		for (int i = 0; i < size_filtered; i++)
			str(filtered[i]);
	}
	free(filtered);
}

void sortUI(Service* serv)
{
	char command[20];
	printf("What do you want to sort the products by? Name/category: ");
	scanf("%s", command);
	DynamicArray* filtered = createDynamicArray(getServiceSize(serv));
	if (filtered == NULL)
	{
		printf("Memory allocation failed!\n");
		return;
	}
	if (strcmp(command, "name") == 0)
		sortService(serv, &sortName, filtered);
	else if (strcmp(command, "category") == 0)
		sortService(serv, &sortCategory, filtered);

	for (int i = 0; i < getServiceSize(serv);i++)
	{
		Product* product = getElemOnPos(filtered, i);
		str(*product);
	}
	destroyArray(filtered);
}
