package day05

import (
	"crypto/md5"
	"encoding/hex"
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

func GetPassword(str string) string {

	var password string
	for _, k := range GetHashCount(str, 8) {
		password = password + string(k[0])
	}
	return password
}