#ASSIGNMENT One
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr


#varibility of rainfall for the flood month Ashaiman
NC = xr.open_dataset('chirps_21_WA_new.nc')
Ashaiman = NC.precip.sel(longitude = -0.032, latitude = 5.69, method = 'nearest')
Ashaiman_June = Ashaiman.sel(time =slice('2010-06-01', '2010-06-30'))
Ashaiman_anon = (Ashaiman_June-np.mean(Ashaiman_June))
#percentage contribution of 9 sept, 2007 rainfall
per_cont = (Ashaiman_June.sel(time = '2010-06-20') /Ashaiman_June.sum())*100

#Dansoman
Dansoman = NC.precip.sel(longitude = -0.256, latitude = 5.542, method = 'nearest')
Dansoman_Oct = Dansoman.sel(time =slice('2011-10-01', '2011-10-31'))
Dansoman_anon = (Dansoman_Oct-np.mean(Dansoman_Oct))
#percentage contribution of 9 sept, 2007 rainfall
Dan_per_cont = (Dansoman_Oct.sel(time = '2011-10-25') /Dansoman_Oct.sum())*100

#kwame nkrumah circle
Circle = NC.precip.sel(longitude = -0.216, latitude = 5.556, method = 'nearest')
Circle_june = Circle.sel(time =slice('2013-06-01', '2013-06-30'))
Circle_anon = (Circle_june-np.mean(Circle_june))
#percentage contribution of 9 sept, 2007 rainfall
Circ_per_cont = (Circle_june.sel(time = '2013-06-03') /Circle_june.sum())*100


#Santa Maria
Santa = NC.precip.sel(longitude = -0.264, latitude = 5.604, method = 'nearest')
santa_sept = Circle.sel(time =slice('2014-09-01', '2014-09-30'))
santa_anon = (santa_sept-np.mean(santa_sept))
#percentage contribution of 9 sept, 2007 rainfall
santa_per_cont = (santa_sept.sel(time = '2014-09-26') /santa_sept.sum())*100



fig, ax = plt.subplots(2,2, figsize = (40, 40))
fig.subplots_adjust(bottom=0.5, left = 0.4)
#Ashaiman
ax[0,0].plot(Ashaiman_June, color = 'k', lw = 3, marker = 'o', label = 'Rainfall amount')
ax[0,0].plot(Ashaiman_anon, color = 'r', lw = 3, marker = 'o', label = 'Ranifall anomaly')
ax[0,0].set_ylabel('Rainfall (mmd$^{-1}$)', fontsize =18)
ax[0,0].set_xlabel('Days', fontsize =18)
ax[0,0].set_title('Ashaiman, June, 2010', size =20, weight ='bold')
ax[0,0].axhline(y = 10, color ='k', label = '75th Percentile' , linestyle = '-', lw =3)
ax[0,0].axhline(y = 25, color ='r', label = '95th Percentile', linestyle = '--', lw =3)
ax[0,0].set_xticks(range(1, 30, 3))
ax[0,0].set_xticklabels(['3','6', '9','12', '15', '18', '21','24', '27', '30'], size =20)
ax[0,0].set_yticks(range(-10, 60, 10))
ax[0,0].set_yticklabels(['-10','0','10', '20', '30', '40', '50'], size =20)
ax[0,0].annotate('*', xy =(18.5, 27), size =40, color = 'b')
ax[0,0].annotate('12.03%', xy =(20, 29), size =30, color = 'k')
ax[0,0].legend(loc = 2, fontsize =15)
#ax[0,0].legend(loc =1, bbox_to_anchor=(0.50, 1.0), fontsize = 15)


#Dansoman
ax[0,1].plot(Dansoman_Oct, color = 'k', lw = 3, marker = 'o', label = 'Rainfall amount')
ax[0,1].plot(Dansoman_anon, color = 'r', lw = 3, marker = 'o', label = 'Ranifall anomaly')
ax[0,1].set_ylabel('Rainfall (mmd$^{-1}$)', fontsize =18)
ax[0,1].set_xlabel('Days', fontsize =18)
ax[0,1].set_title('Dansoman, October, 2011', size =20, weight ='bold')
ax[0,1].axhline(y = 10, color ='k', label = '75th Percentile' , linestyle = '-', lw =3)
ax[0,1].axhline(y = 25, color ='r', label = '95th Percentile', linestyle = '--', lw =3)
ax[0,1].set_xticks(range(1, 30, 3))
ax[0,1].set_xticklabels(['3','6', '9','12', '15', '18', '21','24', '27', '30'], size =20)
ax[0,1].set_yticks(range(-10, 60, 10))
ax[0,1].set_yticklabels(['-10','0', '10',  '20','30', '40',  '50' ], size =20)
ax[0,1].annotate('*', xy =(23.6, 46), size =40, color = 'b')
ax[0,1].annotate('22.56%', xy =(25, 48), size =30, color = 'k')
#ax[0,1].legend(loc =1, bbox_to_anchor=(0.50, 1.0), fontsize = 15)
ax[0,1].legend(loc = 2, fontsize =15)
#ax[0,1].legend(title = 'Legend', loc=3, bbox_to_anchor=(1, -0.25), fontsize = 15)

#circle plot
ax[1,0].plot(Circle_june, color = 'k', lw = 3, marker = 'o', label = 'Rainfall amount')
ax[1,0].plot(Circle_anon, color = 'r', lw = 3, marker = 'o', label = 'Ranifall anomaly')
ax[1,0].set_ylabel('Rainfall (mmd$^{-1}$)', fontsize =18)
ax[1,0].set_xlabel('Days', fontsize =18)
ax[1,0].set_title('Kwame Nkrumah Circle, June, 2013', size =20, weight ='bold')
ax[1,0].axhline(y = 10, color ='k', label = '75th Percentile' , linestyle = '-', lw =3)
ax[1,0].axhline(y = 25, color ='r', label = '95th Percentile', linestyle = '--', lw =3)
ax[1,0].set_xticks(range(1, 30, 3))
ax[1,0].set_xticklabels(['3','6', '9','12', '15', '18', '21','24', '27', '30'], size =20)
ax[1,0].set_yticks(range(-10, 50, 10))
ax[1,0].set_yticklabels(['-10','0','10', '20', '30', '40'], size =20)
ax[1,0].annotate('*', xy =(1.5, 19.2), size =40, color = 'b')
ax[1,0].annotate('26.26%', xy =(3, 21), size =30, color = 'k')
ax[1,0].legend(loc = 2, fontsize =15)

#Santa Maria plot
ax[1,1].plot(santa_sept, color = 'k', lw = 3, marker = 'o', label = 'Rainfall amount')
ax[1,1].plot(santa_anon, color = 'r', lw = 3, marker = 'o', label = 'Ranifall anomaly')
ax[1,1].set_ylabel('Rainfall (mmd$^{-1}$)', fontsize =18)
ax[1,1].set_xlabel('Days', fontsize =18)
ax[1,1].set_title('Santa Maria, September, 2014', size =20, weight ='bold')
ax[1,1].axhline(y = 10, color ='k', label = '75th Percentile' , linestyle = '-', lw =3)
ax[1,1].axhline(y = 25, color ='r', label = '95th Percentile', linestyle = '--', lw =3)
ax[1,1].set_xticks(range(1, 30, 3))
ax[1,1].set_xticklabels(['3','6', '9','12', '15', '18', '21','24', '27', '30'], size =20)
ax[1,1].set_yticks(range(-10, 50, 10))
ax[1,1].set_yticklabels(['-10','0','10', '20', '30', '40'], size =20)
ax[1,1].annotate('*', xy =(24.5, 20), size =40, color = 'b')
ax[1,1].annotate('26.52%', xy =(26, 21), size =25, color = 'k')
ax[1,1].legend(loc = 2, fontsize =15)
