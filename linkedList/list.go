package main

import (
	"errors"
	"fmt"
)


type ListNode struct {
	next  *ListNode
	value interface{}
}

type List struct {
	first *ListNode
}

func NewList() *List {
	return new(List)
}

func (li *List) String() string {
	if li.first == nil {
		return "[]"
	}
	var items []interface{}
	current := li.first
	
	for current.next != nil {
		items = append(items, current.value)
		current = current.next
	}
	
	items = append(items, current.value) // the loop means that the 

	return fmt.Sprint(items)
}

func (li *List) Get(index int) (interface{}, error) {

	if li.first == nil {
		return struct{}{}, errors.New("empty list")
	}

	current := li.first
	for i := 0; i < index; i += 1 {
		if current.next == nil {
			return struct{}{}, errors.New("index out of range")
		}
		current = current.next
	}
	return current.value, nil
}

func (li *List) Append(value interface{}) {

	newNode := &ListNode{value: value}

	// if the list is empty, put the new value in the first position
	if li.first == nil {
		li.first = newNode
		return
	}
	// else traverse the list to the last node
	current := li.first
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
}

func (li *List) Length() int {

	if li.first == nil {
		return 0
	}

	count := 1
	current := li.first
	for {
		if current.next == nil {
			break
		}
		count += 1
		current = current.next
	}
	return count
}