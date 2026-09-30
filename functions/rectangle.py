def rectangle_info(w, h):
	area = w * h
	perimeter = 2*w + 2*h
	return area, perimeter

a, p = rectangle_info(1, 10)
print("Area:", a)
print("Perimeter:", p)
