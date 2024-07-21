from pathlib import Path
import              re


# ------------------- #
# -- REGEX TACTICS -- #
# ------------------- #

SHORT_POWER_PATTERN = re.compile(r'([a-zA-Z]+)(\d+)')

def short_power_match(match):
    x = match.group(1)
    p = match.group(2)

    if x == 'S':
        return f"S_{{{p}}} "

    return f"{x}^{{{p}}} "


# ----------- #
# -- TOOLS -- #
# ----------- #

def std_math(formula):
    for pattern, replace_match in [
        (SHORT_POWER_PATTERN, short_power_match),
    ]:
        formula = re.sub(pattern, replace_match, formula)

    return formula

if __name__ == "__main__":
    for formula in [
        "a2 + b2 + 2ab",
        "b2 + a2 + 2ab",
        "2ab + b2 + a2",
        "b257 - 4ac",
        "S4",
    ]:
        std_formula = std_math(formula)

        print(
            '---',
            formula,
            std_formula,
            sep = "\n"
        )
