def float_within_error(x: float, answer: float, err: float) -> bool:
    return (answer - err) < x < (answer + err)
