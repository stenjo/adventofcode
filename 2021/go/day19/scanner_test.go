package day19

import "testing"

func TestScanner_addBeacon(t *testing.T) {
	type args struct {
		pos xyz
	}
	tests := []struct {
		name string
		s    *Scanner
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.s.addSignal(tt.args.pos)
		})
	}
}

func TestScannerList_loadScanners(t *testing.T) {
	sl := ScannerList{}
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		sl   *ScannerList
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", &sl, args{str:loadtest("test1.txt")}, 5},
		{"2", &sl, args{str:loadtest("test2.txt")}, 5},
	}
	for _, tt := range tests {
		sl = ScannerList{}
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.sl.loadScanners(tt.args.str); got != tt.want {
				t.Errorf("ScannerList.loadScanners() = %v, want %v", got, tt.want)
			}
		})
	}
}
