#include "UI.h"
#include <iostream>
#define _CRTDBG_MAP_ALLOC
#include <crtdbg.h>
//#include "Test.h"

int main() {

	_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
	//	_CrtSetBreakAlloc(289);

	{
		Repository repo;
		Service serv(&repo);
		AdoptionList* adoptionList = new AdoptionList;
		UserService userserv(&repo, adoptionList);
		Ui ui(&serv, &userserv);

		std::cout << "-----WELCOME TO THE DOG SHELTER-----\n";
		std::cout << "\n";
		int cmd = ui.service_mode();
		if (cmd == 1)
		{
			while (true) {
				ui.menu();
				int command;
				std::cout << "Enter command: ";
				std::cin >> command;
				if (command == 1)
					ui.addUi();
				else if (command == 2)
					ui.removeUi();
				else if (command == 3)
					ui.updateUi();
				else if (command == 4)
					ui.printRepo();
				else if (command == 5)
					break;
				else
					std::cout << "Invalid command\n";
			}
		}
		else if (cmd == 2) {
			
			int op=ui.listMode();
			if (op == 1)
			{
				delete adoptionList;
				adoptionList = new AdoptionListCSV("adoptionlist.csv");
			}
			else if (op == 2)
			{
				delete adoptionList;
				adoptionList = new AdoptionListHTML("adoptionlist.html");
				
			}
			else
			{
				std::cout << "Invalid command\n";
				return 0;
			}

			UserService userserv2(&repo, adoptionList);
			userserv=userserv2;
			Ui ui(&serv, &userserv);
			while (true) {
				ui.UserMenu();
				int command;
				std::cout << "Enter command: ";
				std::cin >> command;
				std::cout << "\n";
				if (command == 1)
					ui.parseDogs();
				else if (command == 2)
					ui.parseDogs(true);
				else if (command == 3)
					ui.printList();
				else if (command == 4)
					break;
				else
					std::cout << "Invalid command!";
			}
		}
		else
			std::cout << "Invalid command\n";
		delete adoptionList;
	}
	_CrtDumpMemoryLeaks();

}
