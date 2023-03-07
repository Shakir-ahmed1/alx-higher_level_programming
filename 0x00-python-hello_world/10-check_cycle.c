#include "lists.h"
/**
 * free_both - it frees two memories at once
 * @a: first mem
 * @b: second mem
 */
void free_both(listint_t *a, listint_t *b)
{
	free(a);
	free(b);
}
/**
 * check_cycle - it checks if a given linked list has a cycle
 * @list: the first list
 * Return: 0 if there is no cycle. 1 if ther is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *move, *t, *m;
	int i = 0, j = 0;

	temp = malloc(sizeof(listint_t));
	move = malloc(sizeof(listint_t));
	if (temp == NULL || temp == NULL)
		return (1);
	t = temp;
	m = move;
	temp = list;
	move = list;
	if (list == NULL || list->next == NULL || move == move->next)
	{
		free_both(t, m);
		return (1);
	}
	while (1)
	{
		move = list;
		temp = temp->next;
		j = 0;
		while (j < i)
		{
			if (temp == move)
			{
				free_both(t, m);
				return (1);
			}
			if (temp == NULL || move == NULL)
			{
				free_both(t, m);
				return (0);
			}
			move = move->next;
			j++;
		}
		i++;
	}
	free_both(t, m);
	return (0);
}
