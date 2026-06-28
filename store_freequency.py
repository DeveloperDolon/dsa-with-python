
# store freequeency in dict

nums = [1, 2, 3, 4, 5, 1, 2, 3];

# basic method TC -> O(N) / SC -> O(N)
def storeFrequency(nums):
    freequency = {};
    for num in nums: 
        if num in freequency:
            freequency[num] += 1;
        else: 
            freequency[num] = 1;
    return freequency;


# advance method TC -> O(N) / SC -> O(N)
def storeFrequencyAdvance(nums):
    freequency = {};
    for num in nums: 
        freequency[num] = freequency.get(num, 0) + 1;
    return freequency;

print("Freequencs: ", storeFrequency(nums));
print("Freequencs Advance: ", storeFrequencyAdvance(nums));
