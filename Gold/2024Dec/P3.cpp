#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

struct Job {
    long long deadline;
    long long duration;
};

void addJob(std::vector<Job>& jobs, long long start_time, long long process_time) {
    jobs.push_back({start_time + process_time, process_time});
}

int calculateMaxJobs(const std::vector<Job>& jobs) {
    auto sorted_jobs = jobs;
    std::sort(sorted_jobs.begin(), sorted_jobs.end(), 
        [](const Job& x, const Job& y) { 
            return x.deadline < y.deadline; 
        });
    
    long long current_time = 0;
    std::priority_queue<long long> scheduled_durations;
    
    for (const auto& job : sorted_jobs) {
        current_time += job.duration;
        scheduled_durations.push(job.duration);
        
        if (current_time > job.deadline) {
            current_time -= scheduled_durations.top();
            scheduled_durations.pop();
        }
    }
    
    return scheduled_durations.size();
}

std::vector<Job> readTestCase() {
    std::vector<Job> jobs;
    int job_count;
    std::cin >> job_count;
    
    for(int i = 0; i < job_count; i++) {
        long long start_time, process_time;
        std::cin >> start_time >> process_time;
        addJob(jobs, start_time, process_time);
    }
    
    return jobs;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int test_cases;
    std::cin >> test_cases;
    
    while(test_cases--) {
        auto jobs = readTestCase();
        std::cout << calculateMaxJobs(jobs) << '\n';
    }
    
    return 0;
}
