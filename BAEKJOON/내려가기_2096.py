import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
dpMax = [*MIS()]
dpMin = [dpMax[0], dpMax[1], dpMax[2]]
for n in range(1, N):
	arr = [*MIS()]
	tmpMax = [dpMax[0], dpMax[1], dpMax[2]]
	tmpMin = [dpMin[0], dpMin[1], dpMin[2]]
	dpMax[0] = max(tmpMax[0], tmpMax[1]) + arr[0]
	dpMax[1] = max(tmpMax[0], tmpMax[1], tmpMax[2]) + arr[1]
	dpMax[2] = max(tmpMax[1], tmpMax[2]) + arr[2]
	
	dpMin[0] = min(tmpMin[0], tmpMin[1]) + arr[0]
	dpMin[1] = min(tmpMin[0], tmpMin[1], tmpMin[2]) + arr[1]
	dpMin[2] = min(tmpMin[1], tmpMin[2]) + arr[2]
print(max(dpMax), min(dpMin))