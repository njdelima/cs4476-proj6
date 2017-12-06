import os, random

DIR = 'HumanObjectSketches'
TEST_DIR = os.path.join(DIR, 'test')
TRAIN_DIR = os.path.join(DIR, 'train')
RAW_DIR = os.path.join(DIR, 'raw')

categories = [name for name in os.listdir(RAW_DIR) if os.path.isdir(os.path.join(RAW_DIR, name))]

if not os.path.exists(TRAIN_DIR):
	os.makedirs(TRAIN_DIR)

if not os.path.exists(TEST_DIR):
	os.makedirs(TEST_DIR)

for category in categories:
	train_category_path = os.path.join(TRAIN_DIR, category)
	test_category_path = os.path.join(TEST_DIR, category)
	os.makedirs(train_category_path)
	os.makedirs(test_category_path)
	
	raw_category_path = os.path.join(RAW_DIR, category)

	raw_files = [name for name in os.listdir(raw_category_path) if os.path.isfile(os.path.join(raw_category_path, name))]

	test_files = [raw_files.pop(random.randrange(len(raw_files))) for _ in xrange(20)]
	train_files = raw_files

	for file in test_files:
		os.rename(os.path.join(raw_category_path, file), os.path.join(test_category_path, file))

	for file in train_files:
		os.rename(os.path.join(raw_category_path, file), os.path.join(train_category_path, file))

