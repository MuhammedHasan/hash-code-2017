from solver import *

for i in ['me_at_the_zoo', 'trending_today',
          'videos_worth_spreading', 'kittens']:
    s = Solver(i)
    s.solve()
    s.parse()
