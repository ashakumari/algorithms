# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def find_number_of_decoding(input_string)
	str_len = input_string.length
	if str_len == 1
		return 1
	end

	counter_arr = Array.new(str_len, 0)
	counter_arr[0] = 1
	i = 1

	while i < str_len
		counter_arr[i] = 0
		current_char = input_string[i]
		if current_char > '0'
			counter_arr[i] = counter_arr[i-1]
		end
		prev_char = input_string[i-1]
		if (prev_char == '1' or (prev_char == '2' && current_char < '7'))
			if counter_arr[i-2] == 0
				counter_arr[i] += 1
			else
				counter_arr[i] += counter_arr[i-2]
			end 
		end
		i += 1
	end
	return counter_arr[str_len-1]
end

test_data = {
	'0' => {
		'input_string' => '1234',
		'expected_result' => 3
	},
	'1' => {
		'input_string' => '111',
		'expected_result' => 3
	},
	'2' => {
		'input_string' => '121',
		'expected_result' => 3
	},
	'3' => {
		'input_string' => '1218213',
		'expected_result' => 15
	},
	'4' => {
		'input_string' => '1210213',
		'expected_result' => 6
	}

}


test_data.each do |test_no, dataset|
	puts find_number_of_decoding(dataset['input_string']) == dataset['expected_result']
end 