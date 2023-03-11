/**
 * is_palindrome - checks if the linked list value is symmetry
 * @head: the starting point of the linked list
 * Return: 0 if not palindrome. 1 if palindrome
 */
int isPalindromeUtil(listint_t **left, listint_t *right);
int is_palindrome(listint_t **head)
{
   return isPalindromeUtil(head, *head);
}
int isPalindromeUtil(listint_t **left, listint_t *right)
{
	int isp, isp1;

	if (right == NULL)
		return 1;
	isp = isPalindromeUtil(left, right->next);
	if (isp == 0)
		return 0;
	isp1 = (right->n == (*left)->n);
	*left = (*left)->next;

	return isp1;
}


