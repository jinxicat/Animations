from hyperopt import fmin, tpe, hp

def sim(params):
  ###put your methods here ;)
  return -roi

###bayesian optimization
space = {
    "roof_pct": hp.uniform("initial_roof_pct", 0.001, 0.07),
    "step_pct": hp.uniform("step_pct", 0.001, 0.07),
    "stop_loss_pct": hp.uniform("stop_loss_pct", 0.01, 0.055)
}

###main shit
tpe_algo = tpe.suggest
tpe_trials = Trials()
tpe_best = fmin(fn=sim,space=space,algo=tpe_algo,trials=tpe_trials,max_evals=50)
print(tpe_best)
