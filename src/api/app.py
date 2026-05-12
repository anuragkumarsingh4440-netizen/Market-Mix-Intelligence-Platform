from fastapi import FastAPI

from src.pipeline.prediction_pipeline import (
    PredictionPipeline,
    CustomData
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message":
        "MarketMix Intelligence API Running"
    }


@app.post("/predict")
def predict_revenue(

    spend: int,
    impressions: int,
    clicks: int,
    conversions: int,
    ctr: float,
    roas: float
):

    data = CustomData(

        spend=spend,

        impressions=impressions,

        clicks=clicks,

        conversions=conversions,

        ctr=ctr,

        roas=roas
    )

    pred_df = data.get_data_as_dataframe()

    prediction_pipeline = PredictionPipeline()

    prediction = prediction_pipeline.predict(
        pred_df
    )

    return {

        "predicted_revenue":
        round(float(prediction[0]), 2)
    }