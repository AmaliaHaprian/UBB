#include "Ui.h"
#include <iostream>
#include <string>
#include <utility>
#include <windows.h>
#include <cstdlib>
#include <chrono>
#include <thread>
#include "ValidationException.h"
using namespace std;

void waitForSeconds(int seconds) {
	std::this_thread::sleep_for(std::chrono::seconds(seconds));
}

Ui::Ui(Service* serv, UserService* userserv)
{
	this->serv = serv;
	this->userserv = userserv;
}

void Ui::addUi()
{
	/*
	std::string breed, name, link;
	int age;

	std::cout << "Enter name: ";
	std::cin >> name;

	std::cin.ignore();
	std::cout << "Enter breed: ";
	std::getline(std::cin, breed);

	std::cout << "Enter age: ";
	std::cin >> age;

	std::cout << "Enter link: ";
	std::cin >> link;


	try
	{
		this->serv->addService(breed, name, age, link);
		std::cout << "Dog added successfully\n";
	}
	catch (const std::exception& e)
	{
		std::cout << "Dog already in the shelter\n";
	}
	*/

	Dog d{};
	cout << "Enter dog information (name, breed, age, link): "<<std::endl;
	std::cin.ignore();
	cin >> d;
	
	try {
		DogValidator::validate(d);
	}
	catch (ValidationException& ex)
	{
		std::cout << ex.getMessage() << std::endl;
		return;
	}
	
	try
	{
		this->serv->addService(d.getBreed(), d.getName(), d.getAge(), d.getLink());
		std::cout << "Dog added successfully\n";
	}
	catch (ValidationException& ex)
	{
		std::cout << ex.getMessage()<<std::endl;
	}
}

void Ui::menu()
{
	std::cout << "\n";
	std::cout << "     -----ADMIN MENU-----\n";
	std::cout << "        1. Add dog\n";
	std::cout << "        2. Remove dog\n";
	std::cout << "        3. Update information\n";
	std::cout << "        4. See all dogs\n";
	std::cout << "        5. Exit\n";
}

void Ui::removeUi()
{
	std::string name;
	std::cout << "Enter name of dog you want to adopt: ";
	std::cin.ignore();
	std::getline(std::cin, name);
	try {
		DogValidator::validateString(name);
	}
	catch (ValidationException& ex)
	{
		std::cout << ex.getMessage() << std::endl;
		return;
	}
	std::cout << "\n";

	try
	{
		this->serv->removeService(name);
		std::cout << "Dog removed from the shelter\n";
	}
	catch (ValidationException& ex)
	{
		std::cout << ex.getMessage()<<std::endl;
	}
}

void Ui::printRepo()
{
	std::cout << "Dogs:\n";

	for (auto dog : this->serv->getDogs())
	{
		//std::cout << dog.str() << std::endl;
		std::cout << dog<<std::endl;
	}

	/*
	for (int i = 0; i < this->serv->getSize();i++)
	{
		Dog d = this->serv->getDog(i);
		std::cout<<d.str() << std::endl;
	}
	*/
}

void Ui::updateUi()
{
	int command;
	std::string name, newstring, newage;
	bool res;

	std::cout << "Enter name of dog: ";
	std::cin.ignore();
	std::getline(std::cin, name);

	try {
		DogValidator::validateString(name);
	}
	catch (ValidationException& ex)
	{
		std::cout << ex.getMessage() << std::endl;
		return;
	}

	std::cout << "\n1. Change breed\n";
	std::cout << "2. Change age\n";
	std::cout << "3. Change link\n";
	std::cout << ">>";
	std::cin >> command;

	if (command == 1 || command == 3)
	{
		std::cout << "Enter new string: ";
		std::cin.ignore();
		std::getline(std::cin, newstring);
		try {
			DogValidator::validateString(newstring);
		}
		catch (ValidationException& ex)
		{
			std::cout << ex.getMessage() << std::endl;
			return;
		}
		res = this->serv->updateService(name, command, newstring);
	}
	else
	{
		std::cout << "Enter new age: ";
		std::cin.ignore();
		std::getline(std::cin, newage);
		try {
			DogValidator::validateNumber(newage);
		}
		catch (ValidationException& ex)
		{
			std::cout << ex.getMessage() << std::endl;
			return;
		}
		res = this->serv->updateService(name, command, "", stoi(newage));
	}
	if (res == true)
		std::cout << "Successful update\n";
	else std::cout << "No such dog\n";
}

void Ui::UserMenu()
{
	std::cout << "\n";
	std::cout << "     -----MENU-----\n";
	std::cout << "       1. See all dogs" << std::endl;
	std::cout << "       2. Show all dogs of a certain breed" << std::endl;
	std::cout << "       3. See the adoption list" << std::endl;
	std::cout << "       4. Exit" << std::endl;
}

void Ui::parseDogs(bool filtered_flag)
{
	int index = 0;
	Dog d;
	int cmd;
	std::vector<Dog> dogs;
	if (filtered_flag == false)
		dogs = this->serv->getDogs();
	else
	{
		std::string breed;
		int age;
		std::cout << "Enter breed: ";
		std::cin.ignore();
		getline(std::cin, breed);
		std::cout << "Enter max age: ";
		std::cin >> age;
		dogs = this->userserv->filterDogs(breed, age);
	}

	while (true)
	{
		if (index >= dogs.size())
		{
			index = 0;
		}
		if (index == 0)
			std::cout << "	These are all the dogs in the shelter!\n";
		d = dogs[index];

		std::string Url = d.getLink();
		std::cout << d.str() << std::endl;
		waitForSeconds(1);
		system(std::string("start " + Url).c_str());

		std::cout << "1. Adopt\n";
		std::cout << "2. Next\n";
		std::cout << "3. Exit\n";
		std::cout << ">>";
		std::cin >> cmd;
		if (cmd == 1) {
			if (this->userserv->addToList(d) == true)
				std::cout << "Dog added to the adoption list\n";
			else std::cout << "Dog already in the adoption list\n";
			index++;
		}
		else if (cmd == 2) {
			index++;
			continue;
		}
		else if (cmd == 3) {
			break;
		}
		else {
			std::cout << "Invalid command! \n";
		}
	}
}

void Ui::printList()
{	/*
	std::cout << "Adoption list:\n";
	if (this->userserv->getListSize() == 0)
	{
		std::cout << "No dogs in the adoption list\n";
		return;
	}

	for (auto d : this->userserv->getAdoptionList())
	{
		std::cout << d.str() << std::endl;
	}
	*/
  //  std::wstring name = std::wstring(this->userserv->getAdoptionListFileName().begin(), this->userserv->getAdoptionListFileName().end());
	ShellExecuteA(NULL, NULL, this->userserv->getAdoptionListFileName().c_str(), NULL, NULL, SW_SHOWNORMAL);
	/*
	for (int i = 0; i < this->userserv->getListSize();i++)
	{
		Dog d = this->userserv->getAdoptionList()[i];
		std::cout<<d.str()<<std::endl; 
	}
	*/
}

int Ui::listMode()
{
	int op;
	std::cout << "Choose list mode:\n";
	std::cout << "1. CSV file\n";
	std::cout << "2. HTML file\n";
	std::cout << ">>";
	std::cin >> op;
	return op;
}

int Ui::service_mode()
{
	int cmd;
	std::cout << "Choose application mode:\n";
	std::cout << "1. Admin mode\n";
	std::cout << "2. User mode\n";
	std::cout << ">>";
	std::cin >> cmd;

	if (cmd == 1)
	{
		std::cout << "Admin mode\n";
	}
	else if (cmd == 2)
	{
		std::cout << "User mode\n";
	}
	else
	{
		std::cout << "Invalid command\n";
	}
	return cmd;
}
