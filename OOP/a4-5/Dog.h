#pragma once
#include <string>

class Dog
{
private:

	std::string breed;
	std::string name;
	int age;
	std::string link;

public:
	Dog();
	Dog(std::string breed, std::string name, int age, std::string link);

	std::string getBreed();
	std::string getName();
	int getAge();
	std::string getLink();

	void setBreed(std::string newbreed);
	void setAge(int newage);
	void setLink(std::string newlink);

	bool operator==(const Dog& dog);
	Dog& operator=(const Dog& dog)
	{
		this->breed = dog.breed;
		this->name = dog.name;
		this->age = dog.age;
		this->link = dog.link;
		return *this;
	}
	std::string str();
};


