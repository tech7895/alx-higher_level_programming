#include "lists.h"

/**
 * insert_node - This function nserts a number into a sorted
 * singly-linked list
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the nw node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;

	if (node == NULL || node->n >= number)
	{
		nw->next = node;
		*head = nw;
		return (nw);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nw->next = node->next;
	node->next = nw;

	return (nw);
}
