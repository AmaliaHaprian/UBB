#include "Tests.h"
#include <assert.h>

void Tests::test_da()
{
	DynamicVector<Dog> vector;

	assert(vector.length() == 0);

	Dog d("Husky", "Bruno", 1, "vcdvs");
	vector.addElem(d);
	assert(vector.length() == 1);

	assert(d == vector.getElem(0));

	Dog d2("Retriever", "Lola", 5, "bbef");
	vector.updateElem(d, d2);

	vector.deleteElem(d2);
	assert(vector.length() == 0);

	DynamicVector<Dog> vector2(vector);
	assert(vector2.length() == 0);

	vector.addElem(d);
	vector2 = vector;
	assert(vector2.length() == 1);

	DynamicVector<Dog> v3;
	v3 = v3;
	assert(v3.length() == 0);
}

void Tests::test_repo()
{
	Repository repo;
	Dog d("Husky", "Bruno", 1, "vcdvs");
	assert(repo.searchRepo("Bruno") == -1);

	assert(repo.removeRepo("Bruno") == false);

	repo.addRepo(d);
	assert(repo.lengthRepo() == 1);
	assert(repo.getDog(0) == d);
	assert(repo.searchRepo("Bruno") == 0);

	assert(repo.addRepo(d) == false);

	Dog d2("Retriever", "Lola", 5, "bbef");
	repo.updateRepo(d, d2);
	assert(repo.searchRepo("Lola") == 0);
	repo.removeRepo("Lola");
	assert(repo.lengthRepo() == 0);
	assert(repo.searchRepo("Lola") == -1);

	repo.addRepo(d);
}

void Tests::test_dog()
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

void Tests::test_service()
{
	Repository repo;
	Service serv(&repo);

	assert(repo.lengthRepo() == serv.getRepo().lengthRepo());

	assert(serv.getSize() == 10);

	std::string name = "Otto";
	std::string breed = "Husky";
	int age = 1;
	std::string link = "vcdvs";
	serv.addService(breed, name, age, link);
	assert(serv.getSize() == 11);

	assert(serv.addService("Husky", "Otto", 1, "vcdvs") == false);

	serv.removeService("Otto");
	assert(serv.removeService("Otto") == false);


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

	Dog* dogs = serv.getElements();
	assert(dogs[0].getName() == "Bruno");

	DynamicVector<Dog> dogs2 = serv.getDogs();
	assert(dogs2.length() == 10);
}

void Tests::test_user_service()
{
	Repository repo;
	UserService userserv(&repo);

	Dog d("Saint Bernard", "Bruno", 5, "https://images.app.goo.gl/NJqT7SCz5RBCDQXX9");
	repo.addRepo(d);
	userserv.addToList(d);
	assert(userserv.getAdoptionList().length() == 1);

	Dog d2("Husky", "Bella", 2, "https://images.app.goo.gl/tQLFozxvJgeETdhC6");
	repo.addRepo(d2);
	Dog d3("Saint Bernard", "Jack", 4, "https://images.app.goo.gl/fC7XXaM5zzkKFfTJA");
	repo.addRepo(d3);

	DynamicVector<Dog>filtered = userserv.filterDogs("Saint Bernard", 5);
	assert(filtered.length() == 2);

}

void Tests::test_all()
{
	test_dog();
	test_da();
	test_repo();
	test_service();
	test_user_service();
}
