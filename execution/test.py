
import os
try:
    os.makedirs('.tmp', exist_ok=True)
    with open('.tmp/test_log.txt', 'w') as f:
        f.write('Python works')
except Exception as e:
    pass
