package main

import (
	"testing"
)

func makeIntList(startingInt, len int) *List {
	list := NewList()
	for i := 0; i < len; i += 1 {
		list.Append(i + startingInt)
	}
	return list
}

func TestListNode_Get(t *testing.T) {

	list := makeIntList(1, 3)

	target := 2
	x, err := list.Get(target)
	if err != nil {
		t.Fatal(err)
	}
	if x.(int)-1 != target {
		t.Fatal("incorrect value returned,", x.(int))
	}

}

func TestListNode_Append(t *testing.T) {

	list := makeIntList(1, 3)

	v := 17

	lenBefore := list.Length()
	list.Append(v)
	lenAfter := list.Length()

	if lenAfter - lenBefore != 1 {
		t.Fatal("delta between list length before and after Append is not one, got", lenAfter - lenBefore)
	}

	x, err := list.Get(lenAfter-1)
	if err != nil {
		t.Fatal(err)
	}
	if x.(int) != v {
		t.Fatal("incorrect value returned,", x.(int))
	}

}

func TestListNode_Length(t *testing.T) {
	list := makeIntList(1, 3)
	if x := list.Length(); x != 3 {
		t.Fatal("incorrect length returned,", x)
	}
}