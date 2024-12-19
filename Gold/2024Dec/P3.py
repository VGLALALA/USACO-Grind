def add_job(jobs, start_time, duration):
    jobs.append((start_time + duration, duration))

def find_max_jobs(jobs):
    sorted_jobs = sorted(jobs, key=lambda job: job[0])
    current_time = 0
    scheduled_durations = []

    for end_time, duration in sorted_jobs:
        current_time += duration
        scheduled_durations.append(duration)

        if current_time > end_time:
            max_duration = max(scheduled_durations)
            current_time -= max_duration
            scheduled_durations.remove(max_duration)

    return len(scheduled_durations)

def parse_test_case(input_lines, line_index):
    num_jobs = int(input_lines[line_index].strip())
    jobs = []
    for j in range(num_jobs):
        start_time, duration = map(int, input_lines[line_index + j + 1].strip().split())
        add_job(jobs, start_time, duration)
    return jobs, line_index + num_jobs + 1

def thing():
    import sys
    input = sys.stdin.read
    input_lines = input().splitlines()
    num_test_cases = int(input_lines[0].strip())
    line_index = 1

    results = []
    for _ in range(num_test_cases):
        jobs, line_index = parse_test_case(input_lines, line_index)
        results.append(find_max_jobs(jobs))

    for result in results:
        print(result)

thing()
