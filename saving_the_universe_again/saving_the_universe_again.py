# Return min number of hacks (swap of adjacent instructions)
# in p so that total damage <= d.
# If impossible, return -1
def min_hacks(d, p):

	p_list = list(p)

	swap_possible = True
	current_damage = 0
	num_hacks = 0

	while swap_possible:
		# calculate current damage
		shoot_damage = 1
		current_damage = 0
		for c in p_list:
			if c == "S":
				current_damage += shoot_damage
			elif c == "C":
				shoot_damage = shoot_damage * 2

		if current_damage > d:
			# find highest "CS" pair and swap
			swap_possible = False
			for i in reversed(range(len(p_list)-1)):
				if p_list[i:i+2] == ["C", "S"]:
					# perform swap
					temp = p_list[i]
					p_list[i] = p[i+1]
					p_list[i+1] = temp
					# update number of hacks
					num_hacks += 1
					swap_possible = True
					break
			# if we didn't find a "CS" pair, then swap_possible remains False
			# and we break out of the while loop
		else:
			break

	if current_damage > d:
		return -1
	else:
		return num_hacks

num_cases = int(input())
for i in range(1, num_cases+1):
	current_case = input().split()
	d = int(current_case[0])
	p = current_case[1]
	solution = min_hacks(d, p)
	if solution < 0:
		solution_string = "IMPOSSIBLE"
	else:
		solution_string = str(solution)
	print("Case #{:d}: {:s}".format(i, solution_string))
	