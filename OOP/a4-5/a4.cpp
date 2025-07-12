#include "UI.h"
#include <iostream>
#define _CRTDBG_MAP_ALLOC
#include <crtdbg.h>
#include "Tests.h"

int main() {

	_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
	//	_CrtSetBreakAlloc(289);

	Tests test;
	test.test_all();

	{
		Repository repo;
		Service serv(&repo);
		UserService userserv(&repo);
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
	}

	_CrtDumpMemoryLeaks();

}