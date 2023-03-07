#include "lists.h"
/**
 * insert_node - it inserts a new node to an existing linkedlist
 * @head: the address of the first node
 * @number: the value to be stored in the node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	temp = *head;
	while(temp->next->n < number)
	{
		if (!temp->next)
			break;
		if (temp->n < number)
			break;
		temp = temp->next;
	}
	if (!temp->next)
		temp->next = new;
	else
	{
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
