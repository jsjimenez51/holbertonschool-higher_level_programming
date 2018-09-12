#include "lists.h"

/**
 * insert_node - inserts a new node into a linked list.
 * @head: a pointer to the head node of a linked list.
 * @number: the number to be stored in the new node.
 *
 * Return: returns a pointer to the new node in the list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new)
	{
		new->n = number;
		new->next = *head;
		if (!new->next || new->n <= (*head)->n)
			*head = new;
		else
			while (new->next && new->n > new->next->n)
			{
				tmp = new->next;
				new->next = tmp->next;
			}
		if (tmp)
			tmp->next = new;
	}
	return (new);
}
