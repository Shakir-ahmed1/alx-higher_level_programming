#include "lists.h"
/**
 * check_cycle - it checks if a given linked list has a cycle
 * @list: the first list
 * Return: 0 if there is no cycle. 1 if ther is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *move;
	int i = 0, j = 0;

	temp = malloc(sizeof(listint_t));
	move = malloc(sizeof(listint_t));
	if (temp == NULL || temp == NULL)
		return (1);
	temp = list;
	move = list;
	if (move == move->next)
	{
		return (1);
	}
	while (1)
	{
		move = list;
		temp = temp->next;
		j = 0;
		while (j < i)
		{
			move = move->next;
			if (temp == move)
			{
				return (1);
			}
			if (temp == NULL || move == NULL)
			{
				return (0);
			}
			j++;
		}
		i++;
	}
	return (0);
}
