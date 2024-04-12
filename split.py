from PIL import Image
import os
import glob

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

def split_and_save_image(input_path, output_path_prefix):
    # 画像を読み込みます
    image = Image.open(input_path)
    
    # 画像の幅と高さを取得します
    width, height = image.size
    
    # 画像を中央で横に2分割します
    left_half = image.crop((0, 0, width // 2, height))
    right_half = image.crop((width // 2, 0, width, height))
    
    # 保存用のファイル名を生成します
    output_path_left = output_path_prefix + "_01.png"  # または "_left.jpg"
    output_path_right = output_path_prefix + "_02.png"  # または "_right.jpg"
    
    # 分割した画像を保存します
    left_half.save(output_path_left)
    right_half.save(output_path_right)


# ワイルドカードを使用してフォルダ内のすべてのファイルを取得します
folders = glob.glob(os.path.join('input', '*'))
for folder in folders:
    files = glob.glob(os.path.join(folder, '*'))
    for file in files:
        # ファイル名のみを取得します
        file_name = os.path.basename(file)
        
        # フォルダー名を取得します
        folder_name = os.path.basename(os.path.dirname(file))
        
        # 拡張子を含むファイル名を取得します
        file_name_with_extension = os.path.basename(file)
        
        # 拡張子なしのファイル名を取得します
        file_name_without_extension = os.path.splitext(file_name_with_extension)[0]
        
        # 拡張子を取得します
        extension = os.path.splitext(file_name_with_extension)[1]

        # 入力画像のパス
        input_image_path = file

        # 出力先
        output_path = 'output\\' + folder_name
        # フォルダが存在しない場合は作成します
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # 出力画像のパスのプレフィックス
        output_image_prefix = output_path + '\\' + file_name_without_extension

        if extension in image_extensions:
            # 画像を分割して保存します
            split_and_save_image(input_image_path, output_image_prefix)
        else:
            pass

