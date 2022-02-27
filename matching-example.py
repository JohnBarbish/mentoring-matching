import pulp
import numpy as np
# make my own integer problem example. Let's start with solving the compatibility between 2 mentors and 3 mentees (ficticious)
mentors = "A B".split()
mentees = "a b c".split()
max_mentees = [1, 2]
mmd = dict(zip(mentors, max_mentees))
compatibility_matrix = np.array([[1, 0, 0.75],
                        [0.5, 0.5, 1]])
def compatibility(pair):
    (mentor_i, mentee_j) = pair
    mentor_ind = mentors.index(mentor_i)
    mentee_ind = mentees.index(mentee_j)
    return compatibility_matrix[mentor_ind, mentee_ind]

# define all possible pairs
possible_pairs = [tuple(c) for c in pulp.itertools.product(mentors, mentees)]

# create a binary decision variable to say whether or not a pair is in use or not
x = pulp.LpVariable.dicts(
    "pair", possible_pairs, lowBound=0, upBound=1, cat=pulp.LpInteger
)

# set up problem
matching_model = pulp.LpProblem("Mentor-Mentee-Matching-Model", pulp.LpMaximize)
# want it to maximize the overall compatibility of all mentors and mentees
matching_model += pulp.lpSum([compatibility(pair)*x[pair] for pair in possible_pairs])

# specify that each mentee can only be paired once
for mentee in mentees:
    matching_model += (
        pulp.lpSum(x[pair] for pair in possible_pairs if mentee in pair) == 1, 
        "Mentee_%s_constraint" % mentee,
    )

# specify the maximum number of mentees for each mentor
for mentor in mentors:
    matching_model += (
        pulp.lpSum(x[pair] for pair in possible_pairs if mentor in pair) <= mmd[mentor],
        "Mentor_%s_max_mentees" % mentor,
    )
    matching_model += (
        pulp.lpSum(x[pair] for pair in possible_pairs if mentor in pair) >= 1,
        "Mentor_%s_min_mentees" % mentor,
    )

matching_model.solve()

print("The choosen pairs are out of a total of %s:" % len(possible_pairs))
for pair in possible_pairs:
    if x[pair].value() == 1.0:
        print(pair)