def main():
	string = input()  # 전체 문자열
	bomb = input()  # 폭발 문자열

	lastChar = bomb[-1]  # 폭발 문자열의 마지막 글자
	stack = []
	length = len(bomb)  # 폭발 문자열의 길이

	'''
	폭발 문자열의 마지막 문자열인지만 확인하고 
	폭발 문자열의 길이만큼 스택에서 확인 
	폭발 문자열이 완성되면 delete
	'''
	for char in string:
		stack.append(char)
		if char == lastChar and ''.join(stack[-length:]) == bomb:
			del stack[-length:]

	answer = ''.join(stack)

	if answer == '':
		print("FRULA")
	else:
		print(answer)


if __name__ == '__main__':
	main()
