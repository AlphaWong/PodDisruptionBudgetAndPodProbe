package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"
)

const (
	min = 0
	max = 3
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/ping", ping)
	s := &http.Server{
		Addr:         ":80",
		Handler:      mux,
		ReadTimeout:  1 * time.Minute,
		WriteTimeout: 1 * time.Minute,
	}
	log.Println(":80 started")
	log.Fatalln(s.ListenAndServe())
}

func ping(w http.ResponseWriter, req *http.Request) {
	time.Sleep(time.Duration(GetRandNumber(max, min)) * time.Second)
	fmt.Fprintf(w, "pong")
}

func GetRandNumber(max, min int) int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(max-min+1) + min
}
