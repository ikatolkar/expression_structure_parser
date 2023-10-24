# expression_structure_parser
Parses an expression in a predefined syntax and grammar into a structure and vice versa

# Requirements

## Functional Requirements
### FR 1
Given a statement/expression in a known syntax/grammar, parse it into a structure (json string)

### FR 2
Given a structure (json string) in a known schema, parse it into a statement/expression in a known syntax/grammar

### FR 3
Evaluation of the expression must be equal to evaluation of the structure


## Non Functional Requirements
### NFR 1

# Assumptions
### A1
New lines (carriage returns) don't mean anything, can be ignored

# Examples
## Example 1
### Input Expression
```
func1(func1(x1,'y1'), x1,p1,'dafad', func2(func2(c2, c3, a1 == b1 and (c1 == d1 and y1 == z1) or (e1 == f1 and g1 == 'a1 == b1 and (((((( (c1 == d1 and y1 == z1)' or (a1 == 'f1 and' g1 == h1) or (i1 == j1 and k1 == l1)')) or (i1==j1 and k1==l1)), d1, d2))
```
### Output JSON
```
{
  "data" : "func1",
  "type" : "function",
  "nodes": [
    {
      "data": "func1",
      "type": "function",
      "nodes": [
        {
          "data": "x1",
          "type": "field"
        },
        {
          "data": "y1",
          "type": "value"
        }
      ]
    },
    {
      "data": "x1",
      "type": "field"
    },
    {
      "data": "p1",
      "type": "field"
    },
    {
      "data": "dafad",
      "type": "value"
    },
    {
      "data": "func2",
      "type": "function",
      "nodes": [
        {
          "data": "func2",
          "type": "function"
        }
      ]
    }
  ]
  # And more.......
}
```
