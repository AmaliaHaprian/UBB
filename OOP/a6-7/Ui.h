#pragma once
#include "Service.h"
#include "UserService.h"

class Ui
{
private:
	Service* serv;
	UserService* userserv;

public:
	Ui(Service* serv, UserService* userserv);
	Ui& operator=(const Ui& other) {
		if (this != &other) {
			this->serv = other.serv;
			this->userserv = other.userserv;
		}
		return *this;
	}
	void addUi();
	void menu();
	void removeUi();
	void printRepo();
	void updateUi();

	int service_mode();

	void UserMenu();
	void parseDogs(bool filtered_flag = false);
	void printList();
	int listMode();
};
