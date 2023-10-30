#include "lists.h"

/**
 * check_cycle - This function checks if a list has a cycle
 * @list: the linked list
 *
 * Return: 1 if there is cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fst, *slow;

	if (!list || !list->next)
		return (0);
	fst = list;
	slow = list;

	while (slow != NULL && fst != NULL && fst->next != NULL)
	{
		slow = slow->next;
		fst = fst->next->next;
		if (slow == fst)
		{
		return (1);
		}
	}
	return (0);
}
