#include "Test.h"
#include <assert.h>
#include "ValidationException.h"
void Test::test_repo()
{
	Repository repo;
	Dog d("Husky", "Bruno", 1, "vcdvs");
	assert(repo.searchRepo("Bruno") == 1);

	try
	{
		repo.removeRepo("Bruno");
		assert(false);
	}
	catch (ValidationException& ex)
	{
		assert(ex.getMessage() == "Dog not found in the shelter");

	}

	repo.addRepo(d);
	assert(repo.lengthRepo() == 1);
	assert(repo.getDog(0) == d);
	assert(repo.searchRepo("Bruno") == 0);

	try {
		repo.addRepo(d);
		assert(false);
	}
	catch (ValidationException& ex)
	{
		assert(ex.getMessage() == "Dog already in the shelter");
	}

	Dog d2("Retriever", "Lola", 5, "bbef");
	repo.updateRepo(d, d2);
	assert(repo.searchRepo("Lola") == 0);
	repo.removeRepo("Lola");
	assert(repo.lengthRepo() == 0);
	assert(repo.searchRepo("Lola") == -1);

	repo.addRepo(d);
}

void Test::test_dog()
{
	Dog d("Husky", "Bruno", 1, "vcdvs");
	assert(d.getAge() == 1);
	assert(d.getBreed() == "Husky");
	assert(d.getName() == "Bruno");
	assert(d.getLink() == "vcdvs");
	d.setAge(2);
	d.setBreed("Retriever");
	d.setLink("wdkc");
	assert(d.getAge() == 2);
	assert(d.getBreed() == "Retriever");
	assert(d.getLink() == "wdkc");

	std::string str = d.str();
	assert(str == "Name: Bruno; Breed: Retriever; Age: 2; Link: wdkc");
}

void Test::test_service()
{
	Repository repo;
	Service serv(&repo);

	assert(repo.lengthRepo() == serv.getRepo().lengthRepo());
	std::cout << serv.getSize()<<std::endl;
	assert(serv.getSize() == 10);

	std::string name = "Otto";
	std::string breed = "Husky";
	int age = 1;
	std::string link = "vcdvs";
	serv.addService(breed, name, age, link);
	assert(serv.getSize() == 11);

	try {
		serv.addService("Husky", "Otto", 1, "vcdvs");
		assert(false);
	}
	catch (ValidationException& ex)
	{
		assert(ex.getMessage() == "Dog already in the shelter");
	}

	serv.removeService("Otto");
	try { serv.removeService("Otto"); 
	assert(false);
	}
	catch (ValidationException& ex)
	{
		assert(ex.getMessage() == "Dog not found in the shelter");	
	}

	assert(serv.getSize() == 10);

	Dog d = serv.getDog(0);
	assert(d.getName() == "Bruno");

	serv.updateService("Bruno", 1, "Retriever");
	Dog d2 = serv.getDog(0);
	assert(d2.getBreed() == "Retriever");

	serv.updateService("Bruno", 2, "", 2);
	Dog d3 = serv.getDog(0);
	assert(d3.getAge() == 2);

	assert(serv.updateService("Lizzy", 1, "Retriever") == false);

	serv.updateService("Bruno", 3, "gfefw");
	Dog d4 = serv.getDog(0);
	assert(d4.getLink() == "gfefw");


	std::vector<Dog> dogs2 = serv.getDogs();
	assert(dogs2.size() == 10);
}

void Test::test_user_service()
{
	Repository repo;
	AdoptionList* adoptionList = new AdoptionList;
	UserService userserv(&repo, adoptionList);

	Dog d("Saint Bernard", "Bruno", 5, "https://images.app.goo.gl/NJqT7SCz5RBCDQXX9");
	repo.addRepo(d);
	userserv.addToList(d);
	assert(userserv.getAdoptionList().size() == 1);

	Dog d2("Husky", "Bella", 2, "https://images.app.goo.gl/tQLFozxvJgeETdhC6");
	repo.addRepo(d2);
	Dog d3("Saint Bernard", "Jack", 4, "https://images.app.goo.gl/fC7XXaM5zzkKFfTJA");
	repo.addRepo(d3);

	std::vector<Dog>filtered = userserv.filterDogs("Saint Bernard", 5);
	assert(filtered.size() == 2);
}

void Test::test_all()
{
	test_dog();
	test_repo();
	test_service();
	test_user_service();
}
