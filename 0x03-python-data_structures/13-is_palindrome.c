#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if the linked list value is symmetry
 * @head: the starting point of the linked list
 * Return: 0 if not palindrome. 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *end;
	int a[1000];
	int i = 0, len = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	start = malloc(sizeof(listint_t));
	end = malloc(sizeof(listint_t));
	if (start == NULL || end == NULL)
		return (0);
	start = *head;
	while (start != NULL)
	{
		a[len] = start->n;
		len++;
		start = start->next;
	}
	for (i = 0; i <= (len / 2); i++)
	{
		if (a[i] == a[len - i - 1])
			continue;
		else
			return (0);
	}
	return (1);
}
