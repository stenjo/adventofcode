package day07

import (
	"strings"
)

func CountIPsSupportingTLS(str []string) int {

	ips := parseLines(str)
	var count int

	for _, ip := range ips {
		if ip.supportsTLS() {
			count++
		}
	}
	return count
}

type Ip struct {
	ip string
	hs string
}

func parseLines(str []string) []Ip {

	iplist := make([]Ip, 0, len(str))

	for _, v := range str {
		parts := strings.Split(strings.ReplaceAll("-"+v, "]", "["), "[")
		ip := make([]string, 0, len(parts))
		hs := make([]string, 0, len(parts))
		for i, s := range parts {
			if i%2 == 0 {	// ip
				ip = append(ip, s)
			} else {
				hs = append(hs, s)
			}
		}
		_ip := Ip{ip: strings.Join(ip, "|")[1:], hs: strings.Join(hs, "|")}
		iplist = append(iplist, _ip)
	}

	return iplist
}

func (i Ip)supportsTLS() bool {
	if hasAbba(i.ip) && !hasAbba(i.hs) {
		return true
	}
	return false
}

func hasAbba(s string) bool {
	for i := 0; i < len(s)-4; i++ {
		if s[i] == s[i+3] && s[i+1] == s[i+2] && s[i] != s[i+1] {
			return true
		}
	}
	return false
}