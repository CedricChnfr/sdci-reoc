package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
)

type Data struct {
	Device string `json:"device"`
	Label  string `json:"label"`
	Value  int    `json:"value"`
	Id     int    `json:"id"`
}
type Packet struct {
	Label string `json:"label"`
	Value int    `json:"value"`
	Id    int    `json:"id"`
}

var dataList []Data

func postDataHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Only POST method is allowed", http.StatusMethodNotAllowed)
		return
	}

	device := r.URL.Query().Get("device")
	label := r.URL.Query().Get("label")
	valueStr := r.URL.Query().Get("value")
	if device == "" || label == "" || valueStr == "" {
		http.Error(w, "Missing required query parameters", http.StatusBadRequest)
		return
	}
	value, err := strconv.Atoi(valueStr)
	if err != nil {
		http.Error(w, "Invalid value for parameter 'value'", http.StatusBadRequest)
		return
	}

	dataList = append(dataList, Data{
		Device: device,
		Label:  label,
		Value:  value,
		Id:     len(dataList),
	})
	println("From '", device, "': ", value)
	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(dataList[len(dataList)-1]); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func getDataHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Only GET method is allowed", http.StatusMethodNotAllowed)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(dataList); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func getPacket(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Only GET method is allowed", http.StatusMethodNotAllowed)
		return
	}
	device := r.URL.Query().Get("device")
	if device == "" {
		http.Error(w, "Missing required query parameter: device", http.StatusBadRequest)
		return
	}

	var p []Packet
	for _, data := range dataList {
		if data.Device == device {
			p = append(p, Packet{
				Label: data.Label,
				Value: data.Value,
				Id:    data.Id,
			})
		}
	}

	if len(p) == 0 {
		http.Error(w, "Packet not found for the given device", http.StatusNotFound)
	} else {
		w.Header().Set("Content-Type", "application/json")
		if err := json.NewEncoder(w).Encode(p); err != nil {
			http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		}
	}
}

func main() {
	http.HandleFunc("/post_data", postDataHandler)
	http.HandleFunc("/get_data", getDataHandler)
	http.HandleFunc("/get_packet", getPacket)
	if err := http.ListenAndServe(":7070", nil); err != nil {
		fmt.Println("Could not start the server:", err)
	}
}
