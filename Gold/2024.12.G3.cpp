#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

class Job {
public:
	Job(long long start_time, long long process_time)
	: deadline_(start_time + process_time)
	, duration_(process_time) {}
	
	long long getDeadline() const { return deadline_; }
	long long getDuration() const { return duration_; }
	
private:
	long long deadline_;
	long long duration_;
};

class JobScheduler {
public:
	void addJob(long long start_time, long long process_time) {
		jobs_.emplace_back(start_time, process_time);
	}
	
	int calculateMaxJobs() const {
		auto sorted_jobs = jobs_;
		std::sort(sorted_jobs.begin(), sorted_jobs.end(), 
			[](const Job& x, const Job& y) { 
				return x.getDeadline() < y.getDeadline(); 
			});
		
		long long current_time = 0;
		std::priority_queue<long long> scheduled_durations;
		
		for (const auto& job : sorted_jobs) {
			current_time += job.getDuration();
			scheduled_durations.push(job.getDuration());
			
			if (current_time > job.getDeadline()) {
				current_time -= scheduled_durations.top();
				scheduled_durations.pop();
			}
		}
		
		return scheduled_durations.size();
	}
	
	void clear() {
		jobs_.clear();
	}
	
private:
	std::vector<Job> jobs_;
};

// I/O handling functions
JobScheduler readTestCase() {
	JobScheduler scheduler;
	int job_count;
	std::cin >> job_count;
	
	for(int i = 0; i < job_count; i++) {
		long long start_time, process_time;
		std::cin >> start_time >> process_time;
		scheduler.addJob(start_time, process_time);
	}
	
	return scheduler;
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	
	int test_cases;
	std::cin >> test_cases;
	
	while(test_cases--) {
		auto scheduler = readTestCase();
		std::cout << scheduler.calculateMaxJobs() << '\n';
	}
	
	return 0;
}
