import google.generativeai as gen_ai
import google.ai.generativelanguage as glm

generation_config_1 = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 90,
  "max_output_tokens": 20000,
  # "response_mime_type": "text/plain"
}

safety_settings_1 = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model_1 = gen_ai.GenerativeModel(
    model_name= "gemini-1.5-pro",
    generation_config = generation_config_1,
    safety_settings = safety_settings_1)

# ================================================== Recommendation model (AI is assistant) ==========================================
generation_config_2 = {
  "temperature": 0.9,
  "top_p": 0.8,
  "top_k": 65,
  "max_output_tokens": 20000,
  # "response_mime_type": "text/plain"
}
safety_settings_2 = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model_2 = gen_ai.GenerativeModel(
    model_name= "gemini-1.5-pro",
    generation_config= generation_config_2,
    # generation_config = glm.GenerationConfig(candidate_count = 3),
    safety_settings = safety_settings_2
)