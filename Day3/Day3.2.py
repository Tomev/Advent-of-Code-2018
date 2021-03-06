from Day3.Claim import Claim

file_read = open("input.txt", "r")

line = file_read.readline()
claims = []

# Parse claims
while line:
    claims.append(Claim(line))
    line = file_read.readline()

sq_inches_already_claimed = set()
sq_inches_claimed_multiple_times = set()

print('Generating list of sq inches that were multiply claimed...')
for i in range(0, len(claims)):

    print(f'Processing claim {i}.')

    sq_inches_claimed = claims[i].list_of_occupied_sq_inches()

    for sq_inch in sq_inches_claimed:
        if sq_inches_already_claimed.__contains__(sq_inch):
            sq_inches_claimed_multiple_times.add(sq_inch)

    sq_inches_already_claimed = sq_inches_already_claimed | set(sq_inches_claimed)

non_invasive_id = -1

print('Looking for claim which pixels had been used only once...')
for i in range(0, len(claims)):

    print(f'Processing claim {i}.')

    non_invasive_id = i + 1

    sq_inches_claimed = claims[i].list_of_occupied_sq_inches()

    for sq_inch in sq_inches_claimed:
        if sq_inches_claimed_multiple_times.__contains__(sq_inch):
            non_invasive_id = -1
            break

    if non_invasive_id != -1:
        break

print(f'Non invasive id = {non_invasive_id}.')
