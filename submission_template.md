# AI Code Review Assignment (Python)

## Candidate
- Name:Gashaw Gedef
- Approximate time spent: 80 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- ` total / valid_count` line of code  divides `total` by total number of orders (`len(orders)` or `valid_count`) instead of count of non-cancelled orders which result in  wrong (too low) average value  whenever cancelled orders exist.

### Edge cases & risks
- Empty list when there is no orders and becomes `valid_count =0` which result in  `ZeroDivisionError`
- If all orders cancelled ,the function returns 0.0 but divides by positive total count result in misleading result or value

### Code quality / design issues
- Explanation mismatches actual behavior (claims correct exclusion but denominator is wrong)
-  Validation or guard should be set to prevent division by zero

## 2) Proposed Fixes / Improvements
### Summary of changes
- Maintain separate counter for non-cancelled orders
- Use that counter as divisor
- Return 0.0 when no valid orders (safe default)

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty list → should return 0.0 (prevent crash)
- All cancelled → should return 0.0
- Mix of cancelled/non-cancelled → average should match only valid amounts / valid count
- Single non-cancelled order → average equals that amount
- Large list with many cancelled → verify no underestimation


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Mismatches code: says excludes cancelled but divides by total orders
- Does not mention division-by-zero risk

### Rewritten explanation
- This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of valid (non-cancelled) orders. If there are no valid orders, it safely returns 0.0.
## 4) Final Judgment
- Decision: Reject
- Justification: Fundamental error in averaging logic (wrong denominator) combined with unhandled division by zero makes the function incorrect and unsafe for real use.
- Confidence & unknowns: High — issues are clear and reproducible. No unknowns.

---



# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Only checks `"@" in email` → extremely weak; accepts clearly invalid strings (e.g. "a@", "@b.com", "user@domain@extra", "text with @ inside")

### Edge cases & risks
- Empty list → correctly returns 0 (this works)
- Strings with multiple @ → counted as valid
- Domain-only or local-only → counted
- Whitespace around email → still counted if @ present

### Code quality / design issues
- Explanation severely overstates capability: claims "valid email addresses" and "safely ignores invalid entries" — but rejects almost nothing
- No structural validation at all

## 2) Proposed Fixes / Improvements
### Summary of changes
- Replaced the extremely weak "@ in email" check with a compiled regular expression for reliable structural validation (non-empty local part, single @, domain with at least one dot and TLD)
- Added isinstance(email, str) check to safely skip non-string inputs and prevent crashes
- Strip leading/trailing whitespace before matching

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Valid formats: "user@domain.com", "name.surname@company.co.ke"
- Invalid: "user@", "@domain.com", "user@domain@extra", "no@", "plain text @"
- Edge: empty string, whitespace-only, multiple @, no dot in domain
- Empty list → should return 0
- All invalid → return 0
- Mixed valid/invalid → correct count of plausible ones

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Grossly overstates validation quality
- `Valid email addresses` is misleading — barely filters anything

### Rewritten explanation
- This function counts strings that match a basic but effective email pattern: non-empty local part, single @ separator, non-empty domain containing at least one dot followed by a TLD. It safely skips non-string inputs, removes leading/trailing whitespace, and returns 0 for empty lists or no matching entries. This is a practical filter, not full RFC 5322-compliant validation.

## 4) Final Judgment
- Decision:  Reject
- Justification:The original implementation does not meet the stated requirement of validating email addresses.
- Confidence & unknowns:High — many obvious false positives.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by total length (`len(values)`) instead of count of valid numeric entries → wrong average when `None` present
- `float(v)` crashes (ValueError) on non-numeric non-None values (e.g. strings, lists)

### Edge cases & risks
- Empty list → `ZeroDivisionError`
- All `None` → `ZeroDivisionError` if list non-empty
- Mixed types with invalid non-None (e.g. `"abc"`, `[1]`) → crash

### Code quality / design issues
- Explanation falsely claims "safely handles mixed input types" — it does not
- No attempt to skip conversion failures

## 2) Proposed Fixes / Improvements
### Summary of changes
- Only count and sum values that are non-None **and** successfully convert to float
- Skip invalid conversions
- Return 0.0 when no valid values

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- All valid numbers → correct average
- Mix of numbers and `None` → average of numbers only
- Non-numeric non-None (string, list, dict) → should skip, not crash
- All `None` or empty → return 0.0
- Single valid value → average equals that value
- Values already float/int vs string numbers ("3.14") → both accepted


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Claims safe handling of mixed types → false (crashes on non-numeric)
- Wrong averaging logic described (ignores denominator issue)
- Overpromises accuracy

### Rewritten explanation
- This function computes the average of numeric measurements, ignoring `None` and skipping any non-`None` values that cannot be converted to float. Only successfully converted values are included in the sum and count. Returns 0.0 if no valid measurements exist.

## 4) Final Judgment
- Decision: Reject
- Justification: Incorrect averaging logic (wrong denominator), crashes on invalid non-None values, and misleading safety claims make the code and explanation unreliable for production use.
- Confidence & unknowns: High confidence — core bugs are clear and reproducible. No major unknowns.
