# mlops-streamlit-ui

Streamlit UI for an MLOps demo, packaged as a Docker image and deployable to Kubernetes/EKS via Helm.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Build container
```bash
docker build -t mlops-streamlit-ui:local .
docker run -p 8501:8501 -e API_URL=http://localhost:8000 mlops-streamlit-ui:local
```

## Helm (render templates)
```bash
helm template mlops-streamlit-ui ./helm/mlops-streamlit-ui
```
