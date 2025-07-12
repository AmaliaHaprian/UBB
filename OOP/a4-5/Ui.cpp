#include "Ui.h"
#include <iostream>
#include <string>
#include <utility>
#include <windows.h>
#include <cstdlib>
#include <chrono>
#include <thread>

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
	std::cin >> name;
	std::cout << "\n";

	try
	{
		this->serv->removeService(name);
		std::cout << "Dog removed from the shelter\n";
	}
	catch (const std::exception& e)
	{
		std::cout << "Not available...Dog already adopted\n";
	}
}

void Ui::printRepo()
{
	std::cout << "Dogs:\n";

	for (int i = 0; i < this->serv->getSize();i++)
	{
		Dog d = this->serv->getDog(i);
		std::cout << d.str() << std::endl;
	}
}

void Ui::updateUi()
{
	int command, newage;
	std::string name, newstring;
	bool res;

	std::cout << "Enter name of dog: ";
	std::cin >> name;

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
		res = this->serv->updateService(name, command, newstring);
	}
	else
	{
		std::cout << "Enter new age: ";
		std::cin >> newage;
		res = this->serv->updateService(name, command, "", newage);
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
	DynamicVector<Dog> dogs;
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
		if (index >= dogs.length())
		{
			index = 0;
		}
		if (index == 0)
			std::cout << "	These are all the dogs in the shelter!\n";
		d = dogs.getElem(index);

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
{
	std::cout << "Adoption list:\n";
	if (this->userserv->getListSize() == 0)
	{
		std::cout << "No dogs in the adoption list\n";
		return;
	}
	for (int i = 0; i < this->userserv->getListSize();i++)
	{
		Dog d = this->userserv->getAdoptionList().getElem(i);
		std::cout << d.str() << std::endl;
	}
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