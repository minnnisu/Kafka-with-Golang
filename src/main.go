package main

import (
	"main/producer"
	"sync"
)

func main() {
	// generate WaitGroup
	// Used to synchronize goroutines
	var wg sync.WaitGroup

	wg.Add(4)

	go func() {
		defer wg.Done()		// signal the termination of a goroutine
		producer.Producer("1")
	}()

	go func() {
		defer wg.Done()
		producer.Producer("2")
	}()

	go func() {
		defer wg.Done()
		producer.Producer("3")
	}()

	go func() {
		defer wg.Done()
		producer.Producer("4")
	}()

	wg.Wait()
}