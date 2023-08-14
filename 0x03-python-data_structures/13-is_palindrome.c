#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - Reverses linked list
 * @h: Pointer to the first node
 * Return: Pointer to the first node of thenew list
 */
void reverse_listint(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *current = *h;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*h = prev;
}

/**
 * is_palindrome - checks if listed list is palindrome
 * @h: The double pointer of the linked list
 *
 * Return: 1 on success, and 0 if fail
 */
int is_palindrome(listint_t **h)
{
	listint_t *slow = *h;
	listint_t *fast = *h;
	listint_t *temp = *h;
	listint_t *dup = NULL;

	if (*h == NULL || (*h)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
	}

		reverse_listint(&dup);

		while (dup && temp)
		{
			if (temp->n == dup->n)
			{
				dup = dup->next;
				temp = temp->next;
			}
			else
				return (0);
		}
		if (!dup)
			return (1);
		return (0);
}
