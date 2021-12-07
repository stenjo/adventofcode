package day05

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func GetHashCount(key string, depth int) []string {

	var keys []string

	for i := 0; i < 100000000; i++ { //
	var keystring = strings.Join([]string{key, strconv.Itoa(i)}, "")
		data := []byte(keystring)
		hash := md5.Sum(data)
		str := hex.EncodeToString(hash[:])
		if str[:5] == "00000" {
			keys = append(keys,str[5:])
			if len(keys) == depth {
				return keys
			}
		}
	}
	return []string {}
}

func GetHash(key string, seed string) (string, bool) {
	var keystring = strings.Join([]string{key, seed}, "")
	data := []byte(keystring)
	hash := md5.Sum(data)
	str := hex.EncodeToString(hash[:])
	if str[:5] == "00000" {
		return str[5:], true
	}

	return "", false
}

func GetPassword(str string) string {

	var password string
	for _, k := range GetHashCount(str, 8) {
		password = password + string(k[0])
	}
	return password
}

func GetBetterSolution(str string) string {

	var password = []string{"_","_","_","_","_","_","_","_",}
	for i := 0; i < 100000000 && strings.Contains(strings.Join(password, ""), "_"); i++ { //
		key,ok := GetHash(str, strconv.Itoa(i))
		if ok {
			password = UpdatePassword(password, key)
			fmt.Print("\r", strings.Join(password, ""))
		}
	}

	return "\r" + strings.Join(password,"")
}

func UpdatePassword(password []string, key string) []string {

	pos,_ := strconv.ParseInt(string(key[0]), 16, 0)
	if pos < 8 && password[pos] == "_" {
		password[pos] = string(key[1])
	}
	return password
}
