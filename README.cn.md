# Stable-Diffusion-Webui-Post-Face-Restore-Again
这是Stable-Diffusion-Webui的脚本。在Extra页面，本脚本会在图片放大后，再运行一次面部修复功能，从而得到更好的面部修复效果。

# 为什么需要它
我们经常都是出小图，尺寸低于1024。这种情况下，如果是全身镜头，眼睛经常会扭曲，即使勾选了面部修复也会。

在Extra页面，当你放大一张图片的时候，webui会自动运行一次面部修复。但是，有时候，一次都不够。尤其是全身镜头，人物眼睛小的时候。

**用这个脚本，就会再多跑一次面部修复，就能修复绝大部分面部问题，几乎感觉不到任何不自然。**  

**不用本脚本:**  
![](img/without.jpg)  

**使用本脚本:**  
![](img/with.jpg)  


# 使用方法
下载并解压本项目，把"postprocessing_facerestore.py"这个文件，放到`你的Stable-Diffusion-Webui/scripts` 目录, 在设置页面，右上角，点击刷新UI即可。

之后，在Extra页面最下方，会多出来一个勾选框叫"Post Face Restore"，去掉勾选，就不会运行了。


