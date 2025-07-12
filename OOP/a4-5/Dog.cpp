#include "Dog.h"
#include <cstring>
#include <iostream>

Dog::Dog()
{
}

Dog::Dog(std::string breed, std::string name, int age, std::string link)
{
	this->breed = breed;
	this->name = name;
	this->age = age;
	this->link = link;
}

std::string Dog::getBreed()
{
	return this->breed;
}

std::string Dog::getName()
{
	return this->name;
}

int Dog::getAge()
{
	return this->age;
}

std::string Dog::getLink()
{
	return this->link;
}

void Dog::setBreed(std::string newbreed)
{
	this->breed = newbreed;
}

void Dog::setAge(int newage)
{
	this->age = newage;
}

void Dog::setLink(std::string newlink)
{
	this->link = newlink;
}

bool Dog::operator==(const Dog& dog)
{
	if (this->age == dog.age && this->name == dog.name && this->breed == dog.breed && this->link == dog.link)
		return true;
	return false;
}

std::string Dog::str()
{
	std::string str = "";
	str = str + "Name: " + this->getName() + "; Breed: " + this->getBreed() + "; Age: " + std::to_string(this->getAge()) + "; Link: " + this->getLink();
	//	std::cout << "Name: " << this->getName() << "; Breed: " << this->getBreed() << "; Age: " << this->getAge() << "; Link: " << this->getLink() << " \n";
	return str;
}
