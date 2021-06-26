# animations

"gridsearch_optimized_fft_extrapolation.py"

overview:
  -basic/novice approach to gridsearch optimization

  -Minimizes the MSE from an fft extrapolation up to the current minute, then uses the optimized parameters to generate an extraploation into the future by       optimized variable "FUTURE_PERIOD_PREDICT"

Known Errors:
  -This optimization approach works, but is flawed because a smaller "FUTURE_PERIOD_PREDICT" parameter almost always results in a smaller MSE. In other words, this   approach is biased because a smaller prediction period generally results in a smaller error.
  
  -MSE can be biased sometimes. In semi-technical terms: The mean squared error between two curves can be close to zero if they are "mirrored images" of one another.
  
Uses:
  -Planning to use this technique for generating a FFT extrapolation sequence as a Deep Learning feature column
