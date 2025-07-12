#include "UserService.h"

UserService::UserService(Repository* repo)
{
	this->repo = repo;
}

bool UserService::addToList(Dog d)
{
	for (int i = 0; i < this->getListSize();i++)
		if (this->adoptionList.getElem(i).getName() == d.getName())
			return false;
	this->adoptionList.addElem(d);
	return true;
}

DynamicVector<Dog> UserService::getAdoptionList()
{
	return this->adoptionList;
}

DynamicVector<Dog> UserService::filterDogs(std::string breed, int age)
{
	DynamicVector<Dog> filtered;
	for (int i = 0; i < this->repo->lengthRepo(); i++)
	{
		Dog d = this->repo->getDog(i);
		if ((breed == "" || d.getBreed() == breed) && (d.getAge() <= age))
			filtered.addElem(d);
	}
	return filtered;
}

