// For this problem, in order to get all of the methods down to a O(1) time complexity, we have to combine daata structures
// A hashmap allows for O(1) reads and deletes, but doesn't have indices so it can't support getting a random
// A list has O(1) reads for getting a random, but deleting takes O(n) where n = Count - index of deleted elem
// We can map each value to its index inside the hashmap and use that to get indices for deletion from the list
// Then, we can swap the element with the last element in the list in order to make deletion O(1)
// Insertion is straightforward
// To implement getRandom we have to use a RNG

// Time Complexity
// GetRandom is always O(1). Insert and Remove are O(1) on average, but O(N) if they trigger a resize
// O(N) Space complexity for storing N elems

public class RandomizedSet {

    private List<int> _myList;
    private Dictionary<int, int> _myDict;
    private Random _myRand;

    public RandomizedSet() {
        this._myList = new List<int>();
        this._myDict = new Dictionary<int, int>();
        this._myRand = new Random();
    }

    public bool Insert(int val) {
        // If we do not already have the value, add it and return true
        if (!_myDict.ContainsKey(val))
        {
            _myDict.Add(val, _myList.Count);
            _myList.Add(val);
            return true;
        }
        return false;
    }

    public bool Remove(int val) {
        // If we have the value, remove it from both structures and return true
        if (_myDict.ContainsKey(val))
        {
            // Swap value with last value
            int lastVal = _myList[_myList.Count - 1];
            int idx = _myDict[val];

            _myList[idx] = lastVal;
            _myDict[lastVal] = idx;

            // Remove val from end of list and from dict
            _myList.RemoveAt(_myList.Count - 1);
            _myDict.Remove(val);
            return true;
        }
        return false;
    }

    public int GetRandom() {
        // Returns random int in range [0, _myList.Count)
        int idx = _myRand.Next(0, _myList.Count);
        return _myList[idx];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
