from sys import argv

def exponencialvspolinamial():

    n=2
    pol = pow(n, 10)
    exp = pow(1.002, n)
    while(pol > exp):
        print('pol: ' + str(pol) + 'exp: '   + str(exp) + 'n: ' +  str(n))
        n*=2
        pol = pow(n, 10)
        exp = pow(1.002, n)

    print('pol: ' + str(pol) + ' exp: '   + str(exp) + ' n: ' +  str(n))


exponencialvspolinamial()