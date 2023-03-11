#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if the linked list value is symmetry
 * @head: the starting point of the linked list
 * Return: 0 if not palindrome. 1 if palindrome
 */
int palind_checker(listint_t**, listint_t*);
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	return palind_checker(head, *head);
}
int palind_checker(listint_t **left, listint_t *right)
{
	int a;

	if (right == NULL)
		return (1);
	a = palind_checker(left, right->next);
	if (a == 0)
		return 0;
	if ((*left)->n == right->n)
	{
		(*left) = (*left)->next;
		return 1;
	}
	else
		return 0;

}
