#include "Service.h"

Service::Service(Repository* repo)
{
    this->repo = repo;
    //  this->generate_dogs();
    //this->repo->load();
}

bool Service::addService(std::string breed, std::string name, int age, std::string link)
{
    Dog d = Dog(breed, name, age, link);
    return this->repo->addRepo(d);
}

bool Service::removeService(std::string name)
{
    return this->repo->removeRepo(name);
}

Repository Service::getRepo()
{
    return this->repo->getRepo();
}

int Service::getSize()
{
    return this->repo->lengthRepo();
}

Dog Service::getDog(int pos)
{
    return this->repo->getDog(pos);
}

bool Service::updateService(std::string name, int command, std::string newstring, int newage)
{
    int pos = this->repo->searchRepo(name);
    if (pos != -1)
    {
        Dog old = this->getDog(pos);
        Dog d = this->getDog(pos);
        if (command == 1)
            d.setBreed(newstring);
        else if (command == 2)
            d.setAge(newage);
        else if (command == 3)
            d.setLink(newstring);
        this->repo->updateRepo(old, d);
        return true;
    }
    return false;

}

void Service::generate_dogs()
{
    this->addService("Saint-Bernard", "Bruno", 5, "https://images.app.goo.gl/NJqT7SCz5RBCDQXX9");
    this->addService("Husky", "Bella", 2, "https://images.app.goo.gl/tQLFozxvJgeETdhC6");
    this->addService("Golden-Retriever", "Daisy", 1, "https://images.app.goo.gl/GELeyXob7Dm1b8g88");
    this->addService("Bulldog", "Cooper", 3, "https://images.app.goo.gl/ZL6URyKZtSd3NGzd7");
    this->addService("Poodle", "Apollo", 7, "https://images.app.goo.gl/si6RgTxBnJX15dHi9");
    this->addService("German-Shepherd", "Lola", 4, "https://images.app.goo.gl/cSTpU3HYBeidPCqU6");
    this->addService("Doberman", "Kyra", 5, "https://images.app.goo.gl/JMZjaprv61sT6vVE9");
    this->addService("Cane-Corso", "Tucker", 8, "https://images.app.goo.gl/4wVG5c6xX4nyyWeAA");
    this->addService("Corgi", "Ollie", 1, "https://images.app.goo.gl/vnT4s1XemoC8zV8e7");
    this->addService("Saint-Bernard", "Jack", 4, "https://images.app.goo.gl/fC7XXaM5zzkKFfTJA");

}



std::vector<Dog> Service::getDogs()
{
    std::vector<Dog> dogs;

    for (int i = 0; i < this->getSize(); i++)
    {
        dogs.push_back(this->getDog(i));
    }
    return dogs;
}
