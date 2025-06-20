from ollama import Client      
client = Client(host="http://localhost:11434")   

MODEL_NAME = "deepseek-r1:7b"     

def generate(question: str, context: list[str]) -> str:
    top_hit = context[0]          # bierzemy tylko najlepsze trafienie
    prompt = (
        "You are a **strict factual assistant**.\n"
        "Rules:\n"
        "1. Use ONLY the information in CONTEXT.\n"
        "2. Quote the sentence that contains the answer.\n"
        "3. Give the answer in one short sentence.\n"
        "4. If the answer is missing, say: I don't know.\n"
        "5. Do NOT reveal your reasoning or use external knowledge.\n\n"
        f"### CONTEXT\n{top_hit}\n\n"
        f"### QUESTION\n{question}\n"
        "### ANSWER (quote + short answer):"
    )
    resp = client.generate(model=MODEL_NAME, prompt=prompt)
    return resp["response"].strip()
