`Pillow` (PIL 的 fork) 是 Python 中最流行的图像处理库。它的核心对象是 **`Image`** 对象。

以下是按功能分类的常用函数和属性，涵盖了从**读取、查看、处理到保存**的全流程。

### 0. 基础导入
```python
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
import numpy as np # 常配合使用
```

---

### 1. 图像的打开与保存 (I/O)
*最基础的操作，注意路径问题。*

| 函数/方法 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`Image.open()`** | 打开图片文件 | `img = Image.open('photo.jpg')` |
| **`img.save()`** | 保存图片 | `img.save('out.png', quality=95)` |
| **`img.format`** | 查看原图格式 (如 'JPEG') | `print(img.format)` |
| **`img.mode`** | 查看颜色模式 (如 'RGB', 'L', 'RGBA') | `print(img.mode)` |
| **`img.size`** | 查看尺寸 `(宽, 高)` | `w, h = img.size` |
| **`img.info`** | 查看元数据 (EXIF, DPI 等) | `print(img.info)` |

---

### 2. 图像转换与调整 (Transform)
*改变图片的尺寸、模式或方向。*

| 方法 | 说明 | 常用参数/示例 |
| :--- | :--- | :--- |
| **`img.resize()`** | **调整大小** (最常用) | `img.resize((224, 224), resample=Image.LANCZOS)` |
| **`img.crop()`** | **裁剪** | `img.crop((left, upper, right, lower))` 例：`(10, 10, 100, 100)` |
| **`img.rotate()`** | 旋转角度 | `img.rotate(45, expand=True)` (`expand=True` 自动扩大画布以防切角) |
| **`img.transpose()`** | 翻转/转置 | `img.transpose(Image.FLIP_LEFT_RIGHT)` (左右镜像)`Image.ROTATE_90`, `Image.TRANSPOSE` |
| **`img.convert()`** | **转换颜色模式** | `img.convert('L')` (转灰度)`img.convert('RGB')` (去透明通道)`img.convert('1')` (转黑白二值) |
| **`img.getbbox()`** | 获取非零区域边界 | 常用于自动裁剪掉周围空白 `img.crop(img.getbbox())` |

> **💡 提示**：`resize` 的 `resample` 参数推荐：
> - 缩小图片：`Image.LANCZOS` (高质量) 或 `Image.ANTIALIAS` (旧版别名)
> - 放大图片：`Image.BICUBIC` 或 `Image.BILINEAR`

---

### 3. 图像增强与滤镜 (Enhance & Filter)
*调整亮度、对比度或添加模糊效果。*

#### A. 内置滤镜 (`ImageFilter`)
```python
from PIL import ImageFilter

img.filter(ImageFilter.BLUR)        # 模糊
img.filter(ImageFilter.GaussianBlur(radius=2)) # 高斯模糊
img.filter(ImageFilter.SHARPEN)     # 锐化
img.filter(ImageFilter.EDGE_ENHANCE)# 边缘增强
img.filter(ImageFilter.DETAIL)      # 细节增强
img.filter(ImageFilter.CONTOUR)     # 轮廓提取
```

#### B. 增强控制 (`ImageEnhance`)
```python
from PIL import ImageEnhance

# 亮度
enhancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(1.5) # 1.0 原图, >1 变亮, <1 变暗

# 对比度
enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(2.0)

# 色彩 (饱和度)
enhancer = ImageEnhance.Color(img)
color_img = enhancer.enhance(0.0) # 0.0 变为灰度图

# 锐化
enhancer = ImageEnhance.Sharpness(img)
sharp_img = enhancer.enhance(3.0)
```

---

### 4. 绘图与文字 (Draw & Text)
*在图片上画框、写文字（常用于目标检测可视化）。*

```python
from PIL import ImageDraw, ImageFont

# 1. 创建绘图对象
draw = ImageDraw.Draw(img)

# 2. 画矩形 (左上角, 右下角)
draw.rectangle([50, 50, 200, 200], outline="red", width=3)

# 3. 画圆 (外接矩形)
draw.ellipse([10, 10, 60, 60], fill="blue", outline="black")

# 4. 画线
draw.line([0, 0, 100, 100], fill="white", width=2)

# 5. 写文字
# 加载字体 (如果不指定路径，使用默认字体，通常很小且不支持中文)
# 推荐下载 .ttf 文件，如 Arial.ttf 或 SimHei.ttf (黑体)
font = ImageFont.truetype("arial.ttf", 24) 
draw.text((50, 210), "Hello Pillow", fill="yellow", font=font)
```

---

### 5. 与 NumPy 互转 (重要！用于深度学习)
*Sklearn/PyTorch/TensorFlow 通常需要 NumPy 数组，而 Pillow 处理文件。*

```python
import numpy as np

# Pillow -> NumPy
img = Image.open('photo.jpg')
np_array = np.array(img) 
# 形状: (H, W, 3) for RGB, (H, W) for Gray
# 数据类型通常是 uint8 (0-255)

# NumPy -> Pillow
new_img = Image.fromarray(np_array)
# 注意：如果数组是浮点数 (0.0-1.0)，需先乘 255 并转为 uint8
```

---

### 6. 批量处理与便捷操作 (`ImageOps`)
`ImageOps` 模块提供了一些不需要创建对象的高级快捷操作。

```python
from PIL import ImageOps

# 自动调整对比度
img = ImageOps.autocontrast(img)

# 反转颜色 (底片效果)
img = ImageOps.invert(img)

# 灰度化 (比 convert('L') 提供更多控制)
img = ImageOps.grayscale(img)

# 镜像
img = ImageOps.mirror(img) # 左右
img = ImageOps.flip(img)   # 上下

# 裁剪中心部分 (类似 crop center)
img = ImageOps.fit(img, (224, 224), centering=(0.5, 0.5)) 
# centering: (0,0)左上, (0.5, 0.5)正中, (1,1)右下
```

---

### 💡 常见场景代码模板

#### 场景 1：预处理图片供模型使用 (Resize + Normalize)
```python
from PIL import Image
import numpy as np

def preprocess_image(path, target_size=(224, 224)):
    img = Image.open(path).convert('RGB')
    # 高质量缩放
    img = img.resize(target_size, Image.LANCZOS)
    # 转数组并归一化到 0-1
    img_array = np.array(img).astype(np.float32) / 255.0
    return img_array
```

#### 场景 2：给图片加水印
```python
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, output_path, text):
    img = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0)) # 透明层
    draw = ImageDraw.Draw(txt_layer)
    
    # 使用默认字体 (实际建议用 truetype)
    font = ImageFont.load_default() 
    
    # 简单计算位置 (右下角)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = img.size[0] - text_w - 10
    y = img.size[1] - text_h - 10
    
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128)) # 半透明白色
    
    # 合并
    out = Image.alpha_composite(img, txt_layer)
    out.convert("RGB").save(output_path)
```

#### 场景 3：检查并修复损坏的图片方向 (EXIF Orientation)
*手机拍的照片经常因为 EXIF 信息导致在电脑上显示旋转了 90 度，但在 PIL 中读取时可能不会自动修正（取决于版本），最好手动处理。*
```python
from PIL import Image, ImageOps

img = Image.open('photo.jpg')
# 自动根据 EXIF 信息修正方向
img = ImageOps.exif_transpose(img)
img.save('fixed_photo.jpg')
```

掌握以上函数，足以应对 95% 的 Python 图像处理需求。对于更复杂的操作（如复杂的蒙版、通道混合），通常结合 `NumPy` 直接操作像素矩阵会更高效。