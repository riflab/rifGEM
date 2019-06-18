import matplotlib.pylab as plt


def plot_PerRhoPhase(per, rho, phas):
	plt.figure(1)
	plt.subplot(211)
	plt.loglog(per,rho)
	plt.ylim(1, 1000)

	plt.subplot(212)
	plt.semilogx(per,phas)
	plt.ylim(0, 180)

	plt.show()
