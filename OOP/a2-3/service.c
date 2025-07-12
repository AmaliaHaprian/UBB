#include "service.h"
#include "validator.h"
#include "undoredo.h"
#include <string.h>
#include <time.h>

Service createService(Repo* repo, UndoRedo* undoredo)
{
	Service serv;
	serv.repo = repo;
	serv.undoredo = undoredo;
	return serv;
}

int addService(Service* serv, Product p)
{
	Operation* redo_operation = createOperation(p, "add");
	Operation* undo_operation = createOperation(p, "delete");
	recordOperation(serv->undoredo, undo_operation, redo_operation);

	return addProduct(getRepoService(serv), p);
}

int deleteService(Service* serv, char* name, char* category)
{
	Operation* redo_operation = createOperation(findProduct(serv->repo, name, category), "delete");
	Operation* undo_operation = createOperation(findProduct(serv->repo, name, category), "add");
	recordOperation(serv->undoredo, undo_operation, redo_operation);

	return deleteProduct(getRepoService(serv), name, category);
}

int updateQuantityService(Service* serv, char* name, char* category, int new_quantity)
{
	Product old = findProduct(serv->repo, name, category);
	Product newProduct = createProduct(name, category, new_quantity, getExpiration(old));
	Operation* redo_operation = createOperation(newProduct, "update");
	Operation* undo_operation = createOperation(old, "update");
	recordOperation(serv->undoredo, undo_operation, redo_operation);

	return updateQuantity(serv->repo, name, category, new_quantity);
}

int updateExpirationService(Service* serv, char* name, char* category, Date new_expiration)
{
	Product old = findProduct(serv->repo, name, category);
	Product newProduct = createProduct(name, category, getQuantity(old), new_expiration);
	Operation* redo_operation = createOperation(newProduct, "update");
	Operation* undo_operation = createOperation(old, "update");
	recordOperation(serv->undoredo, undo_operation, redo_operation);

	return updateExpiration(serv->repo, name, category, new_expiration);
}

int filterByName(Service* serv, char* name, Product* filtered)
{
	
	int size_filtered = 0;
	for (int i = 0; i < getRepoSize(serv->repo); i++)
	{
		{
			Product* product = (Product*)getElemRepo(serv->repo, i);
			if (strstr(product->name, name) != NULL || (strcmp(name, "") == 0))
			{
				filtered[size_filtered++] = *product;
			}
		}
	}

	for(int i=0; i<size_filtered-1; i++)
		for (int j = 0; j < size_filtered - i - 1;j++)
		{
			Product productA = filtered[j];
			Product productB = filtered[j + 1];
			if (productA.quantity>productB.quantity)
			{
				Product temp = filtered[j];
				filtered[j] = filtered[j + 1];
				filtered[j + 1] = temp;
			}
		}
	return size_filtered;
}

int filterByCategory(Service* serv, char* category, Product* filtered)
{
	int size_filtered = 0;
	for (int i = 0; i < getRepoSize(serv->repo); i++)
	{
		Product* product = (Product*)getElemRepo(serv->repo, i);
		if (strcmp(product->category, category ) == 0 || (strcmp(category, "") == 0))
		{
			filtered[size_filtered++] = *product;
		}
	}
	return size_filtered;
}

void sortName(Service* serv, DynamicArray* sorted)
{
	int n = getRepoSize(serv->repo);
	for (int i = 0; i < n; i++)
		addElem(sorted, getElemRepo(serv->repo, i));

	for (int i = 0; i < n - 1; i++)
	{
		for (int j = 0; j < n - i - 1; j++)
		{
			Product* productA = (Product*)getElemOnPos(sorted, j);
			Product* productB = (Product*)getElemOnPos(sorted, j+1);
			if (strcmp(productA->name, productB->name) < 0)
			{
				Product* temp = getElemOnPos(sorted, j);
				sorted->elems[j] = getElemOnPos(sorted, j+1);
				sorted->elems[j + 1] = temp;
			}
		}
	}
}

void sortCategory(Service* serv, DynamicArray* sorted)
{
	int n = getRepoSize(serv->repo);
	for (int i = 0; i < n; i++)
		addElem(sorted, getElemRepo(serv->repo, i));

	for (int i = 0; i < n - 1; i++)
	{
		for (int j = 0; j < n - i - 1; j++)
		{
			Product* productA = (Product*)getElemOnPos(sorted, j);
			Product* productB = (Product*)getElemOnPos(sorted, j+1);
			if (strcmp(productA->category, productB->category) < 0)
			{
				Product* temp = getElemOnPos(sorted,j);
				sorted->elems[j] = getElemOnPos(sorted, j+1);
				sorted->elems[j + 1] = temp;
			}
		}
	}
}

void sortService(Service* serv, SortFunction sortf, DynamicArray* sorted)
{
	sortf(serv, sorted);
}

int getServiceSize(Service* serv)
{
	return getRepoSize(serv->repo);
}

Repo* getRepoService(Service* serv)
{
	return getRepo(serv->repo);
}

int undoService(Service* serv)
{
	return undo(serv->undoredo, serv->repo);
}

int redoService(Service* serv)
{
	return redo(serv->undoredo, serv->repo);
}

int expirationService(Service* serv, int days, char* category, Product* filtered)
{
	time_t t = time(NULL);
	struct tm current_time;
	localtime_s(&current_time, &t);
	int size_filtered = 0;

	for (int i = 0; i < getRepoSize(serv->repo); i++)
	{
		Product* product = (Product*)getElemRepo(serv->repo, i);

		struct tm expiration_time = {0};
		expiration_time.tm_year = product->expiration.year - 1900;
		expiration_time.tm_mon = product->expiration.month - 1;
		expiration_time.tm_mday = product->expiration.day;
		time_t expiration = mktime(&expiration_time);
		double seconds_diff = difftime(expiration, t);
		int days_diff = (int)(seconds_diff / (60 * 60 * 24));

		if (days_diff < days && ((strcmp(product->category, category) == 0) || (strcmp(category, "") == 0)))
		{
			filtered[size_filtered++] = *product;
		}
	}
	return size_filtered;
}

int filterService(Service* serv, char* string, Product* filtered, int(*op)(Service*, char*, Product* filtered))
{
	int size_filtered = op(serv, string, filtered);
	return size_filtered;
}



