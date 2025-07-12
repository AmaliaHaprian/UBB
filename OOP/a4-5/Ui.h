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
	void addUi();
	void menu();
	void removeUi();
	void printRepo();
	void updateUi();

	int service_mode();

	void UserMenu();
	void parseDogs(bool filtered_flag = false);
	void printList();
};

