#include "ui.h"
#include "repository.h"
#include "undoredo.h"
#define _CRTDBG_MAP_ALLOC
#include <crtdbg.h>
#include "tests.h"

int main()
{
	_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
	Repo* repo = createRepo(10);
	UndoRedo* undoredo = createUndoRedo();
	Service serv = createService(repo, undoredo);

	UI ui = createUI(serv);
	generate_products(repo);

	while (1)
	{
		all_tests();
		menu();
		printRepo(repo->products);
		int cmd;
		printf("\nCommand: "); 
		scanf("%d", &cmd);
		if (cmd == 1)
			addUi(&serv);
		else if (cmd == 2)
			deleteUi(&serv);
		else if (cmd == 3)
			updateQuantityUi(&serv);
		else if (cmd == 4)
			updateExpirationUi(&serv);
		else if (cmd == 5)
			filter(&serv);
		else if (cmd == 6)
			undoUI(&serv);
		else if (cmd == 7)
			redoUI(&serv);
		else if (cmd == 8)
			expirationSoon(&serv);
		else if (cmd == 9)
			sortUI(&serv);
		else
			break;
	}
	destroy(repo);
	destroyUndoRedo(undoredo);
	_CrtDumpMemoryLeaks();
	return 0;
}
