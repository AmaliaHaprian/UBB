#pragma once
#include "Dog.h"
#include "Repository.h"
#include "Service.h"
#include "UserService.h"

class Test
{
private:
	void test_repo();
	void test_dog();
	void test_service();
	void test_user_service();
public:
	void test_all();
};
