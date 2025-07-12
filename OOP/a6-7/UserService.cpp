#include "UserService.h"
#include <algorithm>
#include <iterator>
UserService::UserService(Repository* repo, AdoptionList* adList)
{
	this->repo = repo;
	this->adoptionList = adList;
}

bool UserService::addToList(Dog d)
{
	for (int i = 0; i < this->getListSize();i++)
		if (this->adoptionList->getDog(i).getName() == d.getName())
			return false;
	this->adoptionList->addDog(d);
	return true;
}

std::vector<Dog> UserService::getAdoptionList()
{
	return this->adoptionList->getDogs();
}

std::vector<Dog> UserService::filterDogs(std::string breed, int age)
{
	std::vector<Dog> filtered;
	std::vector<Dog> dogs;
	for (int i = 0; i < this->repo->lengthRepo(); i++)
	{
		dogs.push_back(this->repo->getDog(i));
	}

	std::copy_if(dogs.begin(), dogs.end(), std::back_inserter(filtered), [&breed, age](Dog d) {
		return (breed == "" || d.getBreed() == breed) && (d.getAge() <= age);
		});
	/*
	std::vector<Dog> filtered;
	for (int i = 0; i < this->repo->lengthRepo(); i++)
	{
		Dog d = this->repo->getDog(i);
		if ((breed == "" || d.getBreed() == breed) && (d.getAge() <= age))
			filtered.push_back(d);
	}
	*/
	return filtered;
}
