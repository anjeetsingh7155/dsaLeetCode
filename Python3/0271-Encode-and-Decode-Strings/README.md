# Encode and Decode Strings

Problem link: [GeeksforGeeks - Encode and Decode Strings](https://www.geeksforgeeks.org/problems/encode-and-decode-strings/1)

Difficulty: Medium

## Problem

We are given a list of strings. We need to:
1. **Encode** the list into a single string.
2. **Decode** that single string back into the original list of strings.

The tricky part is that strings can contain any characters (including spaces or special symbols), so we need a safe way to know where one string ends and the next begins.

## Approach

The idea is to store the **length of each string** before the string itself. This way, while decoding, we always know exactly how many characters to read for each word, no matter what characters it contains.

**Encoding rule:**
```
length + "/:" + actual string
```

**Example:**
```
"Hello" → "5/:Hello"
"World" → "5/:World"
```

**Encoded string:**
```
5/:Hello5/:World
```

While decoding, we read the number before `"/:"` to know the length of the next string, then extract exactly that many characters after `"/:"`. We repeat this until the whole string is processed.

## Code

```python
class Solution:
    def encode(self, arr):
        res = ""
        for s in arr:
            res += str(len(s)) + "/:" + s
        return res

    def decode(self, s):
        res = []
        ptr = 0
        while ptr < len(s):
            j = s.index("/:", ptr)
            length = int(s[ptr:j])
            res.append(s[j + 2:j + 2 + length])
            ptr = j + 2 + length
        return res
```

## Example

**Example 1:**
```
Input: ["Hello", "World"]

Encoded:
5/:Hello5/:World

Decoded:
["Hello", "World"]
```

**Example 2:**
```
Input: ["abc", "!@"]

Encoded:
3/:abc2/:!@

Decoded:
["abc", "!@"]
```

## Complexity

Time: O(n)
Space: O(n)

## Key Idea

Storing the length before `"/:"` tells us exactly how many characters belong to the current string. This way, even if the string contains special characters or digits, decoding stays accurate because we never guess where a string ends — we always know from its stored length.