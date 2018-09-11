#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to a linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *checker = NULL, *current = NULL;

	if (!list || list->next == NULL)
		return (0);
	current = list;
	checker = current->next;

	while (current != NULL && checker->next != NULL
	       && checker->next->next != NULL)
	{
		if (current == checker)
			return (1);
		current = current->next;
		checker = checker->next->next;
	}
	return (0);
}
