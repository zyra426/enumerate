from complete_main import find_and_replace

run_cases = [
    (
        [
            "I know the man you speak of. Kladin is his name", 
            "Hello. My name is Kladin", 
            "Kaladin is so cool!"
        ], ["lines checked: 3, errors found and corrected: 2"],
     )
]

submit_cases = run_cases + [
   (
        [
            "Kladin never backs down, even when everyone else has already given up.",
            "If he's smiling, I'd be more worried than if he were drawing his blade.",
            "I owe Kladin my life, though he'd probably insist it was nothing.",
            "Don't mistake Kaladin's silence for weakness—he notices everything.",
            "The day Kladin walked into town, the whole place seemed to hold its breath.",
            "You can trust Kaladin with your secrets, but don't expect him to share his own.",
        ], ["lines checked: 3, errors found and corrected: 2", "lines checked: 6, errors found and corrected: 3"]
    ) 
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    result = find_and_replace(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
