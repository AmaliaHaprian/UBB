#include "validator.h"
#include "domain.h"
#include <time.h>

int validate_category(char* category)
{
	if (strcmp(category, "dairy") == 0 || strcmp(category, "sweets") == 0 || strcmp(category, "meat") == 0 || strcmp(category, "fruit") == 0)
		return 1;
	return 0;
}

int validate_date(Date date)
{
	time_t t= time(NULL);
	struct tm current_time;
	localtime_s(&current_time, &t);
	time_t today = mktime(&current_time);

	struct tm given_date = { 0 };
	given_date.tm_year = date.year - 1900;
	given_date.tm_mon = date.month - 1;
	given_date.tm_mday = date.day;
	time_t given_time = mktime(&given_date);

	if (difftime(given_time, today) > 0)
		return 1;
	return 0;

}
