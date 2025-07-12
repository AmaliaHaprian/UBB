#pragma once
#include "Repository.h"
#include "DynamicVector.h"
#include "Dog.h"
#include <string>

class UserService
{
private:
	Repository* repo;
	DynamicVector<Dog> adoptionList;

public:
	UserService(Repository* repo);
	bool addToList(Dog d);
	DynamicVector<Dog> getAdoptionList();
	DynamicVector<Dog> filterDogs(std::string breed, int age);
	~UserService() {
		// Destructor
	};
	int getListSize() {
		return this->adoptionList.length();
	}
};

