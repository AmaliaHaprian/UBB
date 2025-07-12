#pragma once

#include "DynamicVector.h"
#include "Dog.h"
#include "Repository.h"
#include "Service.h"
#include "UserService.h"

class Tests
{

private:
	void test_da();
	void test_repo();
	void test_dog();
	void test_service();
	void test_user_service();
public:
	void test_all();
};

