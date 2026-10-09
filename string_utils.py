#  Count the vowels in a string and return the count
def count_vowels_in_text(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
#Create tests for empty string, uppercase letters, and strings with no vowels.
def test_count_vowels():
    assert count_vowels_in_text("") == 0, "Test failed for empty string"
    assert count_vowels_in_text("AEIOU") == 5, "Test failed for uppercase letters"
    assert count_vowels_in_text("bcdfg") == 0, "Test failed for string with no vowels"
    assert count_vowels_in_text("Hello World") == 3, "Test failed for string with mixed case and spaces"
    assert count_vowels_in_text("Python Programming") == 4, "Test failed for string with multiple words"
    print("All tests passed!")
