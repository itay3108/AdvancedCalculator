import pytest

from Calculator import calculate
from inputHandeling.validateInput import validate_input


@pytest.mark.parametrize("invalid_expression", [
    "",
    "abfghjsdc",
    "           ",
    "(2 + 3) * 4)",
    "2 .. 3",
    "()",
    "2 ; 3",
    "- (2 + 3 * 4",
    "2^:7",
    ")2+3("
])
def test_validate_input_invalid(invalid_expression):
    """
    Testing invalid expressions using pytest
    :param invalid_expression: The expression
    :return: Clear if invalid
    """
    with pytest.raises(SyntaxError):
        validate_input(invalid_expression)


@pytest.mark.parametrize("expression, expected_result", [
    ("2 + 3", 5),
    ("(2 + 3) * 4", 20),
    ("2.5 + 3.7", 6.2),
    ("2 + 3 / (4 - 5)", -1),
    ("-2 + 3", 1),
    ("3 / 3 ^ 2", 0.33333333333333333),
    ("~ (2 + 3) * 4", -20),
    ("2 @ 4", 3),
    ("2.5 * 3 $ 1.12", 7.5),
    ("-2 + 3 * (4 - -5)", 25),
    ("123#", 6),
    ("- 2 @ 3 * -4", 10),
    ("- 2 & -3 * -4", -12),
    ("2 + 3!", 8),
    ("2 $ 3", 3),

    ("(2+3+7+8)*2-4/2+5+10-7", 46.0),
    ("20-32-4+6/2-1+15-10+3", -6),
    ("432*5*6/3*71-4+6-634", 306088),
    ("18/2/3+42-5-10*4+3-4!", -21.0),
    ("2^3+4-6/2+1^2+5-3+2-1", 13.0),
    ("20%3+42-5+0.5*14-10+2", 38.0),
    ("(3!+4-2*3+10/2-6+3-1)^2", 25.0),
    ("(2@3)+45-6.5+(7-3)*2", 49.0),
    ("(2$8)*4+5$(78/2)#-1+32", 75),
    ("3+4&5&6-7+8-2/4+3-(4*82)#", -2.5),
    ("(2+3)*4-~6+7-8+10-9/3*20", -25),
    ("20*32#-5+9999#+6-7/2+8", 141.5),
    ("20*32-5+--9!+6-22&50/5", 363516.6),
    ("57.82*15+~3%4^5$~23^2", 868.3),
    ("(500-10*5^2/--0.5)/52!^0.2", 0),
    ("52!/83^(4@5+65)-12&(7-3--8.5)", -12),
    ("2!^~(0.5*82&12%5+(51-28)@2)*82^3", 47.59229147085747),
    ("83^3&0+52.72*21%10@2-(87##!+30)", -590.84),
    ("(83^3)&0@(52.7221%10)@2-(42^3!)&0@2-(87##!+30)", -749.319475),
    ("~--(((-(-3-(456*12^2.5)*4@6)---615#)$534%12)---803#+18!@12)", -3201186852863996.0),

])
def test_evalExpression(expression, expected_result):
    """
    Testing valid expressions using pytest
    :param expression: The expression
    :param expected_result: The Outcome expected from the calculation of the expression
    :return: Clear if the calculation was correct
    """

    assert calculate(expression) == expected_result
