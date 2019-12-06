# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def get_classrooms_count(time_intervals):

	class_rooms = {}
	count = 0

	for interval in time_intervals:
		start, end = interval[0], interval[1]

		room_count = len(class_rooms)
		room_found = False
		for room in class_rooms:
			this_room_available = True
			booked_intervals = class_rooms[room]
			for booked_interval in booked_intervals:
				booked_start, booked_end = booked_interval[0], booked_interval[1]
				if (booked_start <= start <= booked_end) or (booked_start <= end <= booked_end):
					this_room_available = False
					break

			if this_room_available:
				room_count = room
				room_found = True
				break

		if not room_found:
			class_rooms[room_count] = []
		class_rooms[room_count].append((start, end))

	return len(class_rooms)

def get_classrooms_count_optimized(time_intervals):
	start_times = [ start for start, end in time_intervals ]
	end_times = [ end for start, end in time_intervals ]

	start_times.sort()
	end_times.sort()

	n = len(time_intervals)
	current_room_count = 0
	max_room_count = 0
	i = 0
	j = 0

	while i < n and j < n:
		if start_times[i] < end_times[j]:
			current_room_count += 1
			i += 1

			if current_room_count > max_room_count:
				max_room_count = current_room_count
		else:
			current_room_count -= 1
			j += 1

	return max_room_count


assert get_classrooms_count([(30, 75), (0, 50), (60, 150)]) == 2
assert get_classrooms_count([(30, 75), (0, 50), (80, 150), (60, 70)]) == 2
assert get_classrooms_count([(30, 75), (0, 50), (75, 150), (60, 70)]) == 2
assert get_classrooms_count([(30, 45), (75, 150), (60, 70)]) == 1
assert get_classrooms_count([(30, 75), (0, 50), (45, 150), (40, 70)]) == 4

assert get_classrooms_count_optimized([(30, 75), (0, 50), (60, 150)]) == 2
assert get_classrooms_count_optimized([(30, 75), (0, 50), (80, 150), (60, 70)]) == 2
assert get_classrooms_count_optimized([(30, 75), (0, 50), (75, 150), (60, 70)]) == 2
assert get_classrooms_count_optimized([(30, 45), (75, 150), (60, 70)]) == 1
assert get_classrooms_count_optimized([(30, 75), (0, 50), (45, 150), (40, 70)]) == 4