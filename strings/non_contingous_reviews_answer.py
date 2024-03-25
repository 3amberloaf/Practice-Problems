# Suppose a company has marked n strings that are prohibited in reviews. They assign a score to each review that denotes how well it follows the 
# guidlines. The score of a review is defined as the longest contingous substring of the review which does not contain anty string among the list of n 
# prohibited strings. A string contains a prohibited word if it has a contingous substring that matches a word from the prohibited list. 

# Given a review and a list of prohibited strings, calculate the review score.

# Checks the words that are NON-CONTINGOUS

def find_longest_substring_without_prohibited_subsequences(review, prohibited_words):
    def is_subsequence(s, sub):
        sub_iter = iter(sub)
        return all(char in sub_iter for char in s)
    
    n = len(review)
    longest = 0
    longest_substring = ""
    
    for start in range(n):
        for end in range(n, start + longest, -1):  # Decrease end, start from n to start+longest
            substring = review[start:end]
            if any(is_subsequence(word, substring) for word in prohibited_words):
                continue  # Skip to the next substring if any prohibited word is a subsequence
            if len(substring) > longest:
                longest = len(substring)
                longest_substring = substring
                break  # Found a longer valid substring, no need to check shorter ones
    
    return longest, longest_substring

# Example usage
review = "GoodProductButScrapAfterWash"
prohibited_words = ["crap", "odpro"]

score, longest_valid_substring = find_longest_substring_without_prohibited_subsequences(review, prohibited_words)
print(f"Score: {score}, Longest Valid Substring: '{longest_valid_substring}'")
