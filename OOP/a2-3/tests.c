#include "tests.h"
#include "domain.h"
#include <assert.h>
#include <string.h>
#include "repository.h"
#include "service.h"
#include <stdlib.h>

void test_createProduct()
{
	Date d = { 12, 12, 2022 };
	Product p = createProduct("milk", "dairy", 5, d);
	assert(strcmp(p.name, "milk") == 0);
	assert(strcmp(p.category, "dairy") == 0);
	assert(p.quantity == 5);
	assert(p.expiration.day == 12);
	assert(p.expiration.month == 12);
	assert(p.expiration.year == 2022);
}

void test_repo()
{
	Repo* repo = createRepo(5);
	assert(repo->products->size == 0);
	Date d = { 12, 12, 2022 };
	Product p = createProduct("milk", "dairy", 5, d);
	addProduct(repo, p);
	assert(repo->products->size == 1);
	Product p2 = createProduct("milk", "dairy", 5, d);
	assert(addProduct(repo, p2) == 0);

	Product* storedProduct = (Product*)repo->products->elems[0];
	assert(storedProduct->quantity == 10);

	updateQuantity(repo, "milk", "dairy", 5);
	Product* storedProduct2 = (Product*)repo->products->elems[0];
	assert(storedProduct2->quantity == 5);

	Product p3 = createProduct("cheese", "dairy", 5, d);
	addProduct(repo, p3);

	assert(deleteProduct(repo, "milk", "dairy") == 1);
	destroy(repo);
}

void test_service()
{
	Repo* repo = createRepo(5);
	UndoRedo* undoredo = createUndoRedo();
	Service serv = createService(repo, undoredo);
	Date d = { 12, 12, 2022 };

	Product p = createProduct("milk", "dairy", 5, d);
	Product p2 = createProduct("cheese", "dairy", 5, d);
	addService(&serv, p);
	addService(&serv, p2);
	assert(serv.repo->products->size == 2);

	Product* filtered1 = (Product*)malloc(sizeof(Product) * getServiceSize(&serv));
	int size_filtered = filterByName(&serv, "milk", filtered1);
	assert(size_filtered == 1);

	Product* filtered2 = (Product*)malloc(sizeof(Product) * getServiceSize(&serv));
	size_filtered = filterByCategory(&serv, "dairy", filtered2);
	assert(size_filtered == 2);

	free(filtered1);
	free(filtered2);

	undoService(&serv);
	assert(serv.repo->products->size == 1);

	redoService(&serv);
	assert(getServiceSize(&serv) == 2);

	assert(redoService(&serv) == 0);
	

	Product p3 = createProduct("icecream", "dairy", 5, d);
	addService(&serv, p3);
	DynamicArray* sorted = createDynamicArray(getServiceSize(&serv));
	sortName(&serv, sorted);


	Product* product = (Product*)sorted->elems[0];
	assert(strcmp(product->name, "milk")== 0);

	product= (Product*)sorted->elems[1];
	assert(strcmp(product->name, "icecream")== 0);

	product = (Product*)sorted->elems[2];
	assert(strcmp(product->name, "cheese")== 0);

	destroyArray(sorted);
	destroy(repo);
	destroyUndoRedo(serv.undoredo);
}

void all_tests()
{
	test_createProduct();
	test_repo();
	test_service();
}
