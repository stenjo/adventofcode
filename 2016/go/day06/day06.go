package day06

func GetErrorCorrected(strList []string) string {

	return ""
}

func transpose(s []string) []string {

	t := make([]string, len(s))
	for i := 0; i < len(t); i++ {
		for j, v := range s[i] {
			t[i] = t[i] + string(v)
		}
	}
	return t
}