from datetime import datetime, timedelta


test_string = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'


def longest_call_number(phone_numbers):
    longest_number = ''

    longest_call = 0

    for phone_number, calls in phone_numbers.items():
        call_duration = sum(calls)
        if call_duration > longest_call:
            longest_call = call_duration

            longest_number = phone_number

    return longest_number

def into_cost(call_time):
    if call_time < 300:
        return call_time * 3
    else:
        addition = 0 if call_time % 60 == 0 else 1
        return ((call_time // 60) + addition) * 150


def solution(S):
    phone_numbers = dict()
    for row in S.split('\n'):
        call_time_string, phone_number = row.split(',')

        call_time = datetime.strptime(call_time_string, '%H:%M:%S')

        call_time_seconds = timedelta(hours=call_time.hour, minutes=call_time.minute, seconds=call_time.second).total_seconds()

        if phone_number in phone_numbers:
            phone_numbers[phone_number].append(call_time_seconds)
        else:
            phone_numbers[phone_number] = [call_time_seconds]
    phone_numbers_costs = dict()

    for phone_number, call_times in phone_numbers.items():
        cost = sum(map(into_cost, call_times))
        phone_numbers_costs[phone_number] = cost

    del phone_numbers_costs[longest_call_number(phone_numbers)]

    return sum(phone_numbers_costs.values())


print(solution(test_string))
