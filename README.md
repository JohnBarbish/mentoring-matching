# mentoring-matching
Contains an example of how to match mentees to mentors based on some responses from survey.

This particular example is based on how to help match mechanical engineering graduate student as mentors and mentees. Incoming graduate students are mentees, while senior graduate students serve as mentors.

This following procedure is followed for matching mentors and mentees:
  1. The included excel file is an example of the output from a survey gathering mentor and mentee data.
  2. This data is then loaded into python with pandas dataframes as mentors and mentees.
  3. An research compatibility matrix relating each mentor and mentee based on how much research interests overlap.
  4. Using pulp, a linear problem is defined and set up in order to maximize the compatibility score of the mentors and mentees, while also respecting limits set by the mentors or mentees. For example, each mentor can only have one or two mentees.
  5. Lastly, the linear problem is resolved with additional mentor and mentee preferences incorporated.
  6. The linear problems are solved, giving the mentor for each mentee.
