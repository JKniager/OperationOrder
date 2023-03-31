# Demonstration and Explanation of Different Expression Notation

| Table of Contents |
| ----------------- |
| [Introduction](#introduction-how-humans-write-expressions)|
| [A Little History](#a-little-history-jan-łukasiewicz) |
| [Prefix Notation](#prefix-notation) |
| [Postfix Notation](#postfix-notation) |
| [Running the Demo](#running-the-demo) |

## Introduction: How Humans Write Expressions

We all know how you write a mathematical expressions.  We learned to do it in arithmetic class as kids.

2 \+ 2 = 4

We eventually learned the order of operations, and how parentheses can override that order.

**Example 1:**

```pseudo
4 * 5 + 3 ^ 2 =
4 * 5 + 9 =
20 + 9 =
29
```

**Example 2:**

```pseudo
4 * ( 5 + 3 ) ^ 2 =
4 * 8 ^ 2 =
4 * 64 =
256
```

This way of writing expressions is called *infix notation*.
For us, this becomes second nature as we practice.

But you aren't in math class right now, you're on GitHub, which means you're programming computers (or starting to learn about programming).
How does this way of writing equations look to a computer?
In code, it's pretty much the same, but what if it was a string input that needed to be parsed?

This becomes a little more complicated.  On top of programming the difference between numbers and operators, you also have to program order of operations and the parentheses exceptions.

What if there was a way to represent expressions that would be easier for a computer program to parse?

It turns out there are two other ways!

## A little history: Jan Łukasiewicz

Jan Łukasiewicz was a Polish logician and philosopher.  In 1924 he decided to try to come up with a new way of writing mathematical and logical expressions without the use of parentheses.
Today we call his method of writing expressions *Polish notation* (after his nationality) or *prefix notation*.

Here is an example of "2 \+ 2" written in prefix notation:

\+ 2 2 = 4

## Prefix Notation

Looking at our earlier examples which needed to use parentheses to make exceptions to the order of operations, let us now rewrite them in prefix notation.

**Example 1:**

4 \* 5 \+ 3 ^ 2 becomes:

```pseudo
+ ^ 3 2 * 4 5 =
+ 9 * 4 5 =
+ 9 20 =
29
```

**Example 2:**

4 \* ( 5 \+ 3 ) ^ 2 becomes:

```pseudo
* 4 ^ + 5 3 2 =
* 4 ^ 8 2 =
* 4 64 =
256
```

A way to describe the idea behind this notation is, "I tell you what operation I want you to perform, and then I give you the resources I want you to perform that operation on."
Let's walk through Example 1 to better explain this.

We start with:

`+ ^ 3 2 * 4 5`

First we have the "\+" operator.  The two operands after it are "^" and "3".
Since "^" is an operator, this indicates to us that before the addition can be performed, we first must perform the exponential operation.

So, we look at the operands after "^", and we see "3" and "2".

Rearranging these into infix notation, this means that we must perform the operation "3^2", which gives us "9".

Our expression becomes:

`+ 9 * 4 5`

With the "^" operator taken care of, we can now go back to our "\+" and see what the new operands are.

Now we have a "9" from the result of "^" and a "\*" operator.

Just like before, we need to perform the multiplication before the addition.

The operands for "\*" are "4" and "5", which gives us "4*5" resulting in "20".

Our expression becomes:

`+ 9 20`

Looking at the "\+" we see its operands have become "9" and "20".

Finally, we can perform the addition!  We get "9+20" resulting in "29".

So our final result is:

`29`

Note that, technically, we could have done the multiplication before the exponential and still gotten the same result.
In infix notation, that isn't necessarily clear, which is why we have order of operations, but in prefix notation, if an operator has two operands after it, then you can perform the operation without changing the final result.

Another way to look at prefix notation is as a tree. Let's look again at Example 1:

`+ ^ 3 2 * 4 5`

If we reformat this into a tree, we can see the hierarchy of the expression.

```diagram
+
|- ^
||- 3
||- 2
|- *
||- 4
||- 5
```

Now, what if we were to rewrite this like so:

```python
add(
    power(
        3,
        2
    ),
    multiply(
        4,
        5
    )
)
```

As you can see from the pseudo-code above, many of the programming languages you learn already use prefix notation.
This notation isn't exclusive to mathematics.  As stated above, it simply means "Give the operator, and then give its operands."

One of the reasons this notation is used is because of how easily it can be turned into a tree.
This allows compilers to turn written code into abstract syntax trees for checking and processing.

## Postfix Notation

I mentioned that there are two ways to format expressions without using parentheses.
We've already covered prefix notation, so now let's cover *postfix notation*, a.k.a *Reverse Polish notation*.

Unlike prefix notation, where the operator comes before the operands, postfix notation puts the operator after the operands.

2 2 + = 4

Here are our examples written in postfix notation.

**Example 1:**

4 \* 5 \+ 3 ^ 2 becomes:

```pseudo
3 2 ^ 4 5 * + =
9 4 5 * + =
9 20 + =
29
```

**Example 2:**

4 \* ( 5 \+ 3 ) ^ 2 becomes:

```pseudo
4 5 3 + 2 ^ * =
5 8 2 ^ * =
5 64 * =
256
```

Postfix notation is even simpler to calculate than prefix notation.  You simply perform the operations from left to right using the operands to the left of each operator.

Another way to describe this format would be, "I give you resources and when I want you to do something with them, I give you the operation to perform."

Because of this, postfix notation can be calculated using a stack.

a)

```pseudo
Equation: 3 2 ^ 4 5 * +
Stack:
```

b)

```pseudo
Equation: 2 ^ 4 5 * +
Stack: 3
```

c)

```pseudo
Equation: ^ 4 5 * +
Stack: 3 2
```

d)

```pseudo
Equation: 4 5 * +
Stack: 9
```

e)

```pseudo
Equation: 5 * +
Stack: 9 4
```

f)

```pseudo
Equation: * +
Stack: 9 4 5
```

g)

```pseudo
Equation: +
Stack: 9 20
```

g)

```pseudo
Equation:
Stack: 29
```

Postfix notation is often used for stack based programming languages.

## Running the Demo

Included in this repository is a python program to demonstrate parsing the different notations in code.

To use it, type the following:

```powershell
python MathematicalNotationDemo.py "2 + 2"
2 + 2 = 4.0
```

As you can see, it defaults to infix notation.

For prefix notation, type:

```powershell
python MathematicalNotationDemo.py "+ 2 2" --notation="prefix"
+ 2 2 = 4.0
```

for postfix notation, type:

```powershell
python MathematicalNotationDemo.py "2 2 +" --notation="postfix"
2 2 + = 4.0
```
