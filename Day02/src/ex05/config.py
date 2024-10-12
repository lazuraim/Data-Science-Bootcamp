num_of_steps = 3
filepath = 'data.csv'
template = "Report\n\n\
We have made {total} observations from tossing a coin: \
{tails} of them were tails and {heads} of them were heads.\n\
The probabilities are {tail_percent}% and {head_percent}%, respectively.\n\
Our forecast is that in the next {steps} observations we will have: \
{count_tails} tail and {count_heads} heads."