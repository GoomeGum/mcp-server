from fastapi import FastAPI, HTTPException
from cache import *
from models import *


app = FastAPI()


@app.on_event("startup")
def startup_event():
    load_cache_from_csv("similarity_results_train.csv")
    load_model()


@app.post("/tool/get_elaborate_description_prompt", response_model=DescriptionResponse)
def get_elaborate_description_prompt(request: ContextRequest):
    prompt = generate_elaborate_prompt(request.context)
    return {"prompt": prompt}

@app.get("/resource/cached_description/{concept_id}", response_model=DescriptionResponse)
def cached_description(concept_id: str):
    prompt = get_cached_description(concept_id)
    if prompt is None:
        raise HTTPException(status_code=404, detail="Concept ID not found in cache")
    return {"prompt": prompt}

@app.get("/resource/cached_description_list", response_model=CacheListResponse)
def cached_description_list():
    return {"descriptions": get_all_cached_descriptions()}