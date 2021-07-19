# animations

"gridsearch_optimized_fft_extrapolation.py"

Overview:
  -basic/novice approach to gridsearch optimization

  -Minimizes the MSE from an fft extrapolation up to the current minute, then uses the optimized parameters to generate an extraploation into the future by       optimized variable "FUTURE_PERIOD_PREDICT"
  
Possible Uses:
  -Use extrapolation techniques to remove time-gaps in large timeseires data sets. 
  -Planning to use this technique for generating a FFT extrapolation sequence as a Deep Learning feature column
