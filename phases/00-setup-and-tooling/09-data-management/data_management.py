from datasets import load_dataset

dataset = load_dataset(
    "stanfordnlp/imdb",
    split="train[:1000]"
)

# 第一步：先分出 70% 作为训练集，剩下 30%
first_split = dataset.train_test_split(
    test_size=0.3,
    seed=42
)

train_dataset = first_split["train"]
remaining_dataset = first_split["test"]

# 第二步：把剩下的 30% 平分成验证集和测试集
# 30% 的一半是 15%，所以 test_size=0.5
second_split = remaining_dataset.train_test_split(
    test_size=0.5,
    seed=42
)

validation_dataset = second_split["train"]
test_dataset = second_split["test"]

print("训练集数量：", train_dataset.num_rows)
print("验证集数量：", validation_dataset.num_rows)
print("测试集数量：", test_dataset.num_rows)

total = (
    train_dataset.num_rows
    + validation_dataset.num_rows
    + test_dataset.num_rows
)

print("\n总数量：", total)

print("\n比例：")
print("训练集比例：", train_dataset.num_rows / total)
print("验证集比例：", validation_dataset.num_rows / total)
print("测试集比例：", test_dataset.num_rows / total)

print("\n检查：")
print("训练集是否为 700：", train_dataset.num_rows == 700)
print("验证集是否为 150：", validation_dataset.num_rows == 150)
print("测试集是否为 150：", test_dataset.num_rows == 150)