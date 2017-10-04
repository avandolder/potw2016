# POTW 2016 - Week 16 Gerrymandering

import sys

def main(args):
    # Get the number of districts and votes from the same line of input.
    num_districts, num_votes = [int(x) for x in input().split(' ')]

    # Make lists for the winner and counter of each district, as well as every
    # candidate that may have won a district.
    district_winner = ["" for x in range(num_districts)]
    district_counter = [0 for x in range(num_districts)]
    candidates = []

    # The following for loop is essentially an implementation of the Boyer–Moore
    # majority vote algorithm.
    for i in range(num_votes):
        # Loop for the number of votes, getting the candidate the vote was for
        # and the district it was in.
        candidate, district = input().split(' ')
        district = int(district)

        if district_counter[district] == 0:
            # If the district counter has reached zero, set the new current
            # winning candidate.
            district_winner[district] = candidate

            # Add them to the list of candidates that may have won a district
            # as well.
            if candidate not in candidates:
                candidates.append(candidate)

        elif district_winner[district] == candidate:
            district_counter[district] += 1
        else:
            district_counter[district] -= 1

    # Now, determine who the winner of the election was.
    winner_name = ""
    winner_districts = 0
    for c in candidates:
        # Find the number of districts won by candidate c by counting how many
        # times c appeared in the district_winner list.
        districts_won_by_c = district_winner.count(c)

        # If c won more then the current top district winner, make him into
        # the top district winner.
        if districts_won_by_c > winner_districts:
            winner_name = c
            winner_districts = districts_won_by_c

    print(winner_name)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
