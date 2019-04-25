import sys


class Solution:
    # Write your code here
    stack_obj = []
    stack_index = 0

    queue_obj = []
    queue_index = 0

    def pushCharacter(self, data):
        self.stack_obj.append(data)
        self.stack_index += 1

    def enqueueCharacter(self, data):
        self.queue_obj.append(data)

    def popCharacter(self):
        obj = self.stack_obj[self.stack_index-1]
        self.stack_index -= 1
        return obj

    def dequeueCharacter(self):
        obj = self.queue_obj[self.queue_index]
        self.queue_index += 1
        return obj


# read the string s
s = 'racecar'

# Create the Solution class object
obj = Solution()

l = len(s)

# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
print(obj.stack_index)
print(obj.queue_obj)

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
