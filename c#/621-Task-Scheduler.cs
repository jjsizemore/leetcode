#region Max Heap
/// <summary>
/// 621. Task Scheduler
/// https://leetcode.com/problems/task-scheduler/
/// You are given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
/// Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
/// However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
/// that is that there must be at least n units of time between any two same tasks.
/// Return the least number of units of times that the CPU will take to finish all the given tasks.
///
/// Example 1:
/// Input: tasks = ["A","A","A","B","B","B"], n = 2
/// Output: 8
/// Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
/// There is at least 2 units of time between any two same tasks.
///
/// Example 2:
/// Input: tasks = ["A","A","A","B","B","B"], n = 0
/// Output: 6
/// Explanation: A -> B -> A -> B -> A -> B
/// There is no cooldown between two same tasks.
///
/// Example 3:
/// Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
/// Output: 16
/// Explanation: A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
/// There is at least 2 units of time between any two same tasks.
///
/// Constraints:
/// 1 <= tasks.length <= 10^4
/// tasks[i] is uppercase English letter.
/// The integer n is in the range [0, 100].
/// </summary>
/// <remarks>
/// Time: O(NlogN)
/// Space: O(N)
/// </remarks>
public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        // queue will hold tasks and time that tasks are cooled
        // keep track of time, increment every time we run a task or are idle
        // PQ will hold frequencies and function as a max heap
        // tally freqs in a dict

        var nextWork = new PriorityQueue<int, int>();
        int time = 0;
        var cooldown = new Queue<(int freq, int aliveTime)>();
        var dict = new Dictionary<char, int>();

        foreach (var t in tasks) {
            dict[t] = dict.GetValueOrDefault(t, 0) + 1;
        }

        foreach (var freq in dict.Values) {
            nextWork.Enqueue(freq, -freq);
        }

        while (nextWork.Count > 0 || cooldown.Count > 0) {
            time++;
            // check cooldown and then process or wait
            if (cooldown.Count > 0 && cooldown.Peek().aliveTime == time) {
                var (freq, _) = cooldown.Dequeue();
                nextWork.Enqueue(freq, -freq);
            }

            if (nextWork.Count > 0) {
                var workFreq = nextWork.Dequeue();
                workFreq--;

                if (workFreq > 0) {
                    cooldown.Enqueue((workFreq, time + n + 1));
                }
            }
        }

        return time;
    }
}

#endregion