#include "lists.h"

/**
 * check_cycle - checks if there's a cycle in a linked list
 * @list: list to be checked
 *
 * Return: 0 if no cycle found, 1 if theres a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first != NULL && first->next != NULL)
	{
		first = first->next->next;
		second = second->next;

		if (first == second)
		{
			return (1);
		}
	}

	return (0);
}
