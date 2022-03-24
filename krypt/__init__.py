import os
if os.name() != 'nt':
  raise OSError('This OS is not Windows!')
