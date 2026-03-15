import pickle

with open('metadata.pkl', 'rb') as f:
    data = pickle.load(f)

print(f"Total chunks: {len(data)}")
for i, m in enumerate(data):
    # Print the first 150 chars of each chunk with its page number
    print(f"--- Chunk {i} | Page {m['page_number']} ---")
    print(m['text'][:150])
    print("-" * 30)
