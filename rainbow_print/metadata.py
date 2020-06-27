# -*- coding: utf-8 -*-
"""
| **@created on:** 6/26/20,
| **@author:** prathyushsp,
| **@version:** v0.0.1
|
| **Description:**
| 
|
| **Sphinx Documentation Status:** 
"""

import json
with open('/'.join(str(__file__).split('/')[:-1]) + '/metadata.json') as f:
    metadata = json.load(f)
