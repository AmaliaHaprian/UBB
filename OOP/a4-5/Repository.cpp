#include "Repository.h"
#include <stdexcept>

int Repository::searchRepo(std::string name)
{
	for (int i = 0; i < this->arr.length(); i++)
	{
		Dog d = this->arr.getElem(i);
		if (d.getName() == name)
			return i;
	}
	return -1;

}

bool Repository::removeRepo(std::string name)
{
	int pos = this->searchRepo(name);
	if (pos != -1)
	{
		Dog d = this->arr.getElem(pos);
		this->arr.deleteElem(d);
		return true;
	}
	return false;
}

Repository Repository::getRepo()
{

	return *this;
}

int Repository::lengthRepo()
{
	return this->arr.length();
}

Dog Repository::getDog(int pos)
{
	return this->arr.getElem(pos);
}

void Repository::updateRepo(Dog old, Dog newdog)
{
	this->arr.updateElem(old, newdog);
}

bool Repository::addRepo(Dog d)
{
	for (int i = 0; i < this->lengthRepo();i++)
	{

		if (this->arr.getElem(i).getName() == d.getName())
			return false;
	}
	this->arr.addElem(d);
}
