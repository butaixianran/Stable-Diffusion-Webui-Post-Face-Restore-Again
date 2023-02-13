# Stable-Diffusion-Webui-Post-Face-Restore-Again
This is a script for Stable-Diffusion-Webui. In Extra tab, it run face restore again, which offers you much better result on face restore.

# Why we need this
We often generate small images with size less than 1024. In that case, eyes are often twisted, even we already have face restore applied.

In Extra Tab, when you upscale an image, it will run face restore one time automatically. But, sometimes, one time is still not good enough.
Especially when image is full shot or wider shot.

**With this script, which runs face restore again, can fix most face problem you have. You won't feel any unnatural thing on character's face.**  

**Without it:**  
![](img/without.jpg)  

**With it:**  
![](img/with.jpg)  


# How to use
Download the "postprocessing_facerestore.py" python script, put it into `Your Stable-Diffusion-Webui/scripts` folder, Reload UI, done.


