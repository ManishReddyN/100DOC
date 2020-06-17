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
    cout<<"Nodes:/n";
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