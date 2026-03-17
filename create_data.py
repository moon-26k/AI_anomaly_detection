import pandas as pd
import numpy as np

data = {
    'packet_size': np.random.uniform(0.1, 0.5, 95).tolist() + [0.9, 0.95, 0.85, 0.88, 0.92],
    'inter_arrival_time': np.random.uniform(0.1, 0.4, 95).tolist() + [0.8, 0.85, 0.9, 0.75, 0.95],
    'src_port': np.random.randint(1024, 65535, 100),
    'dst_port': [443] * 100
}

df = pd.DataFrame(data)
df.to_csv('network_data.csv', index=False)
print("Success! 'network_data.csv'")