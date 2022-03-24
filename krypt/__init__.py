import os
import util.exceptions

if os.name() != 'nt':
  raise util.exceptions.OSError('This OS is not Windows!')
