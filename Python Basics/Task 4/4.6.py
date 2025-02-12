def check_voter_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

age = int(input("Enter your age: "))
print(check_voter_eligibility(age))
