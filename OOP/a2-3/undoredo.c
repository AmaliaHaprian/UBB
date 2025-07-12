#include "undoredo.h"
#include <stdlib.h>
#include <string.h>

void recordUndo(UndoStack* undostack, Operation* operation);
void recordRedo(RedoStack* redostack, Operation* operation);

UndoStack* createUndoStack();
RedoStack* createRedoStack();

Operation* createOperation(Product p, char* operationType)
{
	Operation* operation = (Operation*)malloc(sizeof(Operation));
	if (operation == NULL)
		return NULL;
	operation->product = p;
	operation->operationType = operationType;

	return operation;
}

UndoStack* createUndoStack()
{
	UndoStack* undostack = (UndoStack*)malloc(sizeof(UndoStack));
	undostack->operations = createDynamicArray(5);
	if (undostack->operations == NULL)
	{
		free(undostack);
		return;
	}
	return undostack;
}

RedoStack* createRedoStack()
{
	RedoStack* redostack = (RedoStack*)malloc(sizeof(RedoStack));
	redostack->operations = createDynamicArray(5);
	if (redostack->operations == NULL)
	{
		free(redostack);
		return;
	}
	return redostack;
}

UndoRedo* createUndoRedo()
{
	UndoRedo* undoredo = (UndoRedo*)malloc(sizeof(UndoRedo));
	if (undoredo == NULL) {
		return;
	}
	undoredo->undostack = createUndoStack();

	if (undoredo->undostack == NULL) {
		free(undoredo);
		return NULL;
	}
	undoredo->redostack = createRedoStack();
	if (undoredo->redostack == NULL) {
		destroyUndoStack(undoredo->undostack);
		free(undoredo);
		return NULL;
	}
	undoredo->currentIndex = -1;
	return undoredo;
}

void recordOperation(UndoRedo* undoredo, Operation* operation1, Operation* operation2)
{
	recordUndo(undoredo->undostack, operation1);
	recordRedo(undoredo->redostack, operation2);
	undoredo->currentIndex = getUndoStackSize(undoredo) - 1;
}

void recordUndo(UndoStack* undostack, Operation* operation)
{
	addElem(undostack->operations, operation);
}

void recordRedo(RedoStack* redostack, Operation* operation)
{
	addElem(redostack->operations, operation);
}

int undo(UndoRedo* undoredo, Repo* repo)
{
	if (undoredo->currentIndex == -1)
		return 0;

	Operation* operation = (Operation*)getElemOnPos(getOperationsForUndo(undoredo), undoredo->currentIndex);

	if (strcmp(operation->operationType, "add") == 0)
		addProduct(repo, operation->product);
	else if (strcmp(operation->operationType, "delete") == 0)
		deleteProduct(repo, operation->product.name, operation->product.category);
	else if (strcmp(operation->operationType, "update") == 0)
		updateQuantity(repo, operation->product.name, operation->product.category, operation->product.quantity);
	undoredo->currentIndex--;
	return 1;
}

int redo(UndoRedo* undoredo, Repo* repo)
{
	if (undoredo->currentIndex == getRedoStackSize(undoredo) - 1)
		return 0;

	undoredo->currentIndex++;
	Operation* operation = (Operation*)getElemOnPos(getOperationsForRedo(undoredo), undoredo->currentIndex);

	if (strcmp(operation->operationType, "add") == 0)
		addProduct(repo, operation->product);
	else if (strcmp(operation->operationType, "delete") == 0)
		deleteProduct(repo, operation->product.name, operation->product.category);
	else if (strcmp(operation->operationType, "update") == 0)
		updateQuantity(repo, operation->product.name, operation->product.category, operation->product.quantity);
	return 1;
}

void destroyOperation(Operation* operation)
{
	free(operation);
}

void destroyUndoStack(UndoStack* undostack)
{
	for (int i = 0; i < getSize(undostack->operations); i++)
		destroyOperation(getElemOnPos(undostack->operations, i));
	destroyArray(undostack->operations);
	free(undostack);
}

void destroyRedoStack(RedoStack* redostack)
{
	for (int i = 0; i < getSize(redostack->operations); i++)
		destroyOperation(getElemOnPos(redostack->operations, i));
	destroyArray(redostack->operations);
	free(redostack);
}

void destroyUndoRedo(UndoRedo* undoredo)
{
	destroyUndoStack(undoredo->undostack);
	destroyRedoStack(undoredo->redostack);
	free(undoredo);
}

int getUndoStackSize(UndoRedo* undoredo)
{
	return getSize(getOperationsForUndo(undoredo));
}

int getRedoStackSize(UndoRedo* undoredo)
{
	return getSize(getOperationsForRedo(undoredo));
}

DynamicArray* getOperationsForUndo(UndoRedo* undoredo)
{
	return undoredo->undostack->operations;
}

DynamicArray* getOperationsForRedo(UndoRedo* undoredo)
{
	return undoredo->redostack->operations;
}
