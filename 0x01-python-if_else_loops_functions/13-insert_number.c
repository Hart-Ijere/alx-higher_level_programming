#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to insert into the list
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *prev;

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (!(*head) || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current = *head;
    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    new_node->next = current;
    prev->next = new_node;

    return (new_node);
}
