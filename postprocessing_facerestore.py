# A pose process script
from PIL import Image
import numpy as np

from modules import scripts_postprocessing, gfpgan_model
import gradio as gr
from modules.ui_components import FormRow

class ScriptPostprocessing(scripts_postprocessing.ScriptPostprocessing):
    name = "PostFaceRestore"
    order = 4000

    def ui(self):
        with FormRow():
            use_pose_face_restore = gr.Checkbox(label="Post Face Restore", value=True, elem_id="extras_post_face_restore")

        return {
            "use_pose_face_restore": use_pose_face_restore,
        }

    def process(self, pp: scripts_postprocessing.PostprocessedImage, use_pose_face_restore):
        print("Start Post Face Restore")
        if use_pose_face_restore:
            print("run Restore Face")
            restored_img = gfpgan_model.gfpgan_fix_faces(np.array(pp.image, dtype=np.uint8))
            res = Image.fromarray(restored_img)
            pp.image =res

        # return pp

