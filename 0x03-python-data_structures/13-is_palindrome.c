#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if the linked list value is symmetry
 * @head: the starting point of the linked list
 * Return: 0 if not palindrome. 1 if palindrome
 */
/**
int is_palindrome(listint_t **head)
{
	listint_t *start, *end;
	int a[100];
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
*/
int isPalindromeUtil(listint_t **left, listint_t *right)
{
    /* stop recursion when right becomes NULL */
    if (right == NULL)
        return 1;

    /* If sub-list is not palindrome then no need to check for current left and right, return false */
    int isp = isPalindromeUtil(left, right->next);
    if (isp == 0)
        return 0;

    /* Check values at current left and right */
    int isp1 = (right->n == (*left)->n);

    /* Move left to next node */
    *left = (*left)->next;

    return isp1;
}

/* The main function that checks if linked list is palindrome or not */
int is_palindrome(listint_t **head)
{
   return isPalindromeUtil(head, *head);
}
