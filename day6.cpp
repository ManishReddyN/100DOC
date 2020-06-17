/*Question:
This problem was asked by Google.
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
*/

#include <bits/stdc++.h>
#include <inttypes.h>
using namespace std;
class Node
{
public:
    int val;
    Node *ptr;
};

Node *XOR(Node *a, Node *b)
{
    return (Node *)((uintptr_t)(a) ^ (uintptr_t)(b));
}

void insert(Node **head_ref, int val)
{

    Node *new_node = new Node();
    new_node->val = val;
    new_node->ptr = *head_ref;
    if (*head_ref != NULL)
    {
        (*head_ref)->ptr = XOR(new_node, (*head_ref)->ptr);
    }
    *head_ref = new_node;
}
void printList(Node *head)
{
    Node *curr = head;
    Node *prev = NULL;
    Node *next;
    cout << "Nodes:/n";
    while (curr != NULL)
    {
        cout << curr->val << " ";
        next = XOR(prev, curr->ptr);
        prev = curr;
        curr = next;
    }
    cout << "\n";
}
int main()
{
    Node *head = NULL;
    insert(&head, 10);
    insert(&head, 20);
    insert(&head, 30);
    insert(&head, 40);
    printList(head);
    return (0);
}