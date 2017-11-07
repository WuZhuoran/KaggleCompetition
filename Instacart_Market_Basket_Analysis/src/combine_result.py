import pandas as pd

baseline = pd.read_csv('stack_baseline.csv')
result = pd.read_csv('lgb_sub.csv')

result['order_id'] = baseline['order_id']
result = result[['order_id', 'products']]

print(result)

result.to_csv('lgb_add_embedding_submission.csv', index=False)