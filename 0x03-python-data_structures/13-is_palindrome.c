#include "lists.h"

/**
 * is_palindrome - checks if a given list is a palindrome.
 * @head: a double pointer to the head of the given list.
 *
 * Return: 1 if it is a Palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);
	return (pali_chkr(head, *head));

}

/**
 * pali_chkr - helper function that checks for palindrome by matching values in
 * list from beginning and end, inward.
 * @head: a double pointer to the head of the given list.
 * @end: a pointer to the end of the list.
 *
 * Return: 1 if it is a Palindrome, 0 if it is not.
 */
int pali_chkr(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	/* sets pointers to front and back of list then checks values */
	/* recursively progresses thru the list as long as vals match */
	if (pali_chkr(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
