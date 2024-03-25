# Suppose a company has marked n strings that are prohibited in reviews. They assign a score to each review that denotes how well it follows the 
# guidlines. The score of a review is defined as the longest contingous substring of the review which does not contain anty string among the list of n 
# prohibited strings. A string contains a prohibited word if it has a contingous substring that matches a word from the prohibited list. 

# Given a review and a list of prohibited strings, calculate the review score.

def findReviewScore(review, prohibited_words):
     
     def containsProhibited(substring, prohibited_words):
         """ Checks if the substring contains forbidden word """
         for word in prohibited_words:
             if word in substring:
                 return True
             else:
                 return False
         
     max_length = 0
     
     for i in range(len(review)): # iterates through teh string
         for j in range(i + 1, len(review) + 1): # iterates through indices of the string
             substring = review[i:j]
             if not containsProhibited(substring, prohibited_words):
                 max_length = max(max_length, len(substring))
    
     return max_length
        
review = "GoodProductButScrapAfterWash"
prohibited_words = ["crap", "odpro"]

score = findReviewScore(review, prohibited_words)
print(score)