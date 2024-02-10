M = float(input('Me fale uma distancia em metros: '))
MM = M * 1000
CM = M * 100
DM = M * 10
DAM = M / 10
HM = M / 100
KM = M / 1000
print('Analisando esse valor {}m podemos afirmar que ele corresponde tambem a {}mm, {}cm, {}dm, {}dam, {}hm, {}km'.format(M, MM, CM, DM, DAM, HM, KM ))