import pyautogui
import time
time.sleep(5)
def autotyper(words):
    for char in words:
        pyautogui.typewrite(char)

w=str(
    '''For multimedia projects, I recommend Adobe Premiere Pro and DaVinci Resolve for video editing, Photoshop and Canva for graphic design, and Audacity for audio editing. After Effects is ideal for motion graphics, while Blender is excellent for 3D animation. For website creation, WordPress and Webflow offer flexibility, with GitHub Pages for hosting static sites. Unsplash and Pexels provide free stock images, and Envato Elements offers extensive templates and resources. HandBrake is great for video conversion. These tools cater to various needs, from simple edits to professional-level productions.
    '''
)
autotyper(w)