/*

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

*/


#include <stdio.h> 
#include <stdlib.h> 
#include <inttypes.h> 

struct Node 
{ 
	int data; 
	struct Node* npx; /* XOR of next and previous node */
}; 

struct Node* XOR (struct Node *a, struct Node *b) 
{ 
	return (struct Node*) ( (a) ^  (b)); 
} 


void add(struct Node **head, int data) 
{ 

	struct Node *new_node = (struct Node *) malloc (sizeof (struct Node) ); 
	new_node->data = data; 

	new_node->npx = XOR(*head, NULL); 


	if (*head!= NULL) 
	{ 

		struct Node* next = XOR((*head)->npx, NULL); 
		(*head_ref)->npx = XOR(new_node, next); 
	} 

	*head = new_node; 
} 


Node* get (struct Node *head,int index) 
{ 
	struct Node *curr = head; 
	struct Node *prev = NULL; 
	struct Node *next; 
    int i = 1 ; 

	while (i < index ) 
	{ 
		
		next = XOR (prev, curr->npx);
		prev = curr; 
		curr = next; 
	} 
} 

int main () 
{ 
	struct Node *head = NULL; 
	add(&head, 10); 
	add(&head, 20); 
	add(&head, 30); 
	add(&head, 40); 
  
  struct Node *elt = get(head,2) ;  
  printf("The element at the given index = %d " ,elt->data ) ; 


	return (0); 
} 
