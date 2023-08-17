from ..utils import common_annotator_call, annotator_ckpts_path, HF_MODEL_NAME
import controlnet_aux
import comfy.model_management as model_management

class Manga2Anime_LineArt_Preprocessor:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "preprocessors/edge_line"

    def execute(self, image, **kwargs):
        model = controlnet_aux.LineartMangaDetector.from_pretrained(HF_MODEL_NAME, cache_dir=annotator_ckpts_path).to(model_management.get_torch_device())
        return (common_annotator_call(model, image), )

NODE_CLASS_MAPPINGS = {
    "Manga2Anime_LineArt_Preprocessor": Manga2Anime_LineArt_Preprocessor
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Manga2Anime_LineArt_Preprocessor": "Manga Lineart"
}