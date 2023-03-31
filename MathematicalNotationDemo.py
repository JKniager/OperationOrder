import argparse
from fix_format_demonstration import fix_format_readers


def main():
    calculation_function_lookup = {
        "infix" : fix_format_readers.calculate_infix,
        "prefix" : fix_format_readers.calculate_prefix,
        "postfix" : fix_format_readers.calculate_postfix
    }

    parser = argparse.ArgumentParser(
        prog="MathematicalNotationDemo",
        description="Takes in a mathematical expression as a string and computes the result.\nCan be set to parse expressions written in different notations."
    )

    parser.add_argument("equation",
                        type=str,
                        help="The expression you want calculated.  Note: Put spaces (or whatever you set the --separator to) between the parentheses for infix notation."
    )
    parser.add_argument("-N", "--notation",
                        choices=calculation_function_lookup.keys(),
                        default="infix",
                        type=str.lower,
                        help="The type of notation the expression is written in."
    )
    parser.add_argument("-S", "--separator",
                        default=" ",
                        type=str,
                        help="The string that separates the parts of the expression.  Default is space."
    )

    args = parser.parse_args()

    try:
        print(f"{args.equation} = {calculation_function_lookup[args.notation](args.equation, args.separator)}")
    except fix_format_readers.InvalidInfixExpressionError as error:
        print(f"{args.equation} is misformatted as an infix expression.  Is there a typo or did you mean to use a different format?")
    except fix_format_readers.InvalidPostfixExpressionError as error:
        print(f"{args.equation} is misformatted as a postfix expression.  Is there a typo or did you mean to use a different format?")
    except fix_format_readers.InvalidPrefixExpressionError as error:
        print(f"{args.equation} is misformatted as a prefix expression.  Is there a typo or did you mean to use a different format?")


if __name__ == '__main__':
    main()
