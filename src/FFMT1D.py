import numpy as np


def ffmt1d(res, thi, per):

	# global b
	b = [[0] * 2 for _ in range(2)]
	thi.append(0)
	nl = len(res)
	nper = len(per)
	phi = np.arctan(1)*4
	amu = phi*(4*(10**-7))

	zre = []
	zim = []
	rho = []
	phas = []
	for i in range(0, nper):
		zz = []
		x = np.zeros((nl, 2, 2), dtype=np.complex128)
		a = np.zeros((2, 2), dtype=np.ndarray)
		for j in range(0, nl):
			z = np.sqrt(phi*amu*res[j]*per[i])
			zz.append(complex(z, z))
			exp0 = np.exp((-2)*zz[j]/res[j]*thi[j])
			exp1 = complex(1, 0)+exp0
			exp2 = complex(1, 0)-exp0
		
		# built 3D Matrix
			x[j, 0, 0] = exp1
			x[j, 0, 1] = zz[j]*exp2
			x[j, 1, 0] = exp2/zz[j]
			x[j, 1, 1] = exp1
# 
		a[0, 0] = complex(1, 0)
		a[0, 1] = complex(0, 0)
		a[1, 0] = complex(0, 0)
		a[1, 1] = complex(1, 0)

		for k in range(0, (nl-1)):
			b = multiplication(a, x[k, :, :])
			for m in range(0, 2):
				for n in range(0, 2):
					a[m][n] = b[m][n]

		rnom = zz[nl-1]*b[0][0]+b[0][1]
		rden = zz[nl-1]*b[1][0]+b[1][1]
		rr = rnom/rden
		zre.append(np.real(rr))
		zim.append(np.imag(rr))
		rho.append((1/per[i])*(np.absolute(rnom/rden))**2/(8e-7*phi*phi))
		phas.append(np.arctan(zim[i]/zre[i])*180/phi)
	return rho, phas


def multiplication(a, d):

	c = np.zeros((2, 2), dtype=np.complex128)
	# C[i][j] = complex(0,0)
	for i in range(0, 2):
		for j in range(0, 2):
			for m in range(0, 2):
				c[i][j] = c[i][j] + a[i][m]*d[m][j]
	return c
