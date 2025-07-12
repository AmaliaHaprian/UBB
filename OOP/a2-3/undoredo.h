#pragma once
#include "domain.h"
#include "repository.h"

typedef struct {
	Product product;
	char* operationType;
} Operation;

typedef struct
{
	DynamicArray* operations;
}UndoStack;

typedef struct
{
	DynamicArray* operations;
}RedoStack;

typedef struct {
	UndoStack* undostack;
	RedoStack* redostack;
	int currentIndex;

} UndoRedo;

/*
* Creates an operation
* Input: a Product structure and a string operationType
* Output: a pointer to an Operation structure
*/
Operation* createOperation(Product p, char* operationType);

/*
* Creates an UndoRedo structure
* Input: -
* Output: a pointer to an UndoStack structure
*/
UndoRedo* createUndoRedo();

/*
* Records an operation in the undo stack and in the redo stack
* Input: a pointer to an UndoRedo structure, a pointer to an Operation structure for the undo stack and a pointer to an Operation structurem for the redo stack
* Output: -
*/
void recordOperation(UndoRedo* undoredo, Operation* operation1, Operation* operation2);

/*
* Tries to undo the last operation
* Input: a pointer to an UndoRedo structure and a pointer to a Repo structure
* Output: 1 if the operation was undone successfully, 0 if there are no more operations to undo
*/
int undo(UndoRedo* undoredo, Repo* repo);

/*
* Tries to redo the last operation
* Input: a pointer to an UndoRedo structure and a pointer to a Repo structure
* Output: 1 if the operation was redone successfully, 0 if there are no more operations to redo
*/
int redo(UndoRedo* undoredo, Repo* repo);

/*
* Destroys an operation
* Input: a pointer to an Operation structure
* Output: -
*/
void destroyOperation(Operation* operation);

/*
* Destroys an undo stack
* Input: a pointer to an UndoStack structure
* Output: -
*/
void destroyUndoStack(UndoStack* undostack);

/*
* Destroys a redo stack
* Input: a pointer to a RedoStack structure
* Output: -
*/
void destroyRedoStack(RedoStack* redostack);

/*
* Destroys an undo redo structure
* Input: a pointer to an UndoRedo structure
* Output: -
*/
void destroyUndoRedo(UndoRedo* undoredo);

int getUndoStackSize(UndoRedo* undoredo);

int getRedoStackSize(UndoRedo* undoredo);

DynamicArray* getOperationsForUndo(UndoRedo* undoredo);

DynamicArray* getOperationsForRedo(UndoRedo* undoredo);