export OLLAMA_HOST="127.0.0.1:8001"
# Without this, ollama will keep telling you to pull the model because it can´t find its models
export OLLAMA_MODELS=/usr/share/ollama/.ollama/models

ollama serve