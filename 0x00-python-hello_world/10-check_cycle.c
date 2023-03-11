#include "lists.h"
/**
 * check_cycle - it checks if a given linked list has a cycle
 * @list: the first list
 * Return: 0 if there is no cycle. 1 if ther is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *move;
	int i = 0, j = 0;

	if (list == NULL || list->next == NULL)
	{
		return (0); }
	if (list == list->next)
	{
		return (1); }
	move = list;
	temp = list;
	while (1)
	{
		move = list;
		temp = temp->next;
		j = 0;
		while (j < i)
		{
			if (temp == move)
			{
				return (1);
			}
			if (temp == NULL || move == NULL)
			{
				return (0); }
			move = move->next;
			j++; }
		i++; }
	return (0); }
