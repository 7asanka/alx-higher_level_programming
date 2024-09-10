#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: pointer to the first node
 * @number: number to be inserted
 *
 * Return: address of the inserted list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next != NULL && current->next->n >= number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
