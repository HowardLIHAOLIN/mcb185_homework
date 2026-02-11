import math

def char_to_prob(ch):
	if type(ch) is not str or len(ch) != 1:
		return None
	q = ord(ch)-33
	if q < 0:
		return None
	return 10**(-q/10)
	
def prob_to_char(p):
	if type(p) is not float and type(p) is not int:
		return None
	if p <= 0 or p >= 1:
		return None
	q = -10 * math.log10(p)
	q_int = int(round(q))
	code = q_int + 33
	if code < 33 or code > 126:
		return None
	return chr(code)
    
print(char_to_prob('A'))
print(prob_to_char(0.001))