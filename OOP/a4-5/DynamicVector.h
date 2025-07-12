#pragma once

template<typename T>

class DynamicVector
{
private:
	T* elems;
	int size;
	int capacity;

public:
	DynamicVector(int capacity = 10);
	~DynamicVector();
	void addElem(const T& e);
	int length() const;
	void deleteElem(const T& e);
	T getElem(int pos);
	void updateElem(T old, T newElem);
	T* getElements() { return this->elems; }
	DynamicVector(const DynamicVector& other);
	DynamicVector& operator=(const DynamicVector& v);

private:
	void resize();
};

template<typename T>
DynamicVector<T>::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elems = new T[this->capacity];
}

template<typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[] this->elems;
}

template<typename T>
void DynamicVector<T>::addElem(const T& e)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}

template<typename T>
int DynamicVector<T>::length() const
{
	return this->size;
}

template<typename T>
void DynamicVector<T>::deleteElem(const T& e)
{
	for (int i = 0; i < this->size;i++)
		if (this->elems[i] == e)
		{
			for (int j = i; j < this->size - 1; j++)
				this->elems[j] = this->elems[j + 1];
			this->size--;
		}
}

template<typename T>
inline T DynamicVector<T>::getElem(int pos)
{
	return this->elems[pos];
}

template<typename T>
void DynamicVector<T>::updateElem(T old, T newElem)
{
	for (int i = 0;i < this->size;i++)
		if (this->elems[i] == old)
			this->elems[i] = newElem;
}


template<typename T>
inline DynamicVector<T>::DynamicVector(const DynamicVector& other)
{
	this->size = other.size;
	this->capacity = other.capacity;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = other.elems[i];
}


template<typename T>
inline DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& v)
{
	if (this == &v)
		return *this;

	this->capacity = v.capacity;
	this->size = v.size;
	delete[] this->elems;

	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

template<typename T>
inline void DynamicVector<T>::resize()
{
	this->capacity *= 2;

	T* els = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		els[i] = this->elems[i];

	delete[] this->elems;
	this->elems = els;
}
