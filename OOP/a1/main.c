/*
a. Read a sequence of natural numbers (sequence ended by 0) and determine the number of 0 digits of the product of the read numbers.
b. Given a vector of numbers, find the longest contiguous subsequence such that the sum of any two consecutive elements is a prime number.
*/


#include <stdio.h>
#include <assert.h>

typedef struct {
	int last_index;
	int first_index;
} Sequence_param;

/* Functions */

/*
The function computes the product of the elements of an array
:param v: pointer to an integer, more specifically, to the first element of the array
:param size: the number of elements of the array
return: the product
*/
int product(int* v, int size) {
	int p = 1, i;
	for (i = 0;i < size;i++)
		p *= v[i];
	return p;
}

/*
The function computes the number of 0 digits of an integer
:param p: an integer
return: the number of zero digits
*/
int zero_digits(int p) {
	int cnt = 0, c;
	while (p != 0) {
		c = p % 10;
		if (c == 0) cnt++;
		p /= 10;
	}
	return cnt;
}

/*
The function checks if an integer is a prime number
:param n: an integer
return: 1 if it's prime, 0 otherwise
*/
int check_prime(int n) {
	int ok = 1, d;
	if (n < 2 || (n % 2 == 0 && n != 2)) ok = 0;
	else {
		for (d = 3; d <= n / 2 && ok == 1;d += 2)
			if (n % d == 0) ok = 0;
	}
	return ok;
}

/*
The function computes the longest contiguous subsequence such that the sum of any two consecutive elements is a prime number
:param v: pointer to an integer, more specifically, to the first element of the array
:param size: the number of elements of the array
return: a struct of time Sequence_param, containing the first and last index of the subsequence
*/
Sequence_param check_sequence(int* v, int size) {
	Sequence_param param;
	int last_index = -1, max_length = 0, current_index = -1, current_max = 0, i;
	for (i = 0;i < size - 1;i++)
		if (check_prime(v[i] + v[i + 1]) == 1) {
			current_max++;
			current_index = i + 1;
		}
		else {
			if (current_max + 1 > max_length) {
				max_length = current_max + 1;
				last_index = current_index;
			}
			current_max = 0;
		}
	if (current_max + 1 > max_length) {
		max_length = current_max + 1;
		last_index = current_index;
	}
	if (max_length == 0) {
		param.first_index = -1;
		param.last_index = -1;
	}
	else {
		param.last_index = last_index;
		param.first_index = last_index - max_length + 1;
	}

	return param;
}


/* UI */
void option_error() {
	printf("Invalid option! Try again \n");
}

void unread_vector() {
	printf("You must read the vector first! \n");
}

void menu() {
	printf("	MENU\n");
	printf("1. Read vector\n");
	printf("2. Compute the number of zero digits of the product of read numbers\n");
	printf("3. Compute the longest subsequence such that the sum of any two consecutive elements is a prime number.\n");
	printf("4. Exit\n");
	printf("\n");
}

int get_input() {
	int option;
	printf("Enter your choice:");
	scanf_s("%d", &option);
	return option;
}

int read(int* v) {
	int n;
	int i = 0;
	printf("Enter the elements of the vector: ");
	while (1) {
		scanf_s("%d", &n);
		if (n == 0)
			break;
		v[i++] = n;
	}
	return i;
}
void print_zero_digits(int n) {
	printf("The number of zero digits of the product is: %d\n", n);
}

void print_sequence(int* v, Sequence_param param) {
	if (param.first_index == -1) {
		printf("There is no such subsequence\n");
	}
	else {
		int i;
		printf("The longest subsequence is: ");
		for (i = param.first_index;i <= param.last_index;i++)
			printf("%d ", v[i]);
		printf("\n");
	}

}

void print_exit() {
	printf("Goodbye!\n");
}


/* Test functions*/
void test_product() {
	int v[5] = { 1,2,3,4,5 }, size = 5, p;
	p = product(v, size);
	assert(p == 120);
}

void test_prime() {
	assert(check_prime(11) == 1);
	assert(check_prime(12) == 0);
}

void test_zero_digits() {
	assert(zero_digits(120) == 1);
	assert(zero_digits(100) == 2);
}

void test_sequence() {
	int v[10] = { 3, 12, 11, 2, 4, 8, 3, 2, 3, 1 }, size = 10;
	Sequence_param param;
	param = check_sequence(v, size);
	assert(param.first_index == 5);
	assert(param.last_index == 8);
}


/* Main */
int main() {
	test_product();
	test_prime();
	test_zero_digits();
	//	test_sequence();

	int v[100], size, option, p, cnt, read_vector = 0;
	Sequence_param param;
	while (1) {
		menu();
		option = get_input();
		if (option == 1)
		{
			size = read(v);
			read_vector = 1;
		}
		else if (option == 2)
		{
			if (read_vector == 0) {
				unread_vector();
				continue;
			}
			p = product(v, size);
			cnt = zero_digits(p);
			print_zero_digits(cnt);
		}
		else if (option == 3)
		{
			if (read_vector == 0) {
				unread_vector();
				continue;
			}
			param = check_sequence(v, size);
			print_sequence(v, param);
		}
		else if (option == 4)
		{
			print_exit();
			break;
		}
			
		else option_error();
	}
	return 0;
}