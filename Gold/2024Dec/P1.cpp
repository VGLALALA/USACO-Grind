#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int calculate_groups(const vector<int>& index_list, int max_distance) {
    int group_count = 1;
    int last_position = index_list[0];
    for (size_t i = 1; i < index_list.size(); ++i) {
        if (index_list[i] - last_position > max_distance) {
            group_count++;
            last_position = index_list[i];
        }
    }
    return group_count;
}

void process_label(const vector<int>& index_list, vector<int>& group_results, int total_cows) {
    int current_distance = total_cows;
    while (current_distance > 0) {
        int previous_distance = current_distance;
        int groups = calculate_groups(index_list, current_distance);

        int low = 1, high = current_distance;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (calculate_groups(index_list, mid) == groups) {
                previous_distance = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        group_results[previous_distance] += groups;
        group_results[current_distance + 1] -= groups;

        current_distance = previous_distance - 1;
    }
}

void thing() {
    const int max_cows = static_cast<int>(1.01e6);
    int total_cows;
    cin >> total_cows;
    vector<int> cow_labels(total_cows + 1);
    for (int i = 1; i <= total_cows; ++i) {
        cin >> cow_labels[i];
    }
    vector<int> group_results(total_cows + 2, 0);
    vector<vector<int>> cow_positions(max_cows);

    for (int cow_index = 1; cow_index <= total_cows; ++cow_index) {
        cow_positions[cow_labels[cow_index]].push_back(cow_index);
    }

    for (const auto& positions : cow_positions) {
        if (!positions.empty()) {
            process_label(positions, group_results, total_cows);
        }
    }

    int current_groups = 0;
    for (int i = 1; i <= total_cows; ++i) {
        current_groups += group_results[i];
        cout << current_groups << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    thing();
    return 0;
}
