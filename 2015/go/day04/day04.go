package day04

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"strconv"
	"strings"
)

func GetHashCount(key string) int {

	for i := 0; i < 100000000; i++ { //
		var keystring = strings.Join([]string{key, strconv.Itoa(i)}, "")
		data := []byte(keystring)
		hash := md5.Sum(data)
		str := hex.EncodeToString(hash[:])
		if str[:5] == "00000" {
			return i
		}
	}
	return 0
}

func GetHashCount6Zeros(key string) int {

	for i := 0; i < 10000000000; i++ { //
		var keystring = strings.Join([]string{key, strconv.Itoa(i)}, "")
		data := []byte(keystring)
		hash := md5.Sum(data)
		str := hex.EncodeToString(hash[:])
		if str[:5] == "000000" {
			return i
		}
	}
	return 0
}

func Day4sideB(key string) string {
	for i := 0; i < 10000000; i++ {
		h := md5.New()
		keystring := strings.Join([]string{key, strconv.Itoa(i)}, "")
		io.WriteString(h, keystring)
		// first6 := fmt.Sprintf("%x", h.Sum(nil))[:6]
		str := fmt.Sprintf("%x", h.Sum(nil))[:6]
		if str == "000000" {

			// if first6 == "000000" {
			return strconv.Itoa(i)
		}
	}
	return "No match found"
}

func sum(list []byte) int {
	var result byte
	for i := 0; i < len(list); i++ {
		result += list[i]
	}
	return int(result)
}
