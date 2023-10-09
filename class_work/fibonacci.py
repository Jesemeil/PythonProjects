def fibonacci(limit):
    terms = [0, 1]
    while True:
        next_term = terms[-1] + terms[-2]
        if next_term <= limit:
            terms.append(next_term)
        else:
            break
    return terms


result = fibonacci(60)
print(result)
