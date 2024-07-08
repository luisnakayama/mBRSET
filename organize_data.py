import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

def organize_images(dataframe, image_column, class_column, image_path, result_dir, test_size=0.2, val_size=0.1):
    
    # Create directories for the dataset
    split_dir = os.path.join(result_dir, f'split_{class_column}')
    os.makedirs(split_dir, exist_ok=True)
    
    result_dir = os.path.join(result_dir, 'images')
    
    for split in ['train', 'val', 'test']:
        for cls in dataframe[class_column].unique():
            os.makedirs(os.path.join(result_dir, split, cls), exist_ok=True)

    # Split data into train, validation, and test sets
    train_val, test = train_test_split(dataframe, test_size=test_size, stratify=dataframe[class_column])
    train, val = train_test_split(train_val, test_size=val_size / (1 - test_size), stratify=train_val[class_column])
    
    # Save the splits to CSV files
    train.to_csv(os.path.join(split_dir, 'train.csv'), index=False)
    val.to_csv(os.path.join(split_dir, 'val.csv'), index=False)
    test.to_csv(os.path.join(split_dir, 'test.csv'), index=False)

    # Function to copy images to the correct directory
    def copy_images(data, split):
        for _, row in data.iterrows():
            src_path = os.path.join(image_path, row[image_column])
            dst_path = os.path.join(result_dir, split, row[class_column], row[image_column])
            shutil.copy(src_path, dst_path)

    # Copy images to their respective directories
    copy_images(train, 'train')
    copy_images(val, 'val')
    copy_images(test, 'test')



def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Organize images into class-specific train, val, and test directories.')
    parser.add_argument('--data_csv', type=str, help='Path to the CSV file containing image ids and class labels.')
    parser.add_argument('--image_column', type=str, help='Column name for image filenames.')
    parser.add_argument('--class_column', type=str, help='Column name for class labels.')
    parser.add_argument('--image_path', type=str, help='Directory path where images are stored.')
    parser.add_argument('--result_dir', type=str, help='Directory path where train/val/test directories will be created.')
    parser.add_argument('--test_size', type=float, default=0.2, help='Proportion of the dataset to include in the test split.')
    parser.add_argument('--val_size', type=float, default=0.1, help='Proportion of the dataset to include in the validation split.')

    args = parser.parse_args()

    # Load the data
    df = pd.read_csv(args.data_csv)

    # Organize images
    organize_images(df, args.image_column, args.class_column, args.image_path, args.result_dir, args.test_size, args.val_size)

if __name__ == "__main__":
    main()